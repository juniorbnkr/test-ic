# compose_flask/app.py
from flask import Flask,Response
import pandas as pd
from sqlalchemy import create_engine  
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

db_server = os.environ.get('db_server')
db_pass = os.environ.get('db_pass')
db_user = os.environ.get('db_user')

sqlEngine       = create_engine(f'mysql+pymysql://{db_user}:@{db_server}/ic-test?password={db_pass}', pool_recycle=3600)
dbConnection    = sqlEngine.connect()

@app.route('/<path>')
@app.route('/')
def top_10(path=''):
    if path in ['','ano']:
        filename = 'top_10_ano.sql'
    elif path in ['trimestre']:
        filename = 'top_10_trimestre.sql'

    text_file = open(f"{filename}", "r")
    sql = text_file.read()
    text_file.close()
    
    df = pd.read_sql(sql,
                        con=dbConnection,
                        )     
    return Response(df.to_json(orient="records"), mimetype='application/json')

@app.route('/busca/<search>')
@app.route('/busca/')
def busca(search=''):
    if search == '':
        return 'bad request!', 400
    
    sql = f''' SELECT * FROM `ic-test`.operadoras_ativas
                WHERE razao_social  LIKE "%%{search}%%"
                OR SOUNDEX(nome_fantasia) = SOUNDEX("{search}")
                OR nome_fantasia LIKE "%%{search}%%"; '''
    df = pd.read_sql(sql,
                        con=dbConnection,
                        )     
    return Response(df.to_json(orient="records"), mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True,threaded=False)
    
    
    
    