from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.showhomepage,name='homepage'),
    path('performance/',views.performanceall,name='performance_all'),
    path('performance/<str:var>/',views.performance_sort,name='performance_sort'),
    path('adminview/',views.showadmin,name='admin_view'),
    path('adminview/instructor/',views.instructor_form,name='instructor_insert'),
    path('adminview/instructor/<int:id>/',views.instructor_form,name='instructor_update'),
    path('adminview/instructor/delete/<int:id>',views.instructor_delete,name='instructor_delete'),
    path('adminview/instructor/list/<str:var>/',views.instructor_sort,name='instructor_sort'),
    path('adminview/instructor/list/',views.instructor_list,name='instructor_list'),
    path('adminview/course/',views.course_form,name='course_insert'),
    path('adminview/course/<int:id>/',views.course_form,name='course_update'),
    path('adminview/course/delete/<int:id>',views.course_delete,name='course_delete'),
    path('adminview/course/list/<str:var>/',views.course_sort,name='course_sort'),
    path('adminview/course/list/',views.course_list,name='course_list'),
    path('student/',views.student_form,name='student_insert'),
    path('<int:student_ID>/',views.student_form,name='student_update'),
    path('list/',views.student_list,name='student_list'),
    path('delete/<int:id>',views.student_delete,name='student_delete'),
    path('<str:var>/',views.student_sort,name='student_sort'),
    path('q/studentview/',views.studentviewquery,name='show_studentview'),
    path('q/instructorview/alert',views.sendalert,name='send_alert'),
    path('q/instructorview/',views.instructorviewquery,name='show_instructorview'),
    path('q/instructorview/update',views.updatemarks,name='update_marks'),

]