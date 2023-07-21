from django.shortcuts import render
from.forms import studentR
# Create your views here.
def add (request):
    if request.method == 'POST':
        fm=studentR(request.POST)
        if fm.is_valid():
             fm.save()
    else:
            fm=studentR()
    return render(request,'add.html',{'formss':fm})