import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("studentmanagement-admin-key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://studentmanagement-84271-default-rtdb.firebaseio.com/" #Your database URL
})

dbref = db.reference("StudentsList")
dbref.push( { "ID": 1, "FirstName": "Karl", "LastName": "Gonzales", "Year": 4, "Course": 'BSIT' } )
dbref.push( { "ID": 2, "FirstName": "Cheska", "LastName": "Gubaton", "Year": 4, "Course": 'BSIT' } )
dbref.push( { "ID": 3, "FirstName": "Jomari", "LastName": "Profeta", "Year": 4, "Course": 'BSIT' } )
dbref.push( { "ID": 4, "FirstName": "Anthony", "LastName": "Panalingan", "Year": 4, "Course": 'BSIT' } )



print(dbref.get())
{'-NTlvm9xRj3D_YiMP0k7': {'Course': 'BSIT', 'FirstName': 'Karl', 'ID': 1, 'LastName': 'Gonzales', 'Year': 4}, '-NTlvmDHpdgRWLQtj_Xp': {'Course': 'BSIT', 'FirstName': 'Cheska', 'ID': 2, 'LastName': 'Gubaton', 'Year': 4}, '-NTlvmGi52V96FE_-hQW': {'Course': 'BSIT', 'FirstName': 'Jomari', 'ID': 3, 'LastName': 'Profeta', 'Year': 4}, '-NTlvmK5grP9Rdo9v3Ss': {'Course': 'BSIT', 'FirstName': 'Anthony', 'ID': 4, 'LastName': 'Panalingan', 'Year': 4}}