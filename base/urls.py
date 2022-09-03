from django.urls import path
from . import views
from .views import ComplaintList, ComplaintAdd, ComplaintDetail

urlpatterns = [
    path('', ComplaintList.as_view(), name = 'complaint_list'),
    path('complaint-add', ComplaintAdd.as_view(), name = 'complaint_add'),
    path('complaint/<int:pk>/', ComplaintDetail.as_view(), name = 'complaint_detail'),
]