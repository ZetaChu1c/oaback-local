from django.urls import path
from . import views


urlpatterns = [
    path("upload", views.UploadAttachmentView.as_view(), name="upload"),
]
