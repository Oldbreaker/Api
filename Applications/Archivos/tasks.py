from __future__ import absolute_import, unicode_literals
import sys
import requests
import os
import json
import pandas as pd
from pathlib import Path
from celery import shared_task


@shared_task
def proceso(filelocation: str):
    obj = Path(filelocation)
    if obj.exists():
        path = 'C:/Users/amdat/Desktop/processed-data/'
        uuid = filelocation.rsplit('/', 2)[-2]
        filename = filelocation.rsplit('/', 1)[-1]
        source = filelocation.rsplit('/', 1)[-2]
        destination = path+uuid+'/'+filename
        df = pd.read_csv(filelocation)
        check = df.isna().any().any()
        if check:
            raise ValueError('El archivo contiene datos Nulos')
        else:
            df.columns = map(lambda x: str(x).upper(), df.columns)
            os.mkdir(path + uuid)
            df.to_csv(destination, index=False, encoding='utf-8')
            send_notification(uuid, filename, source, destination)
            metadata(filelocation,  uuid)


def send_notification(uuid: str, filename: str, source: str, destination: str):
    url = 'http://127.0.0.1:8000/notificacion'
    payload = {'UUID': uuid, 'event_type': 'FILEPROCESSED',
               'event_data': {'filename': filename, 'filepath': source, 'move-to': destination,
                              'elapse-time': 'tiempo'}}
    requests.post(url, json=payload)


def metadata(filelocation:  str, uuid: str):
    url = 'C:/Users/amdat/Desktop/metadata/'
    df1 = pd.read_csv(filelocation)
    os.mkdir(url+uuid)
    headers = str(df1.columns)
    filas = str(len(df1.index))
    memoria = str(sys.getsizeof(df1))
    f = open(url+uuid+'/datos.txt', "w")
    f.write("Filas del archivo: "+filas+os.linesep)
    f.write("Bytes: "+memoria+os.linesep)
    f.write("Headers: "+headers)
    f.close()
