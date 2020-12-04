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
    trans = trans.replace("'","")
    trans = trans.replace(':','')
    trans = trans.replace('-','')
    trans = trans.replace('–','')
    trans = trans.replace('’','')
    trans = trans.replace('ș','s')
    trans = trans.replace('ý','y')
    trans = trans.replace('ł','l')
    trans = trans.replace('à','a')
    trans = trans.replace('ō','o')
    trans = trans.replace('õ','o')
    trans = trans.replace('_',' ')
    trans = trans.replace('ã','a')
    trans = trans.replace('ë','e')
    trans = trans.replace('·','')
    return trans

def validate(trans):
	for caracter in trans:
		if caracter not in 'aábcdeéfghiíjklmnñoópqrstuúvwxyz ':
			print(trans)
			print(caracter)
			raise(TypeError)
	return True

def add_wavs(path):
    abs_path = os.getcwd()
    wav_path = abs_path + '/cv-corpus-5.1-2020-06-22/es/wavs'
    csv_path = abs_path + path
    #with open(path) as tsv_file:
    tsv_file = open(csv_path)
    csv_reader = csv.reader(tsv_file, delimiter='\t')
    l = sum(1 for row in csv_reader)
    tsv_file.close()
    counter = 0
    tsv_file = open(csv_path)
    csv_reader = csv.reader(tsv_file, delimiter='\t')
    wav_list = []
    for row in csv_reader:
        name = row[0]
        trans = row[1]
        trans = format(trans)
        validate(trans)
        #print('{0}/{1}'.format(wav_path,name))   
        data, s = librosa.load('{0}/{1}'.format(wav_path,name), sr=16000)
        soundfile.write('./new_cv/audios/{0}'.format(name), data, 16000)
	    	
        file_name = os.path.abspath('./new_cv/audios/{0}'.format(name))
        file_size = os.stat('./new_cv/audios/{0}'.format(name)).st_size
	    	
        wav_list.append([file_name,file_size,trans])
        counter = counter + 1
        percentage = counter/l*100
        #print("{:.1f}",format(percentage))
        print(percentage,'%')
    tsv_file.close()
    return wav_list


def generate_sets(wav_list, gender):

	print("GENERANDO SETS")

	shuffle(wav_list)
	n = len(wav_list)
	index1, index2 = int(0.7*n), int(0.9*n)
	train = wav_list[0: index1]
	dev = wav_list[index1: index2]
	test = wav_list[index2:]

	with open('./new_cv/train/train_'+gender+'.csv', 'w') as myfile:
	    wr = csv.writer(myfile)
	    wr.writerow(['wav_filename','wav_filesize','transcript'])
	    for row in train:
	    	wr.writerow(row)

	with open('./new_cv/dev/dev_'+gender+'.csv', 'w') as myfile:
	    wr = csv.writer(myfile)
	    wr.writerow(['wav_filename','wav_filesize','transcript'])
	    for row in dev:
	    	wr.writerow(row)

	with open('./new_cv/test/test_'+gender+'.csv', 'w') as myfile:
	    wr = csv.writer(myfile)
	    wr.writerow(['wav_filename','wav_filesize','transcript'])
	    for row in test:
	    	wr.writerow(row)

def preprocess_slr_dataset():
    seed(2020)
    try:
        os.mkdir('./new_cv')
        os.mkdir('./new_cv/audios')
        os.mkdir('./new_cv/train')
        os.mkdir('./new_cv/dev')
        os.mkdir('./new_cv/test')
    except FileExistsError:
        pass
    print('Preprocesando data hombres')
    male_wav_list = add_wavs('/cv-corpus-5.1-2020-06-22/es/mcv_cl_male.tsv')
    generate_sets(male_wav_list,'male')
    print("Preprocesando data mujeres")
    female_wav_list= add_wavs('/cv-corpus-5.1-2020-06-22/es/mcv_cl_female.tsv')
    generate_sets(female_wav_list,'female')

preprocess_slr_dataset()

