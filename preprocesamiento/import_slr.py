from random import seed, randint, shuffle
import csv
import os
import wave
import librosa
import soundfile

def format(trans):
	trans = trans.lower()
	trans = trans.replace('.', '')
	trans = trans.replace(',', '')
	trans = trans.replace('¿', '')
	trans = trans.replace('?', '')
	trans = trans.replace('¡', '')
	trans = trans.replace('!', '')
	trans = trans.replace(';', '')
	trans = trans.replace('\\', '')
	trans = trans.replace('"', '')
	trans = trans.replace('ü', 'u')
	trans = trans.replace('3d', 'tres de')
	return trans

def validate(trans):
	for caracter in trans:
		if caracter not in 'aábcdeéfghiíjklmnñoópqrstuúvwxyz ':
			print(trans)
			print(caracter)
			raise(TypeError)
	return True

def add_wavs(path, wav_list):
	with open(path+'line_index.tsv') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter='\t')
	    wav_list = []
	    for row in csv_reader:
	    	name = row[0]
	    	trans = row[1]
	    	trans = format(trans)
	    	validate(trans)
	    	
	    	data, s = librosa.load('{0}{1}.wav'.format(path,name), sr=16000)
	    	soundfile.write('./new_slr/audios/{0}.wav'.format(name), data, 16000)
	    	
	    	file_name = os.path.abspath('./new_slr/audios/{0}.wav'.format(name))
	    	file_size = os.stat('./new_slr/audios/{0}.wav'.format(name)).st_size
	    	
	    	wav_list.append([file_name, file_size, trans])
	return wav_list


def generate_sets(wav_list, gender):

	print("GENERANDO SETS")

	shuffle(wav_list)
	n = len(wav_list)
	index1, index2 = int(0.7*n), int(0.9*n)
	train = wav_list[0: index1]
	dev = wav_list[index1: index2]
	test = wav_list[index2:]

	with open('./new_slr/train/train_{0}.csv'.format(gender), 'w') as myfile:
	    wr = csv.writer(myfile)
	    wr.writerow(['wav_filename','wav_filesize','transcript'])
	    for row in train:
	    	wr.writerow(row)

	with open('./new_slr/dev/dev_{0}.csv'.format(gender), 'w') as myfile:
	    wr = csv.writer(myfile)
	    wr.writerow(['wav_filename','wav_filesize','transcript'])
	    for row in dev:
	    	wr.writerow(row)

	with open('./new_slr/test/test_{0}.csv'.format(gender), 'w') as myfile:
	    wr = csv.writer(myfile)
	    wr.writerow(['wav_filename','wav_filesize','transcript'])
	    for row in test:
	    	wr.writerow(row)

def preprocess_slr_dataset(gender):
	seed(2020)
	try:
		os.mkdir('./new_slr/')
		os.mkdir('./new_slr/audios')
		os.mkdir('./new_slr/train')
		os.mkdir('./new_slr/dev')
		os.mkdir('./new_slr/test')
	except FileExistsError:
		pass

	print("Preprocesando data {0}".format(gender))
	wav_list = add_wavs('./slr/es_cl_{0}/'.format(gender), [])
	generate_sets(wav_list, gender)

preprocess_slr_dataset('male')
preprocess_slr_dataset('female')

