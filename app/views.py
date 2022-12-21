from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def django_forms(request):
    form=NameForm()
    d={'form':form}
    if request.method=="POST":
        form_data=NameForm(request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data['name']
            age=form_data.cleaned_data['age']
            email=form_data.cleaned_data['email']
            gender=form_data.cleaned_data['gender']
            course=form_data.cleaned_data['course']
            d1={'n':name,'a':age,'e':email,'g':gender,'c':course}

            return render(request,'form_data.html',d1)
    return render(request,'django_forms.html',d)