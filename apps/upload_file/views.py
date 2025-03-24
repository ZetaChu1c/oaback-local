from rest_framework.views import APIView
from .serializers import UploadAttachmentSerializer
from django.conf import settings
from rest_framework.response import Response
import os


class UploadAttachmentView(APIView):
    def post(self, request):
        serializer = UploadAttachmentSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data.get("file")
            filename = file.name
            path = settings.MEDIA_ROOT / filename
            file_path = settings.MEDIA_URL + filename
            try:
                with open(path, "wb") as f:
                    for chunk in file.chunks():
                        f.write(chunk)
            except Exception:
                return Response({"errno": 1, "message": "上传文件失败"})
            return Response(
                {
                    "errno": 0,
                    "data": {"url": file_path},
                }
            )
        else:
            print(serializer.errors)
            return Response(
                {
                    "errno": 1,
                    "message": list(serializer.errors.values())[0][0],
                }
            )
