#!/usr/bin/python3
import time, colorama, os, pickle, sys, yapi, youtube_dl
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
  print ("version 1.9:")
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
      sys.exit()
  else:
    os.chdir(directory2)
def download():
  #https://youtu.be/y7guS3MPKg0
  URL = input("Введите ссылку: ")
  if input("Отобразить информацию о видео ? (y/n): ") == "y":
    id = URL[17:28]
    try:
      print (api.get_video_info(id))
    except:
      print ("Чяго ?")
      sys.exit()
  else:
    pass
  #Настройка разрешения видео
  if input("Загрузить видео ? (y/n): ") == "y":
    ydl_opts = {
      "postprocessor":[{
        "key": "ExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192"
      }]
    }
    resolw = input("Укажите разрешение , в котором будет загружено видео (144/360/720/audio/awt): ")
    if resolw == "144":
      opts = "160"
    elif resolw == "369":
      opts = "43"
    elif resolw == "360":
      opts = "18"
    elif resolw == "720":
      opts = "22"
    elif resolw == "audio":
      opts = "140"
    elif resolw == "awt":
      opts = "best"
    else:
      print ("Чяго ?")
      sys.exit()
    ydl_opts.update({"format": opts})
    del resolw
    #скачаивание видео
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([URL])
  else:
    pass
start()
dir()
while True:
  download()