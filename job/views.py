from django.shortcuts import render
from .models import Jobs,Category
# Create your views here.


def all_jobs(request):
    job_list = Jobs.objects.all()
    category_list = Category.objects.all()
    context = {
        'jobs': job_list,
        'job_cat': category_list
    }
    return render(request,'alljobs.html',context)

def job_detalis(request,id):
    job = Jobs.objects.get(id = id)
    context={
        'job': job
    }
    return render(request,'job_details.html',context)