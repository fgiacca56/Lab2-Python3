seconds = int(input("Enter amount of seconds:"))
hours = (seconds // 3600)
minutes = (seconds % 3600) // 60
Seconds = (seconds%3600)%60
print(seconds, " seconds is", hours , "hours,", minutes, "minutes,", "and", Seconds, "seconds")

