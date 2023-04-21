from django.shortcuts import render, redirect
from django.apps import apps
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from .forms import StudentForm


def connectDB():
    if not firebase_admin._apps:
        cred = credentials.Certificate("studentmanagement-admin-key.json")
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://studentmanagement-84271-default-rtdb.firebaseio.com/" #Your database URL
        })
    dbconn = db.reference("StudentsList")
    return dbconn

def index(request):
    students = []
    dbconn = connectDB()
    tblStudents = dbconn.get()
    for key, value in tblStudents.items():
        students.append({"id": value["ID"], "name": value["Name"], "year": value["Year"], "course": value["Course"]})
    return render(request, 'index.html', {'students':students})

def addstudent(request):
    if request.method == 'GET':
        return render(request, 'addstudent.html')
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get("id")
            name = form.cleaned_data.get("name")
            year = form.cleaned_data.get("year")
            course = form.cleaned_data.get("course")
        dbconn = connectDB()
        dbconn.push( { "ID": id, "Name": name, "Year": year, "Course": course })
        return redirect('index')
    
def updatestudent(request, id):
    st = []
    dbconn = connectDB()
    tblStudents = dbconn.get()

    if request.method == 'GET':
        for key, value in tblStudents.items():
            if(value["ID"] == id):
                global updatekey
                updatekey = key
                st.append({"id": value["ID"], "name": value["Name"], "year": value["Year"], "course": value["Course"]})
        return render(request, 'addstudent.html', {'student':st[0]})
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = str(form.cleaned_data.get("name"))
            year = int(form.cleaned_data.get("year"))
            course = str(form.cleaned_data.get("course"))
            updateitem = dbconn.child(updatekey)
            updateitem.update( { "ID": id, "Name": name, "Year": year, "Course": course } )
        return redirect('index')
    
def deletestudent(request, id):
    dbconn = connectDB()
    tblStudents = dbconn.get()
    for key, value in tblStudents.items():
        if(value["ID"] == id):
            deletekey = key
            break
    delitem = dbconn.child(deletekey)
    delitem.delete()
    return redirect('index')