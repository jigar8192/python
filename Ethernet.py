import psutil
import pyttsx3
import time
#######################################################
engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(jigar):
    engine.say(jigar)
    engine.runAndWait()
#######################################################
def Ethernet():
    try:
        data1 = psutil.net_if_stats()['Ethernet'][0]
        #print(data1)
        return data1
    except:
        return False
#Ethernet()
########################################################
def wifi():
    data1 = psutil.net_if_stats()['Wi-Fi'][0]
    return data1
#########################################################
def plugged_info():
    plugged = psutil.sensors_battery()[2]
    return plugged
#########################################################
falgb = 0
falg = 0
falgwifi = 0
while True:
    info = Ethernet()
    if info == True:
        if falg == 0:
            print(f"connected Ethernet")
            falg = 1
    if ((falg == 1)&(Ethernet() == False)):
        falg = 0
        print("disconnected Ethernet")
    #######################################################
    percent = psutil.sensors_battery()[0]
    info = plugged_info()
    if info == True:
        if falgb == 0:
            print(f"charger connected , {percent} percent")
            falgb = 1
    elif ((falgb == 1)&(plugged_info() == False)):
        falgb = 0
        print(f"disconnected charger , {percent} percent")
    #########################################################
    try:
        info = wifi()
        if info == True:
            if falgwifi == 0:
                speak(f"connected wi-fi network")
                falgwifi = 1
            elif ((falgwifi == 1)&(wifi() == False)):
                falgwifi = 0
                speak("disconnected wi-fi network")
    except:
        pass
    #########################################################