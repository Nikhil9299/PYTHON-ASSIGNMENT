date_time = '2020-01-15 09:03:32.744178'

a = lambda x: int(x[:4])
b = lambda x: int(x[5:7])
c = lambda x: int(x[8:10])
d = lambda x: x[11:]

year = a(date_time)
month = b(date_time)
day = c(date_time)
time = d(date_time)

print(f"Year : {year}")
print(f"Month : {month}")
print(f"Day : {day}")
print(f"Time : {time}")

