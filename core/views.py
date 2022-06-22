from django.shortcuts import render,redirect
from django.http import HttpResponse
from core.form import ToDoForm
from core.models import ToDo

def home(request):
    # creating object for form
    form=ToDoForm()
    todos=ToDo.objects.all()
    if request.method=='POST':
        form=ToDoForm(request.POST)
        if form.is_valid():      
            form.save()             
    return render(request,'home.html',{'form':form,'todo':todos})

def update(request,todo_id):
    todo=ToDo.objects.get(id=todo_id)
    form=ToDoForm(instance=todo)
    if request.method=='POST':
        form=ToDoForm(request.POST,instance=todo)
        if form.is_valid():      
            form.save()
            return redirect('home')   
    return render(request,'update.html',{'form':form})

def delete(request,todo_id):
    todo=ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')
# Create your views here.
