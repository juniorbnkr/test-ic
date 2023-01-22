FROM python:3.8.3-slim

WORKDIR /

#system pkgs 
RUN apt-get update
RUN apt-get -y install wget
RUN apt-get -y install unzip
RUN apt-get -y install zip
RUN apt-get -y install file

# #python packages
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./requirements.txt /
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# Copiando a pasta do projeto
COPY ./ /
RUN chmod +x /init.sh


# subindo o app
CMD  ["/init.sh"]
