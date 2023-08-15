
data = {
    "pageHistory": "0,1,2,3", # NOT [0, 1, 2, 3]
    "entry.1515162132": "2023-12-09",
    # "entry.1515162132_month": "08",
    # "entry.1515162132_day": "09",
    "entry.243388263": "test1",
    "entry.1887472648": "name",
    "entry.1436737042": "Week A",
    "entry.195050451": "Monday",
    "entry.525015880": "1",
    "entry.1169215245": "10 ENG BRK",
}

real_data = {
    
}

import requests

url = "https://docs.google.com/forms/d/e/1FAIpQLSdeqP3r7lqXT6nLM_oIWVzbI4iLaM-bR08sYvOswWMQU9i6GA/formResponse?pageHistory=0,1,2,3&entry.1887472648=aaaa&entry.243388263=prefill&entry.1515162132=2023-09-01&entry.1436737042=Week+A&entry.195050451=Monday&entry.525015880=1&entry.1169215245=10+ENG+BRK"

# s = requests.post(url, data=data)


r = requests.post("https://docs.google.com/forms/d/e/1FAIpQLSdeqP3r7lqXT6nLM_oIWVzbI4iLaM-bR08sYvOswWMQU9i6GA/formResponse", data=data)

with open("test.html", "w", encoding="utf-8") as f:
    f.write(r.text)
    