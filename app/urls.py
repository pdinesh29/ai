from django.urls import path,include
from app import views
urlpatterns=[
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('Aichat',views.v1,name='v1')
]