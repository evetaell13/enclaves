from django.urls import path, include, re_path
from .views import index
from django.conf import settings

app_name = 'enclaves_main'
urlpatterns = [
    path('', index, name='index'),
    re_path(r'^accounts/', include('enclaves_auth.urls')),
]
