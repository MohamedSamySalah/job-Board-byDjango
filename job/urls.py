from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_jobs,name='alljobs'),
    path('<int:id>',views.job_detalis,name='jobdetails')
]
