from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaulttags import register
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

    if request.method == 'POST':
        fullName = request.POST['fullName']
        mailAdress = request.POST['mailAdress']

        studentList = Student.objects.filter(fullName__contains=fullName,\
                                             mailAddress__contains=mailAdress)
        paginator = Paginator(studentList, 15)
        page = request.GET.get('page')

        try:
            students = paginator.page(page)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)


        context = {'students': students}

        return render(request,'students.html', context)

    else:

        studentList = Student.objects.all()
        paginator = Paginator(studentList, 15)
        page = request.GET.get('page')

        try:
            students = paginator.page(page)
        except PageNotAnInteger:
            students = paginator.page(1)
        except EmptyPage:
            students = paginator.page(paginator.num_pages)

        context = {'students': students}

        return render(request,'students.html', context)

def teachers(request):

        if request.method == 'POST':
            fullName = request.POST['fullName']
            mailAdress = request.POST['mailAdress']

            teacherList = Teacher.objects.filter(fullName__contains=fullName,\
                                                 mailAddress__contains=mailAdress)
            paginator = Paginator(teacherList, 15)
            page = request.GET.get('page')

            try:
                teachers = paginator.page(page)
            except PageNotAnInteger:
                teachers = paginator.page(1)
            except EmptyPage:
                teachers = paginator.page(paginator.num_pages)


            context = {'teachers': teachers}

            return render(request,'teachers.html', context)

        else:

            teacherList = Teacher.objects.all()
            paginator = Paginator(teacherList, 15)
            page = request.GET.get('page')

            try:
                teachers = paginator.page(page)
            except PageNotAnInteger:
                teachers = paginator.page(1)
            except EmptyPage:
                teachers = paginator.page(paginator.num_pages)


            context = {'teachers': teachers}

            return render(request,'teachers.html', context)
def teacherDetails(request, pk):

    teacher = get_object_or_404(Teacher, pk=pk)
    context = {'teacher': teacher}

    return render(request,'teacherDetails.html', context)

def courses(request):

    if request.method == 'POST':

        code = request.POST['code']
        name = request.POST['name']
        teacher = request.POST['teacher']


        courseList = Course.objects.filter(name__contains=name,\
                                           teacher__slugName__contains=teacher,\
                                           code__contains=code)
        paginator = Paginator(courseList, 15)
        page = request.GET.get('page')

        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)


        context = {'courses': courses}

        return render(request,'courses.html', context)

    else:

        courseList = Course.objects.all()
        paginator = Paginator(courseList, 15)
        page = request.GET.get('page')

        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)


        context = {'courses': courses}

        return render(request,'courses.html', context)
def courseDetails(request, pk):

    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}

    return render(request,'courseDetails.html', context)

def attendances(request):

    if request.method == 'POST':
        date = request.POST['date']
        course = request.POST['course']

        attendanceList = CreateAttendance.objects.filter(date__contains=date, course__name__contains=course)
        paginator = Paginator(attendanceList, 15)
        page = request.GET.get('page')

        try:
            attendances = paginator.page(page)
        except PageNotAnInteger:
            attendances = paginator.page(1)
        except EmptyPage:
            attendances = paginator.page(paginator.num_pages)


        context = {'attendances': attendances}

        return render(request,'attendances.html', context)


    else:

        attendanceList = CreateAttendance.objects.all()
        paginator = Paginator(attendanceList, 15)
        page = request.GET.get('page')

        try:
            attendances = paginator.page(page)
        except PageNotAnInteger:
            attendances = paginator.page(1)
        except EmptyPage:
            attendances = paginator.page(paginator.num_pages)


        context = {'attendances': attendances}

        return render(request,'attendances.html', context)
def attendanceDetails(request, pk):

    createAttendance = get_object_or_404(CreateAttendance, pk=pk)
    attendance = Attendance.objects.filter(course=createAttendance.course, date=createAttendance.date)
    attendanceList = attendance
    paginator = Paginator(attendanceList, 15)
    page = request.GET.get('page')

    try:
        attendances = paginator.page(page)
    except PageNotAnInteger:
        attendances = paginator.page(1)
    except EmptyPage:
        attendances = paginator.page(paginator.num_pages)

    context = {'createAttendance': createAttendance, 'attendances': attendances}

    return render(request,'attendanceDetails.html', context)

