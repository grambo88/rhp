#-*- coding: UTF-8 -*-
"""
RHP - Race Horse Pro
Tyler Gramling
"""

import PyPDF2 as p2
import sys, re, time


raceform = "raceform.pdf"
raceGrades = ("Alw", "OC", "Clm", "Md")

def newFunction(line):
	huh = re.split(" ", line)
	#print(huh)

	nl1 = re.split(":", huh[0])
	#print(nl1)

	#print(nl1[0])

	try:
		value = nl1[1]
		#print(value)
		huh[0] = value
		#print(huh)
		huh.insert(0, nl1[0])
		print(huh)
	except IndexError:
		print(huh)
		value = None



	#print(nl1[1])


	# my_string = ','.join(map(str, nl1)) 
	# print(my_string)


	# if huh[0] in huh:
	# 	ty = re.split(":", huh[0])
	# 	print(huh[0])
	# 	print(ty)

	


def nextStep(data):

	with open("cleanText.txt", "r") as f1:
		with open("newClean.txt", "w") as f2:
			lines = [line.rstrip('\n') for line in f1.readlines()]
			for line in lines:
				if any(s in line for s in raceGrades):
					newFunction(line)
					#print("--------this is in the way------")
				else:
					print(line)



def scrambledText(raceform):

	start_time = time.time()

	print("\nExtracting and loading data sets...\n")

	PDFfile = open(raceform, "rb")
	pdfread = p2.PdfFileReader(PDFfile)

	orig_stdout = sys.stdout
	f = open("output.txt", "w")
	sys.stdout = f

	count = pdfread.numPages

	for i in range(count):
	    page = pdfread.getPage(i)
	    v = page.extractText()
	    print(v)

	sys.stdout = orig_stdout
	f.close()


def cleanTimes(data):

	with open("cleanText.txt", "r") as f1:
		lines = [line.rstrip('\n') for line in f1.readlines()]
		for line in lines:
			if any(s in line for s in raceGrades):
				pass
#print(line)


def cleanUp(data):

	orig_stdout = sys.stdout
	f = open("cleanText.txt", "w")

	sys.stdout = f

	with open("output.txt", "r") as f2:
		data = f2.readlines()
		data = [x.strip() for x in data]

		for f in data:
			f = f.replace('¥', '0')
			f = f.replace('¦', '1')
			f = f.replace('§', '2')
			f = f.replace('¨', '3')
			f = f.replace('©', '4')
			f = f.replace('ª', '5')
			f = f.replace('«', '6')
			f = f.replace('¬', '7')
			f = f.replace('¤', '8')
			f = f.replace('®', '9')
	        ###
			f = f.replace('ô' , '1/2')
			f = f.replace('= ', '-')
			f = f.replace('1:', ' 1:')
			f = f.replace('Î', '^ ')
			f = f.replace('õ', '1/4')
			f = f.replace('Ð', ' ')
			f = f.replace(' /', '/')
	        ###
			f = f.replace('â', 'Jan')
			f = f.replace('á', 'Feb')
			f = f.replace('à', 'Mar')
			f = f.replace('ß', 'Apr')
			f = f.replace('Ü', 'May')
			f = f.replace('Þ', 'Jun')
			f = f.replace('Û', 'Jly')
			f = f.replace('Ý', 'Aug')
			f = f.replace('æ', 'Sep')
			f = f.replace('å', 'Oct')
			f = f.replace('ä', 'Nov')
			f = f.replace('ã', 'Dec')
	        ###
	    #    f = f.replace('ê', '--TRACK--')
	    #    f = f.replace('ï', '--TRACK--')
	    #    f = f.replace('Ñ', '--TRACK--')
			f = f.replace('Ö', '--TRACK MARKER--')
			f = f.replace('ÿ', '--UNKNOWN--')
			f = f.replace('Ç', 'hd ')
			f = f.replace('É', 'nk')
			f = f.replace('=', '-')
			f = f.replace('ö', '3/4')
			f = f.replace('Â', '1/16')
	        ###
			print(f)
		sys.stdout = orig_stdout
		f2.close()
























