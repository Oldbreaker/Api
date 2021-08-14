from rest_framework import serializers


class ArchivoSerealizer(serializers.Serializer):
    filename = serializers.CharField(max_length=100)
    filelocation = serializers.CharField(max_length=100)