def createAttendance(request):
    if request.method == 'POST':
        form = CreateAttendanceForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            date = request.POST.get('date', None)
            coursePK = request.POST.get('course', None)
            course = get_object_or_404(Course, pk=int(coursePK))

            # Error Handling
            try:
                oldAttendance = CreateAttendance.objects.get(date=date, course=course)
                strOldDate = str(oldAttendance.date).split("-")
                oldDate = strOldDate[0]+strOldDate[1]+strOldDate[2]
                strNewDate = str(date).split("-")
                newDate = strNewDate[0]+strNewDate[1]+strNewDate[2]

                if oldDate == newDate and oldAttendance.course == course:
                    return HttpResponseRedirect('/attendanceTaken')
            except Exception as e:

                if str(e.__class__).split("'")[1] == 'baseApp.models.MultipleObjectsReturned':
                    return HttpResponseRedirect('/attendanceTaken')
            # End of Erorr Handling

            for student in course.students.all():
                attendance = Attendance(student=student, course=course, date=date)
                attendance.save()
            instance.save()
            return HttpResponseRedirect('/attendance/' + str(instance.pk))
    else:
        form = CreateAttendanceForm()

    return render(request, 'kayit.html', {'form': form, 'title': 'Yoklama'})

def attendance(request, pk):
    createAttendance = get_object_or_404(CreateAttendance, pk=pk)
    studentList = createAttendance.course.students.all()
    paginator = Paginator(studentList, 15)
    page = request.GET.get('page')

    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        students = paginator.page(1)
    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    context = {'students': students, 'createAttendance': createAttendance}

    return render(request,'attendance.html', context)

def markAttendance(request, capk, spk):
    student = get_object_or_404(Student, pk=spk)
    createAttendance = get_object_or_404(CreateAttendance, pk=capk)
    try:
        attendance = Attendance.objects.get(student=student, course=createAttendance.course, date=createAttendance.date)
    except:
        return HttpResponseRedirect('/attendanceTaken/')
    if attendance.isHere == False:
        attendance.isHere = True
    else:
        attendance.isHere = False
    attendance.save()
    return HttpResponse(status=204)

def studentAttendance(request, pk):

    student = get_object_or_404(Student, pk=pk)
    attendances =  Attendance.objects.filter(student=student)
    heres = Attendance.objects.filter(student=student, isHere=True)
    absences = Attendance.objects.filter(student=student, isHere=False)
    context = {'student': student, 'attendances': attendances,\
               'heresC': len(heres), 'absencesC': len(absences), 'attendancesC': len(attendances)}

    return render(request,'studentAttendance.html', context)

def attendanceTaken(request):

    text = "Yoklama Önceden Alındı!"
    context = {'text': text}

    return render(request,'404.html', context)


# Student Edit Page
def studentDetailsEdit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.POST:
        form = OgrenciKayit(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/studentDetails/%s'%pk)
    else:
        form = OgrenciKayit(instance=student)

    return render(request, 'kayit.html',{ 'form':form, 'title':'Öğrenci'})

# Teacher Edit Page
def teacherDetailsEdit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.POST:
        form = OgretmenKayit(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teacherDetails/%s'%pk)
    else:
        form = OgretmenKayit(instance=teacher)

    return render(request, 'kayit.html',{ 'form':form, 'title':'Öğretmen'})

# Course Edit Page
def courseDetailsEdit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.POST:
        form = DersKayit(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/courseDetails/%s'%pk)
    else:
        form = DersKayit(instance=course)

    return render(request, 'kayit.html',{ 'form':form, 'title':'Ders'})


# Ogrenci Kaydi
def ogrencikaydi(request):
    if request.method == 'POST':
        form = OgrenciKayit(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profilePhoto = request.FILES.get('profilePhoto', None)
            instance.save()
            registered = True
            return HttpResponseRedirect('/')

    else:
        form = OgrenciKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Öğrenci'})

# Ogretmen Kaydi
def ogretmenkaydi(request):
    if request.method == 'POST':
        form = OgretmenKayit(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profilePhoto = request.FILES.get('profilePhoto', None)
            instance.save()
            registered = True
            return HttpResponseRedirect('/')

    else:
        form = OgretmenKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Öğretmen'})


# Ders Kaydi
def derskaydi(request):
    if request.method == 'POST':
        form = DersKayit(request.POST)
        if form.is_valid():
            instance = form.save()
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

# Gelir Kaydi
def gelirkaydi(request):
    if request.method == 'POST':
        form = GelirKayit(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')

    else:
        form = GelirKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Gelir'})

# Gider Kaydi
def giderkaydi(request):
    if request.method == 'POST':
        form = GiderKayit(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')

    else:
        form = GiderKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Gider'})

# Kitap Odemesi Kaydi
def kitapodemesikaydi(request):
    if request.method == 'POST':
        form = KitapOdemesiKayit(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/')

    else:
        form = KitapOdemesiKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Kitap Ödemesi'})
