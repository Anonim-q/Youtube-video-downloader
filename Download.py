#!/usr/bin/python3
import time, colorama, os, pickle, sys, yapi
from subprocess import call
data = "download.data"
api = yapi.YoutubeAPI("AIzaSyAJMzX_t_tRoiSBs7-PS8eSnn6wdK9L1Us")
try:
  with open(data, "rb") as file:
    directory2 = pickle.load(file)
    dire = True
    print (directory2)
except:
  dire = False
colorama.init
def start():
  print (colorama.Fore . WHITE + "Youtube downloader")
  time.sleep(1)
  print (colorama.Style . RESET_ALL)
  print (colorama.Fore . RED + "By Blinc")
  print ("version 1.0:")
  print (colorama.Fore . BLUE + "Канкатенация решает")
  print (colorama.Style . RESET_ALL)
def dir():
  if dire == False:
    try:
     directory = input("Папка: ")
     what = input("Запомнить дерикторию ? (y/n): ")
     if what == "y":
       with open(data, "wb") as file:
         pickle.dump(directory, file)
       del what
     else:
       del what
     os.chdir(directory)
    except:
      print ("Неизвестная ошибка")
      sys.exit
  else:
    os.chdir(directory2)
def download():
  #https://youtu.be/y7guS3MPKg0
  URL = input("Введите ссылку: ")
  if input("Отобразить информацию о видео ? (y/n): ") == "y":
    id = URL[17:28]
    print (api.get_video_info(id))
  else:
    pass
  #Настройка разрешения видео
  if input("Загрузить видео ? (y/n): ") == "y":
    resolw = input("Укажите разрешение , в котором будет загружено видео (144/240/360/720/audio/awt): ")
    if resolw == "144":
      resolution = "160"
    elif resolw == "240":
      resolution = "5"
    elif resolw == "360":
      resolution = "43"
    elif resolw == "369":
      resolution = "18"
    elif resolw == "720":
      resolution = "22"
    elif resolw == "audio":
      resolution = "140"
    elif resolw == "awt":
      resolution = "best"
    adr = "youtube-dl" + " -f " + resolution + " " + URL
    del resolution
    #скачаивание видео
    video = call(adr.split(), shell=False)
  else:
    pass
start()
dir()
while True:
  download()