import urllib.request
import csv
import time
import gdown

def get_images():
	with open('./urls.csv', "rt", encoding='utf-8') as infile:
		read = csv.reader(infile, delimiter=",")
		for row in read :
			print (row[1])
			if len(row) >= 2:
				words = row[1].split("=");
				if len(words) == 3:
					print (words[2])
					#time.sleep(5)
					try:
						#urllib.request.urlretrieve(str(row[1]), str(words[2]))
						gdown.download(str(row[1]), str(words[2]), quiet=False)
					except:
						print("errorrr")
			else:
				print ("nothing")
	print("done")

get_images()
