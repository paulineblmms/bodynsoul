from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", include("admin.urls", namespace="admin")),
    path("", include("main.urls")),
    path("", include("authentication.urls", namespace="authentication")),
    path("", include("calorie_tracking.urls", namespace="calorie_tracking")),
    path("", include("list_information.urls", namespace="list_information")),
    path("", include("problem_report.urls", namespace="problem_report"))
]
