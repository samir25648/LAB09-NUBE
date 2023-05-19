from django.shortcuts import render, redirect
from .models import MyModel
from .forms import MyModelForm

def index(request):
    items = MyModel.objects.all()
    return render(request, 'index.html', {'items': items})

def create(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyModelForm()
    return render(request, 'create.html', {'form': form})

def delete(request, item_id):
    item = MyModel.objects.get(id=item_id)
    item.delete()
    return redirect('index')
