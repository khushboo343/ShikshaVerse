# materials/views.py

from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from .models import Material, Category
from .forms import MaterialForm

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class MaterialListView(View):
    def get(self, request):
        materials = Material.objects.all()
        return render(request, 'material_list.html', {'materials': materials})

class MaterialSubmissionView(View):
    def get(self, request):
        form = MaterialForm()
        categories = Category.objects.all()
        return render(request, 'material_submission.html', {'form': form, 'categories': categories})

    def post(self, request):
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('material_list')
        else:
            return render(request, 'material_submission.html', {'form': form})

def material_submission(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('material_list')
        else:
            return render(request, 'material_submission.html', {'form': form})
    else:
        form = MaterialForm()
        categories = Category.objects.all()
        return render(request, 'material_submission.html', {'form': form, 'categories': categories})

def material_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            materials = Material.objects.filter(title__icontains=query)
        else:
            materials = []
        return render(request, 'material_search_results.html', {'materials': materials})
    else:
        return HttpResponse('Invalid request.')