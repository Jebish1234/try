from django.shortcuts import redirect, render,HttpResponse
from .models import Jobs
from .forms import Create 

# Create your views here.

def home(request):
    query = Jobs.objects.all()
    context = {
        "que" : query
    }
    return render(request,'home.html',context)

def create(request):
    if request.method == "POST":
        fo = Create(request.POST or None)
        if fo.is_valid:
            try:
                fo.save()
                return redirect('/')
            except:
                pass
    
    else:
        fo = Create()

    context = {
        "form" : fo
    }

    return render(request,'create.html',context)