from datetime import datetime, time
from time import sleep
from driver import submit

today = datetime.now()
periodtimes = [
    datetime.combine(today, time(8, 55, 0)),
    datetime.combine(today, time(9, 40, 0)),
    datetime.combine(today, time(10, 40, 0)),
    datetime.combine(today, time(11, 20, 0)),
    datetime.combine(today, time(12, 45, 0)),
    datetime.combine(today, time(13, 30, 0))
]

for i in range(6 if today.weekday() != 2 else 3):
    submit(i + 1)
    sleep((periodtimes[i] - datetime.now()).total_seconds())