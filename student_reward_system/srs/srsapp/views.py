from django.shortcuts import render,redirect
from .forms import studentForm
from .forms import instructorForm
from .forms import courseForm
from .models import student
from .models import instructor
from .models import course
from .models import performance
from  django.db import connection


# Create your views here.
def showhomepage(request):
    return render(request,"srsapp/homepage.html")

def showadmin(request):
    return render(request,"srsapp/admin.html")

def student_list(request):
    context = {'student_list':student.objects.all()}
    return render(request,"srsapp/student_list.html",context)

def instructor_list(request):
    context = {'instructor_list':instructor.objects.all()}
    return render(request,"srsapp/instructor_list.html",context)

def student_form(request,student_ID=0):
    if request.method == "GET":
        if student_ID==0:
            form = studentForm()
        else:
            students=student.objects.get(pk=student_ID)
            form = studentForm(instance=students)
        return render(request,"srsapp/student_form.html",{'form':form})
    else:
        if student_ID==0:
            form = studentForm(request.POST)
        else:
            students=student.objects.get(pk=student_ID)
            form = studentForm(request.POST,instance=students)
        if form.is_valid():
            form.save()
        return redirect('/list')

def instructor_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = instructorForm()
        else:
            instructors=instructor.objects.get(pk=id)
            form = instructorForm(instance=instructors)
        return render(request,"srsapp/instructor_form.html",{'form':form})
    else:
        if id==0:
            form = instructorForm(request.POST)
        else:
            instructors=instructor.objects.get(pk=id)
            form = instructorForm(request.POST,instance=instructors)
        if form.is_valid():
            form.save()
        return redirect('/adminview/instructor/list')

def student_delete(request,id):
    students=student.objects.get(pk=id)
    students.delete()
    return redirect('/list')

def student_sort(request,var):
    students=student.objects.order_by(var)
    context={ 'student_list' : students}
    return render(request,"srsapp/student_list.html",context)

def instructor_delete(request,id):
    instructors=instructor.objects.get(pk=id)
    instructors.delete()
    return redirect('/adminview/instructor/list')

def instructor_sort(request,var):
    instructors=instructor.objects.order_by(var)
    context={ 'instructor_list' : instructors}
    return render(request,"srsapp/instructor_list.html",context)

def course_list(request):
    context = {'course_list':course.objects.all()}
    return render(request,"srsapp/course_list.html",context)

def course_delete(request,id):
    courses=course.objects.get(pk=id)
    courses.delete()
    return redirect('/adminview/course/list')

def course_sort(request,var):
    courses=course.objects.order_by(var)
    context={ 'course_list' : courses}
    return render(request,"srsapp/course_list.html",context)

def course_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = courseForm()
        else:
            courses=course.objects.get(pk=id)
            form = courseForm(instance=courses)
        return render(request,"srsapp/course_form.html",{'form':form})
    else:
        if id==0:
            form = courseForm(request.POST)
        else:
            courses=course.objects.get(pk=id)
            form = courseForm(request.POST,instance=courses)
        if form.is_valid():
            form.save()
        return redirect('/adminview/course/list')

def performanceall(request):
    context = {'performance_all':performance.objects.all()}
    return render(request,"srsapp/performanceall.html",context)

def performance_sort(request,var):
    performances=performance.objects.order_by(var)
    context={ 'performance_all' : performances}
    return render(request,"srsapp/performanceall.html",context)

def studentviewquery(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        raw_query1 = "select * from srsapp_student where \"student_ID\" = %s ;"
        cursor = connection.cursor()
        cursor.execute(raw_query1,(search_id,))
        alldata1=cursor.fetchall()

        raw_query2 = "select * from srsapp_performance where \"student_ID_id\"=%s ;"
        cursor = connection.cursor()
        cursor.execute(raw_query2,(search_id,))
        alldata2=cursor.fetchall()

        raw_query3 = "select * from academic_score_final natural join non_academic_score_final where academic_score_final.\"student_ID\" = %s;"
        cursor = connection.cursor()
        cursor.execute(raw_query3,(search_id,))
        alldata3=cursor.fetchall()

        raw_query4 = "select * from srsapp_alert where \"student_ID\" = %s;"
        cursor = connection.cursor()
        cursor.execute(raw_query4,(search_id,))
        alldata4=cursor.fetchall()

        raw_query5 = "SELECT \"course_ID\", sum(reward_points)from srsapp_academic_reward	where \"student_ID\"=%s	group by \"course_ID\";"
        cursor = connection.cursor()
        cursor.execute(raw_query5,(search_id,))
        alldata5=cursor.fetchall()

        raw_query6 = "select * from srsapp_non_academic_reward where \"student_ID\"=%s"
        cursor = connection.cursor()
        cursor.execute(raw_query6,(search_id,))
        alldata6=cursor.fetchall()

        return render(request,'srsapp/student_view.html',{'data':alldata1,'data2':alldata2,'data3':alldata3,'data4':alldata4,'data5':alldata5,'data6':alldata6})
        
    else:
        return render(request, 'srsapp/studentviewip.html')

def sendalert(request):
    if request.method == 'POST':
        s_id = request.POST.get('id', None)
        c_id= request.POST.get('c_id', None)
        type_1 = request.POST.get('type', None)
        msg = request.POST.get('msg', None)

        raw_query1 = "INSERT INTO public.srsapp_alert(\"student_ID\", \"course_ID\", date, alert_type, alert_message) VALUES (%s, %s,CURRENT_TIMESTAMP, %s,%s);"
        cursor = connection.cursor()
        cursor.execute(raw_query1,(s_id,c_id,type_1,msg))
       
        return redirect('show_instructorview')
        
    else:
        return render(request, 'srsapp/alert_input.html')

def instructorviewquery(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)
        raw_query1 = "select * from srsapp_course natural join srsapp_academic_reward where srsapp_course.\"instructor_ID_id\" = %s ;"
        cursor = connection.cursor()
        cursor.execute(raw_query1,(search_id,))
        alldata1=cursor.fetchall()

        raw_query2 = "select *from public.srsapp_instructor where \"instructor_ID\" = %s ;"
        cursor = connection.cursor()
        cursor.execute(raw_query2,(search_id,))
        alldata2=cursor.fetchall()

        
        
        return render(request,'srsapp/instructorview.html',{'data':alldata1,'data2':alldata2})
        
    else:
        return render(request, 'srsapp/instructor_ip.html')


def updatemarks(request):
    if request.method == 'POST':
        s_id = request.POST.get('id', None)
        c_id= request.POST.get('c_id', None)
        type_1 = request.POST.get('type', None)
        mark = request.POST.get('marks', None)

        raw_query1 = "UPDATE public.srsapp_academic_reward SET  obtained_marks= %s WHERE \"student_ID\"=%s and \"course_ID\"=%s and activity_name=%s;"
        cursor = connection.cursor()
        cursor.execute(raw_query1,(mark,s_id,c_id,type_1))
        return redirect('show_instructorview')
        
    else:
        return render(request, 'srsapp/acad_input.html')

