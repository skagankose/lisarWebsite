from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.defaulttags import register
from django.utils import timezone
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *

# Homepage
@login_required
def home(request):

    currentDate = CurrentDate.objects.all()[0]
    currentYear = str(currentDate.date).split("-")[0]
    newDate = timezone.now()
    newYear = str(newDate).split("-")[0]
    if currentYear != newYear:
        currentDate.delete()
        newCurrentDate = CurrentDate(date=timezone.now())
        newCurrentDate.save()
        allStudents = Student.objects.all()
        for aStudent in allStudents:
            if int(aStudent.schoolLevel) != 13:
                aStudent.schoolLevel = int(aStudent.schoolLevel) + 1
                aStudent.save()
            if int(aStudent.lisarLevel) != 3:
                aStudent.lisarLevel = int(aStudent.lisarLevel) + 1
                aStudent.save()

    context = {}
    return render(request, 'home.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# TMP AboutUs
def aboutUs(request):
    return HttpResponseRedirect('/')

@login_required
def emailAndHome(request, pk):

    course = get_object_or_404(CreateAttendance, pk=pk).course
    studentsToSent = list()
    for student in course.classroom.students.all():
        attendances =  Attendance.objects.filter(student=student)
        heres = Attendance.objects.filter(student=student, isHere=True)
        absences = Attendance.objects.filter(student=student, isHere=False)
        cancelleds = Attendance.objects.filter(student=student, isCancelled=True)
        percentage =  int(float(len(absences)-len(cancelleds))/float(len(attendances)) * 100.0)
        if percentage >= 25.0:

            studentsToSent += [str(student.firstName) + " " + str(student.lastName) + "\t%" + str(percentage)]

            email = EmailMessage(
                'Lisar Akademi Öğrenci Yoklama Bilgisi',
                str(student.firstName) + " " + str(student.lastName) + " %" + str(percentage) +" oranında devamsızlık yapmıştır.",
                'Lisar Akademi Bilgilendirme',
                [str(student.parentMailAddress)],
                headers = {'Reply-To': 'akademiLisar@gmail.com' }
            )
            email.send()

    if len(studentsToSent) > 1:

        message = "Öğrenci İsmi\tDevamsızlık Yüzdesi\n"
        for s in studentsToSent:
            message += s + "\n"
        email = EmailMessage(
            'Lisar Akademi Öğrenci Yoklama Bilgisi',
            message,
            'Lisar Akademi Bilgilendirme',
            ['akademiLisar@gmail.com'],
            headers = {'Reply-To': 'akademiLisar@gmail.com' }
        )
        email.send()

    return HttpResponseRedirect('/')

@login_required
def studentDetails(request, pk):

    student = get_object_or_404(Student, pk=pk)
    context = {'student': student}

    return render(request,'studentDetails.html', context)
@login_required
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

@login_required
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

@login_required
def classrooms(request):

    if request.method == 'POST':
        code = request.POST['code']
        location = request.POST['location']

        classroomList = Student.objects.filter(code__contains=code,\
                                             location__contains=location)
        paginator = Paginator(classroomList, 15)
        page = request.GET.get('page')

        try:
            classrooms = paginator.page(page)
        except PageNotAnInteger:
            classrooms = paginator.page(1)
        except EmptyPage:
            classrooms = paginator.page(paginator.num_pages)


        context = {'classrooms': classrooms}

        return render(request,'classrooms.html', context)

    else:

        classroomList = Classroom.objects.all()
        paginator = Paginator(classroomList, 15)
        page = request.GET.get('page')

        try:
            classrooms = paginator.page(page)
        except PageNotAnInteger:
            classrooms = paginator.page(1)
        except EmptyPage:
            classrooms = paginator.page(paginator.num_pages)

        context = {'classrooms': classrooms}

        return render(request,'classrooms.html', context)

@login_required
def classroomDetails(request, pk):

    classroom = get_object_or_404(Classroom, pk=pk)
    students = classroom.students.all()
    context = {'classroom': classroom, 'students':students}


    return render(request,'classroomDetails.html', context)

# Student Edit Page
@login_required
def classroomDetailsEdit(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    if request.POST:
        form = SinifKayit(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/classroomDetails/%s'%pk)
    else:
        form = SinifKayit(instance=classroom)

    return render(request, 'kayit.html',{ 'form':form, 'title':'Sınıf'})

@login_required
def teacherDetails(request, pk):

    teacher = get_object_or_404(Teacher, pk=pk)
    context = {'teacher': teacher}

    return render(request,'teacherDetails.html', context)

@login_required
def courses(request):

    if request.method == 'POST':

        code = request.POST['code']
        name = request.POST['name']
        teacher = request.POST['teacher']


        courseList = Course.objects.filter(name__contains=name,\
                                           teacher__fullName__contains=teacher,\
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
@login_required
def courseDetails(request, pk):

    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}

    return render(request,'courseDetails.html', context)

@login_required
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
@login_required
def attendanceDetails(request, pk):

    createAttendance = get_object_or_404(CreateAttendance, pk=pk)
    attendance = Attendance.objects.filter(course=createAttendance.course, date=createAttendance.date)
    if attendance[0].isCancelled == True:
        statusText = "Ders İptal Edildi."
    else:
        statusText = "Yoklama Sorunsuz Alındı."
    attendanceList = attendance
    paginator = Paginator(attendanceList, 15)
    page = request.GET.get('page')

    try:
        attendances = paginator.page(page)
    except PageNotAnInteger:
        attendances = paginator.page(1)
    except EmptyPage:
        attendances = paginator.page(paginator.num_pages)

    context = {'createAttendance': createAttendance, 'attendances': attendances, 'statusText': statusText}

    return render(request,'attendanceDetails.html', context)
@login_required
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

            for student in course.classroom.students.all():
                attendance = Attendance(student=student, course=course, date=date)
                attendance.save()
            instance.save()
            return HttpResponseRedirect('/attendance/' + str(instance.pk))
    else:
        form = CreateAttendanceForm()

    return render(request, 'kayit.html', {'form': form, 'title': 'Yoklama'})
@login_required
def attendance(request, pk):
    createAttendance = get_object_or_404(CreateAttendance, pk=pk)
    studentList = createAttendance.course.classroom.students.all()
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
@login_required
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
@login_required
def cancelAttendance(request, pk):
    createAttendance = get_object_or_404(CreateAttendance, pk=pk)
    attendances = Attendance.objects.filter(course=createAttendance.course, date=createAttendance.date)
    for attendance in attendances:
        attendance.isCancelled = True
        attendance.save()
    return HttpResponseRedirect('/')
@login_required
def studentAttendance(request, pk):
    student = get_object_or_404(Student, pk=pk)
    attendances =  Attendance.objects.filter(student=student)
    heres = Attendance.objects.filter(student=student, isHere=True)
    absences = Attendance.objects.filter(student=student, isHere=False)
    cancelleds = Attendance.objects.filter(student=student, isCancelled=True)
    context = {'student': student, 'attendances': attendances,\
               'heresC': len(heres), 'absencesC': len(absences)-len(cancelleds), 'attendancesC': len(attendances),
               'cancelledsC': len(cancelleds)}

    return render(request,'studentAttendance.html', context)
@login_required
def attendanceTaken(request):

    text = "Bu dersin yoklamasi bu tarih için önceden alındı."
    context = {'text': text}

    return render(request,'404.html', context)


# Student Edit Page
@login_required
def studentDetailsEdit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.POST:
        form = OgrenciKayit(request.POST, instance=student)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profilePhoto = request.FILES.get('profilePhoto', None)
            instance.save()
            form.save()
            return HttpResponseRedirect('/studentDetails/%s'%pk)
    else:
        form = OgrenciKayit(instance=student)

    return render(request, 'kayit.html',{ 'form':form, 'title':'Öğrenci'})

# Teacher Edit Page
@login_required
def teacherDetailsEdit(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.POST:
        form = OgretmenKayit(request.POST, instance=teacher)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profilePhoto = request.FILES.get('profilePhoto', None)
            instance.save()
            form.save()
            return HttpResponseRedirect('/teacherDetails/%s'%pk)
    else:
        form = OgretmenKayit(instance=teacher)

    return render(request, 'kayit.html',{ 'form':form, 'title':'Öğretmen'})

# Course Edit Page
@login_required
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
@login_required
def ogrencikaydi(request):
    if request.method == 'POST':
        form = OgrenciKayit(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profilePhoto = request.FILES.get('profilePhoto', None)
            instance.save()
            registered = True
            pk = int(instance.pk)
            return HttpResponseRedirect('/studentDetails/'+str(pk))

    else:
        form = OgrenciKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Öğrenci'})

# Ogretmen Kaydi
@login_required
def ogretmenkaydi(request):
    if request.method == 'POST':
        form = OgretmenKayit(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profilePhoto = request.FILES.get('profilePhoto', None)
            instance.save()
            form.save()
            registered = True
            pk = int(instance.pk)
            return HttpResponseRedirect('/teacherDetails/'+str(pk))

    else:
        form = OgretmenKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Öğretmen'})


# Ders Kaydi
@login_required
def derskaydi(request):
    if request.method == 'POST':
        form = DersKayit(request.POST)
        if form.is_valid():
            instance = form.save()
            pk = int(instance.pk)
            return HttpResponseRedirect('/courseDetails/'+str(pk))

    else:
        form = DersKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Ders'})




# Sınıf Kaydi
@login_required
def sinifkaydi(request):
    if request.method == 'POST':
        form = SinifKayit(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            form.save()
            pk = int(instance.pk)
            return HttpResponseRedirect('/classroomDetails/'+str(pk))

    else:
        form = SinifKayit()

    return render(request, 'kayit.html', {'form': form, 'title': 'Sınıf'})

# Gelir Kaydi
@login_required
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
@login_required
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
@login_required
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

# Öğrenci Okul Kaydi
@login_required
def lisekaydi(request):
    if request.method == 'POST':
        form = AddHighSchool(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('/')

    else:
        form = AddHighSchool()

    return render(request, 'kayit.html', {'form': form, 'title': 'Lise'})

# Öğretmen Okul Kaydi
@login_required
def unikaydi(request):
    if request.method == 'POST':
        form = AddUniversity(request.POST)
        if form.is_valid():
            instance = form.save()
            return HttpResponseRedirect('/')

    else:
        form = AddUniversity()

    return render(request, 'kayit.html', {'form': form, 'title': 'Üniversite'})


"""
# BookPayment

@login_required
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
@login_required
def attendanceDetails(request, pk):

    createAttendance = get_object_or_404(CreateAttendance, pk=pk)
    attendance = Attendance.objects.filter(course=createAttendance.course, date=createAttendance.date)
    if attendance[0].isCancelled == True:
        statusText = "Ders İptal Edildi."
    else:
        statusText = "Yoklama Sorunsuz Alındı."
    attendanceList = attendance
    paginator = Paginator(attendanceList, 15)
    page = request.GET.get('page')

    try:
        attendances = paginator.page(page)
    except PageNotAnInteger:
        attendances = paginator.page(1)
    except EmptyPage:
        attendances = paginator.page(paginator.num_pages)

    context = {'createAttendance': createAttendance, 'attendances': attendances, 'statusText': statusText}

    return render(request,'attendanceDetails.html', context)
@login_required
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

            for student in course.classroom.students.all():
                attendance = Attendance(student=student, course=course, date=date)
                attendance.save()
            instance.save()
            return HttpResponseRedirect('/attendance/' + str(instance.pk))
    else:
        form = CreateAttendanceForm()

    return render(request, 'kayit.html', {'form': form, 'title': 'Yoklama'})
@login_required
def attendance(request, pk):
    createAttendance = get_object_or_404(CreateAttendance, pk=pk)
    studentList = createAttendance.course.classroom.students.all()
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
@login_required
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
@login_required
def cancelAttendance(request, pk):
    createAttendance = get_object_or_404(CreateAttendance, pk=pk)
    attendances = Attendance.objects.filter(course=createAttendance.course, date=createAttendance.date)
    for attendance in attendances:
        attendance.isCancelled = True
        attendance.save()
    return HttpResponseRedirect('/')
@login_required
def studentAttendance(request, pk):
    student = get_object_or_404(Student, pk=pk)
    attendances =  Attendance.objects.filter(student=student)
    heres = Attendance.objects.filter(student=student, isHere=True)
    absences = Attendance.objects.filter(student=student, isHere=False)
    cancelleds = Attendance.objects.filter(student=student, isCancelled=True)
    context = {'student': student, 'attendances': attendances,\
               'heresC': len(heres), 'absencesC': len(absences)-len(cancelleds), 'attendancesC': len(attendances),
               'cancelledsC': len(cancelleds)}

@login_required
def attendanceTaken(request):

    text = "Bu dersin yoklamasi bu tarih için önceden alındı."
    context = {'text': text}

    return render(request,'404.html', context)
"""
