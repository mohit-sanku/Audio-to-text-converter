from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	transcript = ""
	if request.method =="POST":

		if "file" not in request.files:
			print("FORM DATA RECIEVED")
			return redirect(request.url)

		file = request.files["file"]
		if file.filename == "":
			print("FORM DATA NOT RECIEVED")
			return redirect(request.url)
			
		if file:
			print("FORM DATA RECIEVED")
			recognizer = sr.Recognizer()	#Initialize instance of speech recognition
			audioFile = sr.AudioFile(file)	#Analog signals to digital signals converion(understandable format)
			with audioFile as source:
				data = recognizer.record(source)	#reading through the recognizer understandable to speech recognition module
			transcript = recognizer.recognize_google(data, key=None)	#data conversion into text format
			#print(text)

	return render_template('index.html', transcript = transcript)

if __name__ == "__main__":
	app.run(debug=True, threaded=True)