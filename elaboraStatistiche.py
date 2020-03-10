import pandas as pd
import re
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def elabora(nomefile):
    file = pd.read_csv(nomefile + '.csv')
    result = open('statistiche -  ' + nomefile + '.txt', 'w')

    #print(file)
    print('totale risultati -> '+str(len(file)))
    result.write('totale risultati -> '+str(len(file)))
    print(file['genere'].value_counts())
    result.write('\n'+str(+file['genere'].value_counts()))

    contatoreSante = 0
    contatoreSanti = 1
    for index, row in file.iterrows():
        if re.search(r's\.', row["via"]) or \
            re.search(r'santa', row["via"]) or \
            re.search(r'santo', row["via"]) or \
                re.search(r' san ', row["via"]):
            if (row['genere']) is 'm':
                contatoreSanti += 1
            else:
                contatoreSante += 1
    print('Santi di genere maschile -> '+str(contatoreSanti))
    result.write('\nSanti di genere maschile -> '+str(contatoreSanti))

    print('Santi di genere femminile -> '+str(contatoreSante))
    result.write('\nSanti di genere femminile -> '+str(contatoreSante))

