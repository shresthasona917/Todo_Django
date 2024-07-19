from django.shortcuts import render,redirect
from base.models import Todo

# Create your views here.
def home(request):
    todos_obj = Todo.objects.all()
    context = {'todos':todos_obj}
    return render(request,'index.html',context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Todo.objects.create(name=name, description=description, status=status)
        return redirect('home')
    return render(request,'create.html')

def edit(request,pk):
    todos_obj = Todo.objects.get(id=pk)
    context = {'todos':todos_obj}
    if request.method == "POST":
       todos_obj.name = request.POST.get('name')
       todos_obj.description = request.POST.get('description')
       todos_obj.save()
       return redirect('home')
    return render(request,'edit.html',context)

def delete(request,pk):
    todos_obj = Todo.objects.get(id=pk)
    todos_obj.delete()
    return redirect('home')