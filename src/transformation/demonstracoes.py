import pandas as pd
from sqlalchemy import create_engine  
import os, datetime, subprocess, logging, utils

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

def process_demonstracoes(year,quarter)->bool:
    try:
        file_info = subprocess.run(['file', f'/demonstracoes_contabeis/{year}/{quarter}T{year}.csv'], capture_output=True).stdout.decode()
        if 'ISO-8859' in file_info:
            encode = 'latin1'
        elif 'UTF-8' in file_info:
             encode = 'utf8'
             
        df = pd.read_csv(f"/demonstracoes_contabeis/{year}/{quarter}T{year}.csv",
                        sep=";", encoding=encode)
        df['DATA'] = pd.to_datetime(df['DATA'])
        df['VL_SALDO_FINAL'] = pd.to_numeric(df['VL_SALDO_FINAL'].str.replace(',','.'))

        if 'VL_SALDO_INICIAL' in df.columns:
            df['VL_SALDO_INICIAL'] = pd.to_numeric(df['VL_SALDO_INICIAL'].str.replace(',','.'))
        else:
            df['VL_SALDO_INICIAL'] = None
            
        df['ANO'] = year
        df['TRIMESTRE'] = quarter
        df.to_sql('demonstracoes_contabeis',
                con=dbConnection,schema="ic-test",
                if_exists="append",
                index_label='id'
                )            
    except Exception as e:
        logger.warning(e)
        return False
    
    return True   

if __name__ == '__main__':
    year = int(datetime.datetime.now().strftime("%Y"))
    for y in range(year-2, year):
        for quarter in range(1,5):
            logger.debug(f"processing demonstracoes: {quarter}T{y}")
            if process_demonstracoes(y,quarter):
                logger.info(f'  -- finished: {quarter}T{y}')
            else:
                logger.error(f'error: {quarter}T{y}')