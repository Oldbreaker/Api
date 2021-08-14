import os
import shutil
import requests
import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serealizers import ArchivoSerealizer
from .tasks import proceso


class File(APIView):

    def send_notification(self, uuid: str, filename: str, source: str, destination: str):
        url = 'http://127.0.0.1:8000/notificacion'
        time = datetime.datetime.now()
        payload = {'UUID': uuid, 'event_type': 'FILERECEIVED',
                   'event_data': {'filename': filename, 'filepath': source, 'move-to': destination,
                                  'receivded-timestamp': str(time)}}
        requests.post(url, json=payload)

    def retrive_file(self, filename: str, filelocation: str):
        uuid = filelocation.rsplit('/', 1)[-1]
        path = 'C:/Users/amdat/Desktop/work/'
        source = filelocation + '/' + filename
        destination = path+uuid+'/'+filename
        os.mkdir(path + uuid)
        shutil.move(source, destination)
        self.send_notification(uuid, filename, source, destination)
        proceso.delay(destination)

    def post(self, request):
        serealizer = ArchivoSerealizer(data=request.data)
        if serealizer.is_valid(raise_exception=True):
            filename = serealizer.data['filename']
            filelocation = serealizer.data['filelocation']
            self.retrive_file(filename, filelocation)
            return Response({'message': 'Solicitud Hecha'}, status=status.HTTP_201_CREATED)
        return Response(serealizer.errors, status=status.HTTP_400_BAD_REQUEST)
