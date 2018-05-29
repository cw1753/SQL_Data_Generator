from datetime import datetime
import random


# Generate the timeStamp data
# Can change the range of the time stamp
def genTimeStamp():
    year = random.randint(2015, 2018)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(1, 12)
    min = random.randint(0, 59)
    sec = random.randint(0, 59)
    timeStamp = datetime(year, month, day, hour, min, sec)
    return timeStamp