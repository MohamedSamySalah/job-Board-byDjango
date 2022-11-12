from django.contrib import admin

# import models here 
from .models import Jobs,Category
# Register your models here.

admin.site.register(Jobs)
admin.site.register(Category)