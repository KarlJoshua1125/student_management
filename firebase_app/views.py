from django.shortcuts import render, redirect
from django.apps import apps
from django.http import JsonResponse
import firebase_admin
from firebase_admin import credentials, db
from .forms import StudentForm
from datetime import date


def connectDB():
    if not firebase_admin._apps:
        cred = credentials.Certificate("studentmanagement-admin-key.json")
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://studentmanagement-84271-default-rtdb.firebaseio.com/"  # Your database URL
        })
    dbconn = db.reference("StudentsList")
    return dbconn


def index(request):
    students = []
    dbconn = connectDB()
    tblStudents = dbconn.get()
    print(tblStudents)
    for key, value in tblStudents.items():
        students.append({"id": int(value["ID"]), "fname": value["FirstName"], "lname": value["LastName"],
                         "year": int(value["Year"]), "course": value["Course"], "key": key})
    return render(request, 'index.html', {'students': students})


def attendance(request):
    dbconn = connectDB()
    students = dbconn.get()  # Fetch all students from Firebase

    student_list = []
    for student_key in students.keys():
        student = students[student_key]
        student_list.append({
            'name': f"{student['FirstName']} {student['LastName']}",
            'IDname': f"{student['FirstName']}{student['LastName']}"
        })

    context = {
        'current_date': date.today().strftime("%Y-%m-%d"),
        'students': student_list
    }
    return render(request, 'attendance.html', context)



def deletestudent(request, id):
    dbconn = connectDB()
    tblStudents = dbconn.get()
    for key, value in tblStudents.items():
        if (value["ID"] == id):
            deletekey = key
            break
    delitem = dbconn.child(deletekey)
    delitem.delete()
    return redirect('index')


def update_student(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == 'POST':
        id = int(request.POST.get('id'))
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        year = int(request.POST.get('year'))
        course = request.POST.get('course')
        key = request.POST.get('key')

        dbconn = connectDB()
        dbconn.child(key).update({"ID": id, "FirstName": fname, "LastName": lname, "Year": year, "Course": course})

        return JsonResponse({'status': 'success'})
    else:

        return JsonResponse({'status': 'errors', 'errors': 'Unable to update student.'})


def search_students(request):
    query = request.GET.get('query', '')
    students = students.objects.filter(lname__icontains=query)
    return render(request, 'index.html', {'students': students})
