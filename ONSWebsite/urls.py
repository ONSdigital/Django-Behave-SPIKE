"""
URL configuration for ONSWebsite project.

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
from django.contrib import admin
from django.urls import path, include
from onsApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("onsApp.urls")),
    path("accessibility_statement", views.accessibility_statement, name="accessibility_statement"),
    path("cookies", views.cookies, name="cookies"),
    path("page_1", views.page_1, name="page_1"),
    path("page_2", views.page_2, name="page_2"),
    path("page_3", views.page_3, name="page_3"),
    path("privacy_data", views.privacy_data, name="privacy_data_page"),
]
