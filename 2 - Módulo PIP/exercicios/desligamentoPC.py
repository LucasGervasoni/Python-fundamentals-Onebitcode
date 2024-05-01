import os

#Desligar computador
#os.system("shutdown /s") #desliga em 60s
#os.system("shutdown /s /t 0") #desliga o computador imediatamente
#os.system("shutdown now") - linux

#cancela o desligamento
#os.system("shutdown /a")

def turn_off_one_hour():
  os.system("shutdown /s /t 3600")

def turn_off_half_hour():
  os.system("shutdown /s /t 1800")
  
def cancel_shutdown():
  os.system("shutdown / a")