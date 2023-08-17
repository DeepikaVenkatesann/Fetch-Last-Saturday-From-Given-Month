from datetime import datetime, timedelta
def lastsaturday(month, year):
    lastday = datetime(year, month + 1, 1) - timedelta(days=1)
    weekdays = lastday.isoweekday()
    days_to_subtract = (weekdays - 5) % 7 
    lastsaturday = lastday - timedelta(days=days_to_subtract)
    return lastsaturday.day

def totalsaturdays(month, year):
    first_day = datetime(year, month, 1)
    last_day = datetime(year, month + 1, 1) - timedelta(days=1)
    num_saturdays = sum(1 for day in range((last_day - first_day).days + 1) if (first_day + timedelta(days=day)).weekday() == 5)
    return num_saturdays
    
last_sat, total_sats = lastsaturday(month=6, year=2023)
total_sats = totalsaturdays(month=6, year=2023)

print("Last Saturday:",last_sat)
print("Total Saturdays:",total_sats)
