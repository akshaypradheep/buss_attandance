import pyrebase
import serial
import datetime
now = datetime.datetime.now()
#Firebase Configuration
config = {
  "apiKey":"AIzaSyBeTkzdsVpcKpZkU9BMzNwCloUlNf2MWAo",
  "authDomain": "akshaypradheepdc.firebaseapp.com",
  "databaseURL": "https://akshaypradheepdc.firebaseio.com",
  "storageBucket": "akshaypradheepdc.appspot.com"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()
rf = serial.Serial('/dev/ttyUSB0')

def inRead():
	_a = rf.read(12)
	_b = _a.decode('utf-8')
	#a = input("enter the user ID:")
	return _b

def timeStamp():
	import datetime
	now = datetime.datetime.now()
	a = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
	return a 
	pass

def Check():
	print("WAITING FOR RF ID")
	a = inRead()
	_reg = db.child("NEXUS").child("userList").child(a).get()
	reg = _reg.val()
	d = timeStamp()
	t = now.hour
	if reg == "True":
		if t < 12:
			db.child("NEXUS").child("attandanceList").child(d).child(a).child("am").set(1)
			pass
		if t > 12:
			db.child("NEXUS").child("attandanceList").child(a).child("pm").set(1)
			pass
		pass
	pass

def mark():
	print("WAITING FOR RF ID")
	a = inRead()
	print(a)
	db.child("NEXUS").child("userList").child(a).set("True")

while True:
	Check()
	pass
