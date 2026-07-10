Age=int(input("Enter your present age :"))
year_left=100-Age
days=year_left*365
hours=days*24
minutes=hours*1440
seconds=minutes*86400
print(f"years left:{year_left}")
print(f"days left:{days}")
print(f"hours:{hours}")
print(f'minutes:{minutes}')
print(f"seconds:{seconds}")