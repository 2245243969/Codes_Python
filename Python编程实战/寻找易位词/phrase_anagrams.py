import sys
from collections import Counter
import load_dictionary

dict_file=load_dictionary.load('2of4brif.txt')
#保证下面使用的字母i和a都是小写
dict_file.append('a')
dict_file.append('i')
dict_file=sorted(dict_file)

ini_name=input("Enter a name:")

def find_anagrams(name,word_list):
    """根据用户输入的名字，在字典中寻找其易位词短语，输出最终找到的易位短语"""
    name_letter_map=Counter(name)
    anagrams=[]
    for word in word_list:
        text=''
        word_letter_map=Counter(word.lower())
        for letter in word:
            if word_letter_map[letter]<=name_letter_map[letter]:
                text+=letter
            if Counter(text)==word_letter_map:
                anagrams.append(word)
    print(*anagrams,sep='\n')