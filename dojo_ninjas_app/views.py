from django.shortcuts import render ,redirect
from .models import *

def index(request):
    context= {
        "dojos" :Dojo.objects.all(),
        "ninjas": Ninja.objects.all()
    }
    return render(request , 'dojo_ninjas_app/index.html' , context)


def create_dojo(request):
    if request.method == 'POST' :
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']

        Dojo.objects.create(name=name , city=city ,state=state)

        return redirect('/')
    return redirect('/')


def create_ninja(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dojo_id = request.POST['dojo']

        dojo = Dojo.objects.get(id=dojo_id)

        Ninja.objects.create(first_name=first_name , last_name=last_name , dojo=dojo)
        return redirect('/')
    return redirect('/')


def delete_dojo(request , dojo_id):
    if request.method == 'POST':
        dojo = Dojo.objects.get(id=dojo_id)
        dojo.delete()

        return redirect('/')
    return redirect('/')
