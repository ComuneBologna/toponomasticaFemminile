import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def controllaDuplicati(nomeFile):
    df = pd.read_csv(nomeFile+'.csv',index_col=False)
    df = df.drop_duplicates(subset=['nomi','via'], keep='last')
    duplicateRowsDF = df[df.duplicated(['via'],keep=False)]
    for index, row in duplicateRowsDF.iterrows():
        stringIndex = (row['via'].index(row['nomi']))
        newdf = (df[df.via == row['via']])
        if len(newdf) == 1:
            continue
        for index2, row2 in newdf.iterrows():
            stringIndex2 = (row['via'].index(row2['nomi']))
            if (stringIndex == stringIndex2):
                continue
            if (stringIndex > stringIndex2):
                #print(str(row['nomi']))
                df = df.drop(index)
                break
            if (stringIndex < stringIndex2):
                #print('droppo')
                #print(str(row2['nomi']))
                df = df.drop(index2)
                break

    duplicateRowsDF = df[df.duplicated(['via'],keep=False)]
    print("Duplicate Rows  are:", duplicateRowsDF, sep='\n')

    if len(duplicateRowsDF) != 0:
        df.to_csv(nomeFile+'__clean.csv', index=False)
    else:
        print('no Duplicates found')