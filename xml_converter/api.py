from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .logic import xml_file_to_json
from .serializers import UploadFileSerializer


class ConverterViewSet(ViewSet):
    parser_classes = [MultiPartParser, ]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid():
            uploaded_file = serializer.validated_data['file']
            json_response = xml_file_to_json(uploaded_file)
            return Response(json_response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
