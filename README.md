## Open Data e toponomastica femminile

Script python relativo al lavoro 'open data e toponomastica femminile, pubblicato al seguente link [Open Data e Toponomastica Femminile!](http://dati.comune.bologna.it/node/4224)

# Elenco dei file:

nomif.txt -> dizionario nomi femminili

nomim.txt -> dizionario nomi maschili

stradario.csv -> stradario della città di Bologna 

**scriptStradario.py** -> script principale, da eseguire

**elaboraStatistiche.py** -> script per elaborare statistiche sui risultati (n.b. viene lanciato in automatico al termine dell'esecuzione di scriptStradario.py)

**controlloDuplicati.py** -> script che controlla che non siano presenti duplicati nel file di output  (n.b. viene lanciato in automatico al termine dell'esecuzione di scriptStradario.py)


# Dipendenze e librerie utilizzate:
[pandas](https://pandas.pydata.org/)


# Fonti:
[Stradario](http://dati.comune.bologna.it/node/3144)

[Dizionario nomi maschili](https://github.com/kalos/italian-wordlists/blob/master/nomi_maschili)

[Dizionario nomi femminili](https://github.com/kalos/italian-wordlists/blob/master/nomi_femminili)


# Credits:

DataTeam del Comune di Bologna

SIT – Sistema Informativo Territoriale del Comune di Bologna

@kalos per il database di nomi maschili e femminili 
