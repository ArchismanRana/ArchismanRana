import time

timestamp = time.strftime('%H:%M:%S') #Shows exact time
print(timestamp)

Hour = int(time.strftime('%H'))
print(Hour)

if Hour==18:
    print("It's Bedtime!! Go for sleep!")

#Code for wakeup
recent_time = time.strftime('%H:%M:%S')
Recenttime = int(time.strftime('%H'))
name=input("Your Name:")
c= name.capitalize()
if(4<=Recenttime<12):
    print('GOOD MORNING',c,'its',recent_time)
elif(12>=Recenttime<17):
    print('GOOD EVENING',c,'its',recent_time)
else:
    print('GOOD NIGHT',c,'its',recent_time)
