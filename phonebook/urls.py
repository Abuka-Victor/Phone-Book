from django.urls import path
from .views import index

app_name = 'pb'

urlpatterns = [
    path('', index)
]