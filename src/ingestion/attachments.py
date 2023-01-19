import requests, os, datetime
from bs4 import BeautifulSoup

def save_attachments() -> None:
    URL = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    os.system("mkdir /attachments/")

    anexos = ['Anexo I - Lista completa de procedimentos (.pdf)',
            'Anexo I - Lista completa de procedimentos (.xlsx)',
            'Anexo II - Diretrizes de utilização (.pdf)',
            'Anexo III - Diretrizes clínicas (.pdf)',
            'Anexo IV - Protocolo de utilização (.pdf)',]

    links = soup.find_all("a",class_='internal-link')

    for link in links:
        if link.text.strip() in anexos:
            os.system(f"wget -P /tmp/ {link['href']} --no-verbose")

    os.system(f"zip -FSrj /attachments/{datetime.datetime.now().strftime('%Y%m%d')}.zip /tmp/*")
    os.system("rm -r /tmp/")

if __name__ == "__main__":
    save_attachments()
