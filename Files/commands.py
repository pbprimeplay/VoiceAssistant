import webbrowser, wikipedia, datetime, subprocess, wolframalpha

client = wolframalpha.Client('Your API-Client ID')

def api_search(response):
	res = client.query(response)
	return next(res.results).text

def open_site(site_name):
	webbrowser.open(site_name)

def wiki(query):
	try: return wikipedia.summary(query, sentences=3)
	except: return False

def make_note(note):
    date = datetime.datetime.now()
    filename = str(date).replace(':', "_") + '.txt'
    newfile = open(filename, "w")
    newfile.write(note)

    subprocess.Popen(["notepad.exe", filename])

def greeting():
	currentHour = int(datetime.datetime.now().hour)
	if currentHour >= 0 and currentHour < 12:
		return 'Good morning'

	if currentHour >= 12 and currentHour < 16:
		return 'Good afternoon'

	if currentHour >= 16 and currentHour != 0:
		return 'Good evening'

def get_date():
	today = datetime.date.today()
	return today.strftime("%A, %B %d, %Y")

def open_app(appname):
	if 'google chrome' in appname.lower():
		subprocess.call(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
		return True

	elif 'powerpoint' in appname.lower():
		subprocess.call(r'C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE')
		return True

	elif 'excel' in appname.lower():
		subprocess.call(r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE')
		return True

	elif 'word' in appname.lower():
		subprocess.call(r'C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE')
		return True

	elif 'notepad' in appname.lower():
		subprocess.Popen(r'notepad.exe')
		return True

	elif 'file explorer' in appname.lower():
		subprocess.Popen(r'explorer')
		return True

	elif 'spotify' in appname.lower():
		subprocess.call(r'C:\Users\USER\AppData\Roaming\Spotify\Spotify.exe')
		return True

	return False
