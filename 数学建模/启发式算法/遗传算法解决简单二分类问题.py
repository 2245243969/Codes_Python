#已知一组二维的样本点，以及其相应的标签，通过遗传算法寻求一条直线。
import numpy as np
import matplotlib.pyplot as plt
from random import random, sample, choice, uniform
from math import floor


def data_generate():
    Points = []
    N = 100
    for i in range(N):
        X = uniform(-2.5, 2.5)
        Y = uniform(-2.5, 2.5)
        Points.append((X, Y))
    class_1 = []
    class_2 = []

    for point in Points:
        if point[1] - point[0] - 0.5 > 0:
            class_1.append(point)
        elif point[1] - point[0] + 0.5 < 0:
            class_2.append(point)

    N1 = len(class_1)
    N2 = len(class_2)
    print(N1, N2)
    datas = class_1 + class_2
    labs = [0] * N1 + [1] * N2
    return np.array(datas), np.array(labs)


def my_draw_line(datas, labs, ws, n_cluster=2, str_title=""):
    plt.cla()

    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, n_cluster)]

    # 画点
    for i, lab in enumerate(labs):
        plt.scatter(datas[i, 0], datas[i, 1], s=16., color=colors[lab])

    # 画判决线
    min_x = np.min(datas[:, 0])
    max_x = np.max(datas[:, 0])
    x = np.arange(min_x, max_x, 0.01)

    for i, w in enumerate(ws):
        y = -(x * w[0] + w[2]) / w[1]
        plt.plot(x, y, color=(0, 0, 0, 1.0))

    w = ws[0]
    y = -(x * w[0] + w[2]) / w[1]
    plt.plot(x, y, color=(1.0, 0, 0, 1.0))

    plt.xlim(-2.5, 2.5)
    plt.ylim(-2.5, 2.5)
    plt.title(str_title)
    plt.show()


def sigmoid(z):
    return 1.0 / (1 + np.exp(-z))


def calculate_accuracy(datas, labs, w):
    if len(np.array(w).shape) != 2:
        w = np.array(w)
        w = np.expand_dims(w, axis=-1)

    z = np.dot(datas, w)  # Nx1
    h = sigmoid(z)        # Nx1
    lab_det = (h > 0.5).astype(np.float64)
    error_rate = np.sum(np.abs(labs - lab_det)) / len(labs)
    return error_rate


def CE(X, Y, W):
    if len(np.array(W).shape) != 2:
        W = np.array(W)
        W = np.expand_dims(W, axis=-1)
    z = np.dot(X, W)
    h = sigmoid(z)
    eps = 0.000001
    loss_ce = -np.sum(Y * np.log(h + eps) + (1 - Y) * np.log(1 - h + eps))
    return loss_ce


def loss_SVM(datas, labs, w):
    if len(np.array(w).shape) != 2:
        w = np.array(w)
        w = np.expand_dims(w, axis=-1)
    labs_svm = labs.copy()
    labs_svm = labs_svm * 2 - 1

    z = np.dot(datas, w)  # Nx1
    loss_svm = np.abs(np.sum(z * labs_svm)) / np.linalg.norm(w)
    return -loss_svm


def create_individual(individual_size):
    """
    Create an individual.
    """
    return [uniform(-1, 1) for _ in range(individual_size)]


def create_population(individual_size, population_size):
    """
    Create an initial population.
    """
    return [create_individual(individual_size) for _ in range(population_size)]


def get_fitness(individual, datas, labs):
    error_rate = calculate_accuracy(datas, labs, individual)
    ce_loss = CE(datas, labs, individual)
    svm_loss = loss_SVM(datas, labs, individual)
    return {'CE': ce_loss, 'error': error_rate * 100, 'svm': svm_loss, 'coeff': individual}


def evaluate_population(population, datas, labs, method, selection_size, best_individuals_stash):
    fitness_list = [get_fitness(individual, datas, labs) for individual in population]
    error_list = sorted(fitness_list, key=lambda i: i[method])
    best_individuals = error_list[: selection_size]
    best_individuals_stash.append(best_individuals[0]['coeff'])

    print('Error: ', best_individuals[0]['error'],
          'CE: ', best_individuals[0]['CE'],
          'svm', best_individuals[0]['svm'])

    return best_individuals


def crossover(parent_1, parent_2):
    individual_size = len(parent_1['coeff'])
    loci = [i for i in range(0, individual_size)]
    loci_1 = sample(loci, floor(0.5 * individual_size))
    loci_2 = [i for i in loci if i not in loci_1]

    child = np.zeros(individual_size)
    child[loci_1] = np.array(parent_1['coeff'])[loci_1]
    child[loci_2] = np.array(parent_2['coeff'])[loci_2]
    return child.tolist()


def mutate(individual, probability_of_gene_mutating):
    individual_size = len(individual)
    loci = [i for i in range(0, individual_size)]
    no_of_genes_mutated = floor(probability_of_gene_mutating * individual_size)
    loci_to_mutate = sample(loci, no_of_genes_mutated)

    for locus in loci_to_mutate:
        gene_transform = choice([-1, 1])
        change = gene_transform * random()
        individual[locus] = individual[locus] + change
    return individual


def get_new_generation(selected_individuals, population_size, probability_of_individual_mutating, probability_of_gene_mutating):
    parent_pairs = [sample(selected_individuals, 2) for _ in range(population_size)]
    offspring = [crossover(pair[0], pair[1]) for pair in parent_pairs]

    offspring_indices = [i for i in range(population_size)]
    offspring_to_mutate = sample(
        offspring_indices,
        floor(probability_of_individual_mutating * population_size)
    )

    mutated_offspring = [[i, mutate(offspring[i], probability_of_gene_mutating)]
                         for i in offspring_to_mutate]
    for child in mutated_offspring:
        offspring[child[0]] = child[1]
    return offspring


if __name__ == "__main__":
    datas_in, labs_in = data_generate()

    N, D = np.shape(datas_in)
    datas = np.c_[datas_in, np.ones([N, 1])]
    labs = np.expand_dims(labs_in, axis=-1)

    individual_size = len(datas[0])
    population_size = 1000
    rate_select = 0.2
    selection_size = floor(rate_select * population_size)
    max_generations = 50
    probability_of_individual_mutating = 0.1
    probability_of_gene_mutating = 1
    best_individuals_stash = [create_individual(individual_size)]

    initial_population = create_population(individual_size, population_size)
    current_population = initial_population
    method = 'svm'

    for i in range(max_generations):
        plt.ion()
        current_best_individual = get_fitness(best_individuals_stash[-1], datas, labs)
        print('Generation: ', i)
        best_individuals = evaluate_population(current_population, datas, labs, method,
                                               selection_size, best_individuals_stash)
        current_population = get_new_generation(best_individuals, population_size,
                                                probability_of_individual_mutating,
                                                probability_of_gene_mutating)

        ws = [individual['coeff'] for individual in best_individuals]
        str_title = "Generation %d Error=%.1f CE=%.3f svm=%.1f" % (i,
                                                                   best_individuals[0]['error'],
                                                                   best_individuals[0]['CE'],
                                                                   best_individuals[0]['svm'])
        my_draw_line(datas_in, labs_in, ws, n_cluster=2, str_title=str_title)
        plt.pause(0.5)
        plt.ioff()

    my_draw_line(datas_in, labs_in, [best_individuals_stash[-1]], n_cluster=2)
    plt.show()
