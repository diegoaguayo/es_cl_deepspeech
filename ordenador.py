import csv
import os
from pydub import AudioSegment

tsv_names = ['dev.tsv','test.tsv','train.tsv']
path = os.getcwd()

#def mp3_to_wav(mp3_titles):
#    wav_titles = []
#    for mp3_title in mp3_titles:
#        aux = mp3_title.split(".")
#        wav_titles.append(aux[0] + ".wav")
#    return wav_titles

def mp3_to_wav(mp3_title):
    aux = mp3_title.split(".")
    return aux[0] + ".wav"

def ordenador(files):
    unclassified_cl = []
    classified_cl = []
    male_cl = []
    female_cl = []
    for file in files:
        tsv_file = open(file)
        read_tsv = csv.reader(tsv_file, delimiter="\t")

        for row in read_tsv:
            if row[7] == 'chileno':
                if row[6] == 'male':
                    male_cl.append((mp3_to_wav(row[1]),row[2]))
                    classified_cl.append(row[1])
                elif row[6] == 'female':
                    female_cl.append((mp3_to_wav(row[1]),row[2]))
                    classified_cl.append(row[1])
                else:
                    unclassified_cl.append(row[1])
        tsv_file.close()

    male_cl = set(male_cl)
    female_cl = set(female_cl)

    with open('./mcv_cl_male.tsv','wt') as male_file:
        male_writer = csv.writer(male_file, delimiter='\t')
        for tup in male_cl:
            male_writer.writerow(list(tup))

    with open('./mcv_cl_female.tsv','wt') as female_file:
        female_writer = csv.writer(female_file, delimiter='\t')
        for tup in female_cl:
            female_writer.writerow(list(tup))

    return set(classified_cl)

def mp3_2_wav(dirname,mp3_names):
    #sound.export("/output/path/file.wav", format="wav")    
    try: 
        os.mkdir('./wavs')
    except FileExistsError:
        pass

    l = len(mp3_names)
    counter = 0
    clips_dir = dirname + '/clips'
    #for mp3_name in os.listdir(clips_dir):
    for mp3_name in mp3_names:
        counter = counter + 1
        mp3_dir = clips_dir +'/'+ mp3_name
        #print(mp3_dir)
        name = mp3_name.split(".")
        wav_name = name[0] + ".wav"
        sound = AudioSegment.from_mp3(mp3_dir)
        wav_dir = './wavs/'+wav_name
        sound.export(wav_dir, format="wav")   
        percent = counter/l*100
        print(percent," %")

print("Creando csv")
names = ordenador(tsv_names)
#print(len(names))
print("Creando wavs")
mp3_2_wav(path, names)
print("Completado")

