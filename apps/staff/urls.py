from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = "staff"

router = DefaultRouter(trailing_slash=False)
router.register("staff", views.StaffViewSet, basename="staff")
router.register("modify", views.ModifyDepartmentViewSet, basename="department_modify")

urlpatterns = [
    path("departments", views.DepartmentListView.as_view(), name="departments"),
    # path('staff', views.StaffView.as_view(), name='staff_view'),
    path("active", views.ActiveStaffView.as_view(), name="active_staff"),
    path("download", views.StaffDownloadView.as_view(), name="download_staff"),
    path("upload", views.StaffUploadView.as_view(), name="upload_staff"),
    # path("test/celery", views.TestCeleryView.as_view(), name="test_celery"),
    path("department", views.DepartmentAddView.as_view(), name="department_add"),
] + router.urls