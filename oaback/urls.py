"""
URL configuration for oaback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("api/auth/", include("apps.oaauth.urls")),
    path("api/absent/", include("apps.absent.urls")),
    path("api/inform/", include("apps.inform.urls")),
    path("api/staff/", include("apps.staff.urls")),
    path("api/image/", include("apps.image.urls")),
    path("api/home/", include("apps.home.urls")),
    path("api/file/", include("apps.upload_file.urls")),
] + static("api" + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# http://127.0.0.1:8000/media/86ZnVLYKKWujT2t52WgXJS.jpg
