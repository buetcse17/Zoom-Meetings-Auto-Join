print("""
                                             .__  .__ 
____________   ____   _____             ____ |  | |__|
\___   /  _ \ /  _ \ /     \   ______ _/ ___\|  | |  |
 /    (  <_> |  <_> )  Y Y  \ /_____/ \  \___|  |_|  |
/_____ \____/ \____/|__|_|  /          \___  >____/__|
      \/                  \/               \/         

    """)

import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import lst, week_day
import webbrowser


def printCurrentTime() :
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time = ", current_time)

keyboard = Controller()

isStarted = False

while True:
    for i in lst:
        currentDay = week_day[datetime.today().weekday()]
        currentMeeting = i[3]
        currentStart = i[1]
        currentEnd = i[2]
        
        if currentDay != i[4] :
            continue

        while True:
            if isStarted == False:
                if int(datetime.now().hour) >= int(i[1].split(':')[0]) and int(datetime.now().minute) >= int(i[1].split(':')[1]):
                    if int(datetime.now().hour) <= int(i[2].split(':')[0]) and int(datetime.now().minute) < int(i[2].split(':')[1]):
                        webbrowser.open(i[0])
                        isStarted = True
                        print("Current Day : " + currentDay + "DAY")
                        print("Current Meeting : " + currentMeeting)
                        print("Current Meeting Start : " + currentStart)
                        print("Current Meeting End : " + currentEnd)
                        print("Meeting Started ... (" + i[3] +")\n")  
                        print()
                    else:
                        break
                else:
                    break

            elif isStarted == True:
                if int(datetime.now().hour) >= int(i[2].split(':')[0]) and int(datetime.now().minute) >= int(i[2].split(':')[1]):
                    time.sleep(1)
                    isStarted = False
                    print("Meeting Ended ...(" + i[3] +")\n")
                    print()
                    break
    time.sleep(30)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
