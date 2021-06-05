from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='blogs-frontship'),
    path('Home/', views.home, name='blogs-home'),
   # path('frontship/', views.front, name='blogs-frontship'),
    path('register/', views.add, name='blogs-register'),
    path('submit/', views.add, name='blogs-register'),
    path('dashboard/', views.dashboard, name='blogs-dashboard'),
]


'''
[{% for dess in des %} '{{ dess.orgin }}', {% endfor %}]
'''