from data import timetable, weekdays, entries
import webbrowser
import keyboard
import os
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
load_dotenv()

NAME = os.getenv("NAME")
SURNAME = os.getenv("SURNAME")
FORM = os.getenv("FORM")

today = datetime.now()



def finalform(period):
    weekday = weekdays[today.weekday()]
    weekday = "Monday"
    year = str(today.year)
    month = str(today.month)
    month = "0" + month if len(month) == 1 else month
    day = str(today.day)
    day = "0" + day if len(day) == 1 else day
    bigform = FORM
    bigform += entries["name"] + "=" + NAME + "&"
    bigform += entries["surname"] + "=" + SURNAME + "&"
    bigform += entries["year"] + "=" + year + "&"
    bigform += entries["month"] + "=" + month + "&"
    bigform += entries['day'] + '=' + day + "&"
    bigform += entries["week"] + "=" + "Week+B" + "&"
    bigform += entries["weekday"] + '=' + weekday + "&"
    # bigform += entries["periodb"][today.weekday()] + '=' + str(period) + "&"
    bigform += entries["periods"][0] + '=' + str(period) + "&"

    # bigform += timetable[today.weekday()][period - 1][1] + \
    #     "=" + timetable[today.weekday()][period - 1][0]
    bigform += timetable[0][period - 1][1] + \
    "=" + timetable[0][period - 1][0]
    
    return bigform




