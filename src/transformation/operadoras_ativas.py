import pandas as pd
from sqlalchemy import create_engine  
import os,logging, utils

logger = logging.getLogger("_")
logger.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(utils.CustomFormatter())
logger.addHandler(ch)

db_server = os.environ.get('db_server')
db_pass = os.environ.get('db_pass')
db_user = os.environ.get('db_user')

pd.options.display.float_format = '{:.2f}'.format

sqlEngine       = create_engine(f'mysql+pymysql://{db_user}:@{db_server}/ic-test?password={db_pass}', pool_recycle=3600)
dbConnection    = sqlEngine.connect()

def process_operadoras_ativas()->bool:
    try:
        df = pd.read_csv('Relatorio_cadop(1) (2) (1).csv',
                        sep=';',
                        header=1,
                        encoding='latin1')
        df.rename(columns={"Registro ANS": "registro_ans",
                        "CNPJ":'cnpj',
                        "Razão Social":'razao_social',
                        "Nome Fantasia":"nome_fantasia",
                        "Modalidade":"modalidade",
                        "Logradouro":'logradouro',
                        "Número":"numero",
                        "Modalidade":"modalidade",
                        "Complemento":'complemento',
                        "Bairro":"bairro",
                        "Cidade":"cidade",
                        "UF":'uf',
                        "CEP":"cep",
                        "DDD":"ddd",
                        "Telefone":"telefone",
                        "Fax":"fax",
                        "Endereço eletrônico":"email",
                        "Representante":"representante",
                        "Cargo Representante":"cargo_representante",
                        "Data Registro ANS":"data_registro_ans",
                        }, inplace=True)
            
        df['data_registro_ans'] = pd.to_datetime(df['data_registro_ans'])
        df['cnpj'] = df['cnpj'].astype(str)
        df['fax'] = df['fax'].astype(str)
        df['telefone'] = df['telefone'].astype(str)
        df['cep'] = df['cep'].astype(str)
                
        df.to_sql('operadoras_ativas',
                        con=dbConnection,schema="ic-test",
                        if_exists="append",
                        index_label='id'
                        )                
    except Exception as e:
        logger.warning(e)
        return False
    
    return True 

if __name__ == '__main__':
    if process_operadoras_ativas():
        logger.info(f'finished')
    else:
        logger.error(f'error')