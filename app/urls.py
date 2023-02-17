
from django.contrib import admin
from django.urls import path

# from app.views import hello, job
from app import views


urlpatterns = [
    path('', views.hello, name='jobs_home'),
    # path('job/1', views.job),
    path('home', views.home, name='home'),
    path('job/<int:id>', views.job_detail, name='job_detail')
]


