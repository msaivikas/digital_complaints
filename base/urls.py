from django.urls import path
from . import views
from .views import ComplaintList

urlpatterns = [
    # path('', views.index, name='index'),
    path('', ComplaintList.as_view(), name = 'complaint_list'),
]