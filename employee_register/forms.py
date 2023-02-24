from django import forms
from .models import Employee
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields ='__all__'
        labels = {
            "fullname":'Full Name',
            "phone":'Phone Number'
        }

    def __init__(self,*args, **kwagrs):
        super(EmployeeForm,self).__init__(*args, **kwagrs)
        self.fields['position'].empty_label = "Select"
        self.fields['salary'].required = False