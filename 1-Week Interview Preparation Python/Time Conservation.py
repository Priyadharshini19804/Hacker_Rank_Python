"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Sample Input

07:05:45PM

Sample Output

19:05:45

"""

s = input()  # assume clean input like "07:05:45PM"

hour = int(s[:2])
minute = s[3:5]
second = s[6:8]
period = s[8:10]

if period == "AM":
    if hour == 12:
        hour = 0
else:  # PM
    if hour != 12:
        hour += 12

print(f"{hour:02d}:{minute}:{second}")
