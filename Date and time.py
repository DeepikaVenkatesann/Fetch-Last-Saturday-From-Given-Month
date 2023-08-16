def lastsaturday(month, year):
    lastday = datetime(year, month + 1, 1) - timedelta(days=1)
    weekdays = lastday.isoweekday()
    last_sat = lastday - timedelta(days=weekdays + 1)
    return last_sat.day, (last_day.day - last_sat.day) // 7 + 1

def totalsaturdays(month, year):
    firstday = datetime(year, month, 1)
    numofsaturdays = (firstday.weekday() - 7) % 7
    return (firstday + timedelta(days=numofsaturdays)).day

input_month_year = "062023"
month = int(input_month_year[:2])
year = int(input_month_year[2:])

last_sat, total_sats = lastsaturday(month, year)
total_sats = totalsaturdays(month, year)

print("Last Saturday:",last_sat)
print("Total Saturdays:",total_sats)
