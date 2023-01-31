from datetime import date
print(sum(sum(date(year=y, day=1, month=m).strftime("%A") == "Sunday" for m in range(1, 13)) for y in range(1901, 2001)))