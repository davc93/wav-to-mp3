import os
from pydub import AudioSegment


def mp3ToWav ():
    if not os.path.exists('./inputs'):
        os.makedirs('inputs')
    if not os.path.exists('./transcriptions'):
        os.makedirs('transcriptions')
    
    name = input('Ingrese el nombre del archivo sin extension => ')
    src = f"./inputs/{name}.WAV"
    dst= f"./transcriptions/{name}.mp3"
    sound = AudioSegment.from_wav(src)
    sound.export(dst, format="mp3")

