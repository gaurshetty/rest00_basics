from django.urls import path
from . import views


urlpatterns = [
    path('1/', views.employee_data_view),
    path('2/', views.employee_data_jsonview),
    path('3/', views.employee_data_jsondirectview),
    path('4/', views.JsonCBV.as_view()),
    path('5/', views.JsonCBV2.as_view()),
]
