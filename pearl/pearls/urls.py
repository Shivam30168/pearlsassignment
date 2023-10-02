# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',views.DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', views.DoctorDetail.as_view(), name='doctor-detail'),
    path('book-appointment/', views.BookAppointment.as_view(), name='book-appointment'),
]
