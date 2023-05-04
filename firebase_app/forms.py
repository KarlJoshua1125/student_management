from django import forms

class StudentForm(forms.Form):
    id= forms.IntegerField()
    fname= forms.CharField(max_length=100)
    lname= forms.CharField(max_length=100)
    year= forms.IntegerField()
    course= forms.CharField(max_length=100)