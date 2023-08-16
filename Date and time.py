def lastsaturday(month, year):
    last_day = datetime(year, month + 1, 1) - timedelta(days=1)
    weekdays = last_day.isoweekday()
    last_sat = last_day - timedelta(days=weekdays + 1)
    return last_sat.day, (last_day.day - last_sat.day) // 7 + 1

def totalsaturdays(month, year):
    firstday = datetime(year, month, 1)
    numsaturdays = (firstday.weekday() - 7) % 7
    return (firstday + timedelta(days=numsaturdays)).day

input_month_year = "062023"
month = int(input_month_year[:2])
year = int(input_month_year[2:])

last_sat, total_sats = lastsaturday(month, year)
total_sats = totalsaturdays(month, year)

print("Last Saturday:",last_sat)
print("Total Saturdays:",total_sats)