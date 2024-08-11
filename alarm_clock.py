from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(seconds):
    time_elapesed = 0

    print(CLEAR)
    while time_elapesed < seconds:
        time.sleep1(1)
        time_elapsed += 1

        time_left = seconds - time_elapesed
        minutes_left = time_left // 60
        seconds_left = time_left % 60 

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)