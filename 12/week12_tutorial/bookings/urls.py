# bookings/urls.py
from django.urls import path

from bookings import views

urlpatterns = [
    path("", views.BookingList.as_view(), name="booking-list"),
    path("create/", views.BookingCreate.as_view(), name="booking-create"),
    path("update/<int:booking_id>", views.BookingUpdate.as_view(), name="booking-update"),
    path("delete/<int:booking_id>", views.BookingDelete.as_view(), name="booking-delete"),
    ##สาเหตุที่ไม่ใส่ login logout ในนี้เพราะไม่งั้นมันจะเป็น bookings/login แต่จริงๆไม่ผิด แค่ path แปลกๆ
]