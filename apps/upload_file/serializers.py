from rest_framework import serializers
from django.core.validators import (
    FileExtensionValidator,
)


class UploadAttachmentSerializer(serializers.Serializer):
    file = serializers.FileField(
        # 允许上传所有类型的文件
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"])],
    )

    def validate_file(self, value):
        # 限制上传文件的大小
        if value.size > 10 * 1024 * 1024:
            raise serializers.ValidationError("文件大小不能超过10MB")
        return value
