# Greet the user based on the time of the day

import datetime

current_hour = datetime.datetime.now().hour

if 6 <= current_hour < 12:
    print("Good morning!")
elif 12 <= current_hour < 18:
    print("Good afternoon!")
else:
    print("Good evening!")
