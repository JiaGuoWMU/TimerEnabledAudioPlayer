from datetime import datetime
from threading import Timer
import pygame as pg


def play_music(music_file, volume = 0.8):
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 2048
    pg.mixer.init(freq, bitsize, channels, buffer)
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found!".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clock.tick(30)


current_time = datetime.today()

# set the time to be a minute after
year = current_time.year
month = current_time.month
day = current_time.day
hour = current_time.hour
minute = current_time.minute + 1
set_time = datetime(year, month, day, hour, minute)

delta_time = set_time - current_time
delta_time_in_seconds = delta_time.seconds + 1

file_name = 'test.wav'
volume = 0.8
t = Timer(delta_time_in_seconds, play_music, [file_name, volume])
t.start()