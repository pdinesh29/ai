from django.urls import path,include
from app import views
urlpatterns=[
    path('',views.v1,name='v1')
]