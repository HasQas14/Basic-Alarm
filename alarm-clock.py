# Docstring
"""A simple clock where it plays a sound after X number of minutes/seconds or at a particular time."""
from datetime import date,datetime,timedelta
import winsound
import time
def setAlarm(numberOfBeeps=10): # default beeps 10
    print("Set ALarm time ")
    while True:
        try:
            tm_h = int(input("Hour: "))
            tm_m = int(input("Minute: "))
        except ValueError:
            print("Wrong Input!")
            continue
        else:
            break
    tm_am_or_pm = input("AM Or PM?  ").upper()
            
    while True:
        if tm_am_or_pm == "AM" or tm_am_or_pm == "PM":
            tm = ("%02d")%tm_h+":"+("%02d")%tm_m+" "+tm_am_or_pm
            print(time)
            break
        else:
            print("Please Enter correct timezone")
            tm_am_or_pm = input("AM Or PM?  ")
            continue

    tm_usr = datetime.strptime(tm,'%H:%M %p').time()
    print(tm_usr)

    tm_now = datetime.now().strftime('%I:%M:%S')
    tm_now = datetime.strptime(tm_now,'%I:%M:%S').time()
    print(tm_now)

    # Difference Logic
    diff = datetime.combine(date.min, tm_usr) - datetime.combine(date.min, tm_now)
    diff_int = diff.seconds
    print(diff_int)
    time.sleep(diff_int)

    for i in range(numberOfBeeps):
        winsound.Beep(1000,100)
        winsound.Beep(1000,100)
        time.sleep(1)

# enter one argument for number of times it beeps
if __name__ == "__main__":
    setAlarm(15)