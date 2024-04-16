from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.

def receipes(request):
    if request.method == "POST":
        data=request.POST 

        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image

        )
        return redirect('/receipes')
    queryset= Receipe.objects.all()
    context={"receipes":queryset}
    return render(request,'receipes.html',context)


def delete_receipe(request,id):
    queryset= Receipe.objects.get(id =id)
    queryset.delete()

    return redirect('/receipes/')


def update_receipe(request,id):
    queryset=Receipe.objects.get(id =id)
    if request.method == 'POST':
        data= request.POST

        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        queryset.receipe_name =receipe_name
        queryset.receipe_description=receipe_description

        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.save()

        return redirect('/receipes/')




    context = {'receipe':queryset}
    return render(request,'update_recepies.html',context)
