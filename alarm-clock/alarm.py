import datetime
import time
from playsound import playsound

print("------ PYTHON ALARM CLOCK ------")

def set_alarm():
    alarm_time = input("Enter alarm time (HH:MM:SS, 24-hour format): ")
    print(f"Alarm set for {alarm_time}...")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("\nALARM RINGING!!!!!")
            try:
                playsound("alarm.mp3")
            except:
                print("Error playing sound. Make sure alarm.mp3 exists.")
            break
        time.sleep(1)

set_alarm()
