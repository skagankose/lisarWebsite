from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponseRedirect
from .models import *
from .forms import *

# Homepage
def home(request):

    context = {}
    return render(request, 'home.html', context)

def studentDetails(request, pk):

    student = get_object_or_404(Student, pk=pk)
    context = {'student': student}

    return render(request,'studentDetails.html', context)

def students(request):

    students = Student.objects.all()
    context = {'students': students}

    return render(request,'students.html', context)


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


# Ders Kaydi
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


# Dönem Kaydi
def donemkaydi(request):
    if request.method == 'POST':
        form = DonemKayit(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')

    else:
        form = DonemKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Dönem'})


# Sınıf Kaydi
def sinifkaydi(request):
    if request.method == 'POST':
        form = SinifKayit(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')

    else:
        form = SinifKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Sınıf'})
