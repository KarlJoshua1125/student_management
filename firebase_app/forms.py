from django import forms

class StudentForm(forms.Form):
    id= forms.IntegerField()
    name= forms.CharField(max_length=100)
    year= forms.IntegerField()
    course= forms.CharField(max_length=100)