from django.shortcuts import render


# Create your views here.


def Test(request):    
    context = {}
    return render(request, "task/test.html", context)