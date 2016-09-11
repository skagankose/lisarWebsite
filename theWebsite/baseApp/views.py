from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *



# Homepage
def home(request):
    context = {}
    return render(request, 'home.html', context)

# Ogrenci Kaydi
def ogrencikaydi(request):
    if request.method == 'POST':
        form = OgrenciKayit(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')

    else:
        form = OgrenciKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Öğrenci'})


# Ogretmen Kaydi
def ogretmenkaydi(request):
    if request.method == 'POST':
        form = OgretmenKayit(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')

    else:
        form = OgretmenKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Öğretmen'})


# Ogrenci Kaydi
def derskaydi(request):
    if request.method == 'POST':
        form = DersKayit(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')

    else:
        form = DersKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Ders'})
