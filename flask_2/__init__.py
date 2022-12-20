from flask import Flask, render_template, request, redirect
import speech_recognition as sr
#import pyttsx3
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
	text = ""
	transcript = ""
	if request.method =="POST":
		r = sr.Recognizer()
		#text = ""
		#while (text!="terminate"):
		with sr.Microphone() as source:
			#clear background noise
			r.adjust_for_ambient_noise(source, duration=0.3)

			print("Speak now.")
				#capture the audio
			audio = r.listen(source)

			try:
				text = r.recognize_google(audio)
				print("Speaker:",text)
			except:
				print("Please Say again!!")
			# return render_template('index.html', transcript = text)
	return render_template('index.html', transcript = text)

if __name__ == "__main__":
	app.run(debug=True, threaded=True)