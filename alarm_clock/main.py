import datetime
import pyglet

AUDIO_PATH = '' # supply path for audio file to play when alarm goes off
player = pyglet.media.Player()
MediaLoad = pyglet.media.load(AUDIO_PATH)

alarm_hour = int(input("What hour do you want to wake up?"))
minute = input("What minute do you want to wake up?")
alarm_minute = int(minute)
am_pm = str(input("Lastly, am or pm?"))
print('Alarm set for: '+str(alarm_hour)+':'+str(minute)+am_pm)

if (am_pm == "pm"):
    alarm_hour = alarm_hour + 12

while(1 == 1):
    if(alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute):
        print("Another day to achieve thine greatness. ")
        player.queue(MediaLoad)
        player.play()
        break

pyglet.app.run()