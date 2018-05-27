import random, os

# Settings
# Min 80 / Max 500
speed = 100

# Get language code
chooseLang = False
if chooseLang:
	langs = ""
	for f in os.listdir("Translations"):
		langs += f.replace(".txt", "") + ", "
	langs = langs[:-2]
	lang = ""
	print("Languages: " + langs)
	lang = raw_input("Enter a language code: ")
else:
	lang = "de"

# Open langauge lists
words = open("WordLists/" + lang + ".txt", "r").read().split("\n")[1:]
trans = open("Translations/" + lang + ".txt", "r").read().split("\n")

def Pad(inp, cols):
	f =  ""
	size = (cols/2) - (len(inp)/2)
	for i in range(size):
		f += " "
	return f + inp

def Capitize(inp):
	f = inp[0].upper()
	c = inp[1:]
	return f + c

def HorizontalRule(cols):
	hr = ""
	for i in range(cols):
		hr += "-"
	print hr

def Say(inp):
	os.system("echo \"" + inp + "\"|espeak -s " + str(speed) + " -v" + lang)

practiced = 0
while True:
	# Gets rows and colums of the terminal
	rows, cols = os.popen('stty size', 'r').read().split()
	rows = int(rows)
	cols = int(cols)
	# Clears the screen
	os.system("clear")

	word = words[random.randint(0, len(words))]
	word = Capitize(word)

	practiced += 1
	print("SpeakSprechen by Ben Faerber, " + trans[0])
	HorizontalRule(cols)
	print(Pad(word, cols))
	HorizontalRule(cols)
	print(trans[1] + " " + str(practiced))
	a = "s"
	while a != "":
		Say(word)
		a = raw_input(trans[2] + " ")