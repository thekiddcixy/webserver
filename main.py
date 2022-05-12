from flask import Flask

app = Flask("quarta_c")

@app.get('/')
def benvenuto():
    return "benvenuto nel sito di Alessandro Montefusco"

@app.get('/contatti')
def marconi():
    return " Via Ciro Corradetti, 2, 00053 Civitavecchia RM"

@app.get('/errore')
def errore():
    return 100

@app.get('/insert')
def insert():
    return "Inserimento avvenuto con successo",201

app.run() #app.run("0.0.0.0") su una ip esterna