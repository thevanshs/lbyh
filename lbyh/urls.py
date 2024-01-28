from django.contrib import admin
from django.urls import path
from homepage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage , name="Homepage"),
]
