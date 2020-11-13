import os
from subprocess import call
sys = os.name
if sys == "posix":
  what = input("Termux/linux ?: ")
  if what == "Termux":
    try:
      os.system("pip install yapi")
    except:
      pass
    try:
      os.system("pip install colorama")
    except:
      pass
    try:
      os.system("pip install youtube-dl")
    except:
      pass
    os.system("cp Download.py /data/data/com.termux/files/usr/bin")
    os.chdir("/data/data/com.termux/files/usr/bin")
    call(["chmod", "0777", "Download.py"])
    os.rename("Download.py", "Download")
  if what == "linux":
    try:
      os.system("sudo apt-get install python3-pip")
    except:
      pass
    try:
      os.system("sudo pip3 install colorama")
    except:
      pass
    try:
      os.system("sudo pip3 install yapi")
    except:
      pass
    try:
      os.system("sudo pip3 install youtube-dl")
    except:
      pass
    os.system("cp Download.py /usr/bin")
    os.chdir("/usr/bin")
    call(["chmod", "0777", "Download.py"])
    os.rename("Download.py", "Download")
else:
  print ("Данная система пока не поддерживается")