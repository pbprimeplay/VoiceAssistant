import pyttsx3
import speech_recognition as sr
import time
from commands import *

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[len(voices) - 1].id)
engine.setProperty('rate', 180)

def listen():
	query = ""

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		query = r.recognize_google(audio, language='en-in')
		print('You: ' + query + '\n')

	except sr.UnknownValueError:
		speak('Sorry sir! I did not get that!')

	return query

def speak(audio):
	print('Computer: ' + audio + '\n')
	engine.say(audio)
	engine.runAndWait()

speak(greeting() + ' and welcome back, sir! What would you like to do today?')

while True:
	reply = listen()

	abort_statements = ['bye', 'abort', 'stop', 'end', 'quit', 'nothing']
	hi_statements = ['hi', 'hello', 'hey']

	all_statements = [abort_statements, hi_statements]

	for statements in all_statements:
		for statement in statements:
			if statement in reply:
				if all_statements.index(statements) == 0:
					speak('Bye, sir! Hope you had a nice time with me!')
					quit()

				elif all_statements.index(statements) == 1:
					speak('Hello, sir!')

	if 'start' in reply:
		app = reply.split("start ", 1)[1]
		speak('Starting ' + app + ', sir!')

		succesful = open_app(app)

		if not succesful:
			speak('Sorry, this app could not be opened')

		else:
			time.sleep(3)

	elif 'open' in reply:
		site = reply.split("open ", 1)[1]
		speak('Opening ' + site + ', sir!')

		open_site("https://"+site+".com")

		time.sleep(3)

	elif 'search' in reply:
		site = reply.split("search ", 1)[1]
		speak('Searching for ' + site + ' on Google')
		site = 'https://www.google.com/search?q='+ site + '&oq=' + site + '&aqs=chrome..69i57j46i67i433j46i67j0i67j46i67j0i67j69i61l2.766j0j7&sourceid=chrome&ie=UTF-8'
		open_site(site)

		time.sleep(3)

	elif 'about' in reply:
		query = reply.split("about ", 1)[1]

		try:
			answer = api_search(reply)
			speak(answer)

		except:
			answer = wiki(query)

			if answer != False:
				speak('(From Wikipedia) ' + answer)

			else:
				speak("Sorry, sir, I could not get any information about that")

	elif 'note' in reply:
		speak('What should I note?')
		newQ = listen()

		make_note(newQ)

	else:
		if reply != "":
			try:
				answer = api_search(reply)
				speak(answer)

			except:
				speak('Sorry, sir! I could not find anything relevant to that')
			
	speak("Do you have any other command, sir?")
