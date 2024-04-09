cities = {
    'Guangzhou': {'country': '中国',
                  'population': '1874.41万人',
                  'fact': '别名是花城或者是五羊城', },
    'Shanghai': {'country': '中国',
                 'population': '2487.4万人',
                 'fact': '中国四大一线城市之一', },
    'Chendu': {'country': '中国',
               'population': '2140.3万人',
               'fact': '九寨沟是国家5A级景区', },

}
for city, city_info in cities.items():
    print(f"\nCityname:{city}")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\tCountry:{country}")
    print(f"\tPopulation:{population}")
    print(f"\tfact:{fact}")
