import datetime, os

year = int(datetime.datetime.now().strftime("%Y"))
base_url = 'https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis'
        
def download_demonstracoes() -> None:
    try:
        for y in range(year-2, year):
            for quarter in range(1,5):
                os.system(f'wget -P /tmp/{y}/ {base_url}/{y}/{quarter}T{y}.zip --no-verbose')
    except Exception as e:
        print(e)
    return None  

def unzip_demonstracoes() -> None:
    try:
        os.system("rm -r /demonstracoes_contabeis/")
        for y in range(year-2, year):
            os.system(f'mkdir -p /demonstracoes_contabeis/{y}/')
            for quarter in range(1,5):
                os.system(f'unzip -d  /demonstracoes_contabeis/{y} /tmp/{y}/{quarter}T{y}.zip')
        os.system("rm -r /tmp/")
    except Exception as e:
        print(e)
    return None
    
if __name__ == "__main__":
    download_demonstracoes()
    unzip_demonstracoes()