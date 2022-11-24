from pydub import AudioSegment


def mp3ToWav ():
    name = input('Ingrese el nombre del archivo sin extension => ')
    src = f"./inputs/{name}.WAV"
    dst= f"./transcriptions/{name}.mp3"
    sound = AudioSegment.from_wav(src)
    sound.export(dst, format="mp3")

