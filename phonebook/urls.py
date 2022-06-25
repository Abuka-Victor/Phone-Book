from django.urls import path
from .views import index, contact_detail

app_name = 'pb'

urlpatterns = [
    path('', index, name="home"),
    path('<int:id>/', contact_detail, name="detail")
]