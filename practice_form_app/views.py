from django.shortcuts import render
from .form import practice_form
# Create your views here.
def about(request):
    
    if request.method == "POST":
        form = practice_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else :
        form = practice_form()
    return render(request,'about.html',{'form':form})