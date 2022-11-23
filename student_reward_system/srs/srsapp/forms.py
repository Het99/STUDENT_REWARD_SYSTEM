from django import forms
from .models import student
from srsapp.models import instructor
from srsapp.models import course

class studentForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ('student_ID','student_name','address')
        labels = {
            'student_ID':'Student ID',
            'student_name':'Student Name',
            'address': 'Address'
        }
    
    def __init__(self, *args, **kwargs):
        super(studentForm,self).__init__( *args, **kwargs)
        self.fields['address'].required = False

class instructorForm(forms.ModelForm):
    
    class Meta:
        model = instructor
        fields = [ 'instructor_ID','instructor_name','instructor_address','admin_ID' ]
        labels = {
            'instructor_ID':'Instructor ID',
            'instructor_name':'Instructor Name',
            'instructor_address':'Address',
            'admin_ID':'Admin_ID'
        }
    
    def __init__(self, *args, **kwargs):
        super(instructorForm,self).__init__(*args, **kwargs)
        self.fields['admin_ID'].empty_label = "select"

class courseForm(forms.ModelForm):

    class Meta:
        model = course
        fields = [ 'course_ID','course_name','instructor_ID' ]
        labels = {
            'course_ID':'Course ID',
            'course_name':'Course Name',
            'instructor_ID':'Instructor ID'
        }

    def __init__(self, *args, **kwargs):
        super(courseForm,self).__init__(*args, **kwargs)
        self.fields['instructor_ID'].empty_label = "select"
    