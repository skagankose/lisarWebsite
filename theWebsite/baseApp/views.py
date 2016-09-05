from django.shortcuts import render

# Homepage
def home(request):
    
    context = {}
    return render(request, 'home.html', context)
