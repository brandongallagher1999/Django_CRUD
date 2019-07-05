from django.shortcuts import render

from .models import Worker
# Create your views here.

def get_all_workers(request):
    obj = Worker.objects.all()
    all_workers = { #Returns a list of all workers in DB
        'workers': obj
    }
    return render(request, "index.html", all_workers)