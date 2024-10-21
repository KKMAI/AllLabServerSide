from django import forms
# from .models import Position
from datetime import date

from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from employee.models import *
from company.models import *

# week 9 #
# class EmployeeForm(forms.Form):
#     GENDER_CHOICES = (("M", "Male"), ("F", "Female"), ("LGBT", "LGBT"))
#     first_name = forms.CharField(max_length=100, required=True)
#     last_name = forms.CharField(max_length=100, required=True)
#     gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
#     birth_date = forms.DateField(initial= date.today(), widget=forms.DateInput({"type":"date"}))
#     hire_date = forms.DateField(initial= date.today(), widget=forms.DateInput(attrs=({"type":"date"})))
#     salary = forms.IntegerField(initial= 0)
#     position = forms.ModelChoiceField(queryset=Position.objects.all())

# week 10 #
class EmployeeForm(ModelForm):
    location = forms.CharField(widget=forms.TextInput(attrs={"cols": 30, "rows": 3}))
    district = forms.CharField(max_length=100)
    province = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=15)
    position = forms.ModelChoiceField(queryset=Position.objects.all())

    class Meta:
        model = Employee
        fields = [
            "first_name", 
            "last_name", 
            "gender", 
            "birth_date", 
            "hire_date", 
            "salary", 
            "position",
            "location",
            "district",
            "province",
            "postal_code"
        ]
        widgets = {
            "birth_date": DateInput(attrs={"class":"input", "type":"date"}),
            "hire_date": DateInput(attrs={"class":"input", "type":"date"}),
        }

    def clean_hire_date(self):
        # cleaned_data = super().clean()
        hire_date = self.cleaned_data.get("hire_date")
        birth_date = self.cleaned_data.get("birth_date")
        print(birth_date)

        print(hire_date)
        if hire_date > date.today():
            raise ValidationError(
                    "hire date cannot be future"
                )
        if birth_date > hire_date:
            raise ValidationError(
                    "birth date cannot be future than hire date"
                )
    
        return hire_date

class ProjectForm(ModelForm):

    staff = ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=CheckboxSelectMultiple()
    )
    class Meta:
        model = Project
        fields = [
            "name",
            "manager",
            "due_date",
            "start_date",
            "description",
            "staff"
        ]

        widgets = {
            "due_date": DateInput(attrs={"type": "date"}),
            "start_date": DateInput(attrs={"type": "date"}),
        }

    # method clean_name = validate for filed name 
    # raise ValidationError คือ Django จับ Error แล้วยัดลง form ให้

    # method clean is validate entire form
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("due_date")

        if start_date and start_date and end_date < start_date:
            raise ValidationError(
                    "due date cannot be before start date"
                )

        return cleaned_data
    
class EditProjectForm(ModelForm):
    staff = ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=CheckboxSelectMultiple
    )
    class Meta:
        model = Project
        fields = [
            "name",
            "manager",
            "due_date",
            "start_date",
            "description",
            "manager",
            "staff"
        ]
