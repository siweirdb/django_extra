num = int(input())

hour = 9
minute = 0

time = 45 * num + int((num - 1) / 2) * 15 + (num - 1 - int((num - 1) / 2)) * 5
hour += int(time / 60)
minute += time % 60
print(hour, minute)
