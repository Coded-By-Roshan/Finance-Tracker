from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('khata/', admin.site.urls),
    path('', include('record.urls')),
]
