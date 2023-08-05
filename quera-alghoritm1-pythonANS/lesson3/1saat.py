hour, minute = map(int, input().split())
rhour = 12 - hour 
rminute = 60 - minute
if hour == 0:
    rhour = 0 
if minute == 0:
    rminute = 0
print()
print("%.2d:%.2d"%(rhour,rminute))
