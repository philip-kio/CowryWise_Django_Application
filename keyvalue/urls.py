from django.db.models.base import Model
from django.urls import path
from .views import  createTimeView

urlpatterns = [

    path('list/', createTimeView, name='create')

]