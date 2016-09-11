from django.shortcuts import render

# Homepage
def home(request):
    context = {}
    return render(request, 'home.html', context)

# Ogrenci Kaydi
def ogrencikaydi(request):
    context = {}
    return render(request, 'kayit.html', context)

# Ogretmen Kaydi
def ogretmenkaydi(request):
    context = {}
    return render(request, 'kayit.html', context)


# Ogrenci Kaydi
def derskaydi(request):
    context = {}
    return render(request, 'kayit.html', context)
