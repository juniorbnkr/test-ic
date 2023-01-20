import os,datetime
import pandas as pd

def convert_to_csv(filename,sheet_name='Anexo I_Rol de Procedimentos') -> None:
    df = pd.read_excel(filename,sheet_name=sheet_name,header=4)
    df.rename(columns={"OD": "Seg. Odontológica","AMB": "Seg. Ambulatorial"}, inplace=True)
    df.to_csv(f"/rol_procedimentos/{datetime.datetime.now().strftime('%Y%m%d')}.csv.zip",
              sep=';',
              index=False,
              quotechar="'",
              compression='zip'
              )
    return None

if __name__ == "__main__":   
    os.system("mkdir /csv/")
    zips = [x.split(".")[0] for x in os.listdir("/attachments/")]
    csvs = [x.split(".")[0] for x in os.listdir("/rol_procedimentos/")]

    for file in zips:
        if file not in csvs:
            os.system(f"unzip -d /attachments/{file} /tmp/" )
            convert_to_csv('/tmp/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536_RN537_RN538_RN539_RN541_RN542_RN544_546.xlsx')
        
    os.system("rm -r /tmp/")