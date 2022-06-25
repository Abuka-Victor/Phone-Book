from django.urls import path
from .views import index, contact_detail, contact_delete, contact_create

app_name = 'pb'

urlpatterns = [
    path('', index, name="home"),
    path('create/', contact_create, name="create"),
    path('<int:id>/', contact_detail, name="detail"),
    path('delete/<int:id>/', contact_delete, name='delete'),
]