import csv
import os
from random import seed, shuffle

try:
	os.mkdir('./training_sets/')
except FileExistsError:
	pass

def open_file(dataset, _set,gender):
	with open('./new_{0}/{1}/{1}_{2}.csv'.format(dataset, _set, gender), 'r') as csv_file:
		file = csv.reader(csv_file, delimiter=',')
		i = 0
		lines = []
		for row in file:
			if i == 0:
				i = 1
			else:
				lines.append(row)
		return lines

def merge(_set):
	
	female_slr = open_file('slr', _set, 'female')
	female_cv = open_file('cv', _set, 'female')
	male_slr = open_file('slr', _set, 'male')
	male_cv = open_file('cv', _set, 'male')

	concatencacion = female_slr + female_cv + male_slr + male_cv
	shuffle(concatencacion)

	with open('./training_sets/{0}.csv'.format(_set), 'w') as myfile:
	    wr = csv.writer(myfile)
	    wr.writerow(['wav_filename','wav_filesize','transcript'])
	    for row in concatencacion:
	    	wr.writerow(row)


merge('train')
merge('dev')
merge('test')