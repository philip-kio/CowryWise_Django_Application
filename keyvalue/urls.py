from django.db.models.base import Model
from django.urls import path
from .views import ListTimeUuid, CreateTimeView

urlpatterns = [
    path('', ListTimeUuid.as_view(), name= 'key_value'), 
    path('create/', CreateTimeView.as_view(), name='create')

]