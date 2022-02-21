import time
from plyer import notification

def main():
    focus = int(input("Focus Length: "))
    shortBreak = int(input("Short Break: "))
    longBreak = int(input("Long Break: "))
    rounds = int(input("Rounds: "))
    # countdown(45,5,15,10) //default
    countdown(focus, shortBreak, longBreak, rounds)

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="redBell.ico",
        timeout=5
    )


def focusTimer(focus):
    focusTime = str((focus // 60)) + " MINUTES"
    notify("FOCUS", focusTime)
    while focus:
        mins, secs = divmod(focus, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        focus -= 1


def shortBreakTimer(shortBreak):
    shortBreakTime = str((shortBreak // 60)) + " MINUTES"
    notify("SHORT BREAK", str(shortBreakTime))
    while shortBreak:
        mins, secs = divmod(shortBreak, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        shortBreak -= 1

def longBreakTimer(longBreak):
    longBreakTime = str((longBreak // 60)) + " MINUTES"
    notify("LONG BREAK", str(longBreakTime))
    while longBreak:
        mins, secs = divmod(longBreak, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        longBreak -= 1


def countdown(f, short, long, rounds):
    originalRound = rounds
    longBreak = long * 60
    while True:
        while rounds:
            shortBreak = short * 60
            focus = f * 60
            print("ROUND ", rounds)
            focusTimer(focus)
            shortBreakTimer(shortBreak)
            rounds -= 1
        longBreakTimer(longBreak)
        rounds = originalRound


if __name__ == "__main__":

    main()
