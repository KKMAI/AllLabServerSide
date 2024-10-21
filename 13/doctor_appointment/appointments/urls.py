from django.urls import path
from appointments import views
from rest_framework.authtoken import views as authen_views


urlpatterns = [
    path('api-token-auth/', authen_views.obtain_auth_token), # sent post request to receive token
    path('doctors/', views.DoctorList.as_view(), name='doctor-list'),
    path('patients/', views.PatientList.as_view(), name='patient-list'),
    path('appointments/', views.AppointmentList.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
]