from django.shortcuts import render,redirect
from .form import RegisterForm 
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
def success(request):
    return render(request, 'index.html')