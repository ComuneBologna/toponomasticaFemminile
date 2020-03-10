# -*- coding: utf-8 -*-
from datetime import datetime
import pandas as pd
import re
import os
from bisect import bisect_left
import time
from elaboraStatistiche import elabora
from controlloDuplicati import controllaDuplicati

start = time.time()

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

datelog = str(datetime.now().strftime("%Y-%m-%d_%H%M%S"))

print('log started -> log -  ' + datelog + '.csv')
result = open('result -  ' + datelog + '.csv', 'w')
result.write('nomi,genere,via')

nomim = open("nomim.txt", 'r').read().split('\n')
nomif = open("nomif.txt", 'r').read().split('\n')
nomim.sort()
nomif.sort()

print("trovati " + str(len(nomim) + len(nomif)) + ' nomi')

stradario = pd.read_csv("stradario.csv", encoding='unicode_escape')


def binary_search(lst, el):
    el = el.replace('ss.', '').replace('s.', '').replace('s. ', '').strip()
    index = bisect_left(lst, el)
    if index < len(lst) and lst[index] == el:
        return index
    else:
        return -1


def searchAndWrite(nome, gen, via):
    if re.search(r'\b' + nome + r'\b..', via) or \
            re.search(r'\bs\.' + nome + r'\b', via) or \
            re.search(r'\bs\. ' + nome + r'\b', via) or \
            re.search(r'\bss\.' + nome + r'\b', via) or \
            re.search(r'\bss\. ' + nome + r'\b', via):
        elem = str(str(nome) + ',' + str(gen) + ',' + str(via))
        result.write('\n' + elem)


def compare(via):
    stradaElems = via.split()
    for elem in stradaElems:
        indexm = binary_search(nomim, elem)
        indexf = binary_search(nomif, elem)
        if indexm > -1:
            return searchAndWrite(nomim[indexm], 'm', via)
        elif indexf > -1:
            return searchAndWrite(nomif[indexf], 'f', via)


if __name__ == '__main__':
    print('trovate ' + str(len(stradario)) + ' strade')
    for index, row in stradario.iterrows():
        strada = row['NOME_VIA'].lower().strip()
        compare(strada)
    result.close()

    temp = pd.read_csv('result -  ' + datelog + '.csv')
    print('trovati ' + str(len(temp)) + ' risultati')
    os.remove('result -  ' + datelog + '.csv')
    temp.sort_values(by=['genere'], inplace=True)
    temp.drop_duplicates(subset=['nomi', 'genere', 'via'], keep='last', inplace=True)
    temp.to_csv('result2 -  ' + datelog + '.csv', index=False)
    end = time.time()
    print('Fine. Tempo impiegato -> '+str(end - start))
    controllaDuplicati('result2 -  ' + datelog)
    elabora('result2 -  ' + datelog)
