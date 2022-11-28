from django.urls import path
from . import views

app_name='job'

urlpatterns = [
    path('',views.all_jobs,name='alljobs'),
    path('<int:id>',views.job_detalis,name='jobdetails')
]
