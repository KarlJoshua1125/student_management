import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("studentmanagement-admin-key.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://studentmanagement-84271-default-rtdb.firebaseio.com/" #Your database URL
})

dbref = db.reference("StudentsList")
dbref.push( { "ID": 1, "Name": "Karl", "Year": 4, "Course": 'BSIT' } )
dbref.push( { "ID": 2, "Name": "Jomari", "Year": 3, "Course": 'BSIT' } )
dbref.push( { "ID": 3, "Name": "Cheska", "Year": 3, "Course": 'BSIT' } )
dbref.push( { "ID": 4, "Name": "Anthony", "Year": 3, "Course": 'BSIT' } )


print(dbref.get())

{'-NTXSZqAac846THZbkQw': {'Course': 'BSIT', 'ID': 1, 'Name': 'Karl', 'Year': 4}, '-NTXSZu7WdWEzXg6uzrC': {'Course': 'BSIT', 'ID': 2, 'Name': 'Jomari', 'Year': 3}, '-NTXSZxcgmnaj-VLD5Vc': {'Course': 'BSIT', 'ID': 3, 'Name': 'Cheska', 'Year': 3}, '-NTXS_07HJjfdt-qamyw': {'Course': 'BSIT', 'ID': 4, 'Name': 'Anthony', 'Year': 3}}