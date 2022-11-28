from django.shortcuts import render
from .models import Jobs,Category
from django.core.paginator import Paginator

# Create your views here.


def all_jobs(request):
    job_list = Jobs.objects.all()
    category_list = Category.objects.all()
    p = Paginator(job_list, 3) 
    # print('number of object',p.count)
    # print('number of page contain objects',p.num_pages)
    # print('number of page range',p.page_range)
    # print("-"*45)
    # page1 = p.page(1)
    # print(page1)
    # print(page1.object_list)
    # print("-"*45)
    # print(page1.has_next())
    # print(page1.has_previous())
    # print(page1.next_page_number())
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = p.get_page(page_number)
    
    context = {
        'jobs': page_obj,
        'job_cat': category_list
    }
    return render(request,'alljobs.html',context)

def job_detalis(request,id):
    job = Jobs.objects.get(id = id)
    context={
        'job': job
    }
    return render(request,'job_details.html',context)