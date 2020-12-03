import sys
import ctypes
from _datetime import datetime
import time

time_tuple = (1950,  # Year
              1,  # Month
              1,  # Day
              0,  # Hour
              15,  # Minute
              0,  # Second
              0,  # Millisecond
              )

def _win_set_time(time_tuple):
    import win32api
    dayOfWeek = datetime(*time_tuple).isocalendar()[2]
    t = time_tuple[:2] + (dayOfWeek,) + time_tuple[2:]
    win32api.SetSystemTime(*t)

def is_admin():
    try:
        print("admin")
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        print("not admin")
        return False

if __name__ == "__main__":
    
    print("Enter the time you want set XX:XX:XX :")
    while(1):
        while(1):
            time = input()
            if(len(time) == 8):
                break
            print("Time format wrong \nEnter a valid time format XX:XX:XX")
        times = time.split(":")
        hours = int(times[0]) #Can't be beyond 23
        minutes = int(times[1]) #Can't be beyond 59
        secondes = int(times[2]) #Can't be beyond 59
        if(hours <= 23):
            if(minutes <= 59):
                if(secondes <= 59):
                    break
                else:
                    print("Seconds musn't exceed 59")
            else:
                print("minutes musn't exceed 59")
        else:
            print("Hours musn't exceed 24")
        
        print("Enter time again")

    s_minutes = 0
    s_hours = 0
    case = 0
    if(minutes != 0):
        s_minutes = minutes * 60
    else:
        case = 1
    if(hours != 0):
        s_hours = hours * 3600
    else:
        case = 2

    total_s = secondes + s_minutes + s_hours #Total time in seconds

    time_t = []
    time_t.append(2000)
    time_t.append(1)
    time_t.append(1)
    time_t.append(hours)
    time_t.append(minutes)
    time_t.append(secondes)
    time_t.append(0)
    time_tuple = tuple(time_t) #First tuple to display
    _win_set_time(time_tuple)
    print(time_tuple)

    lapsed = 0
    
    t = list(time_tuple)
    print(total_s)
    print(sys.platform)
    
    if is_admin():
        print("In win")
        if sys.platform == 'win32':
            print("In win")
            _win_set_time(time_tuple)
            while(lapsed != total_s):
                t[5] = t[5] - 1
                #processing cases
                if(t[5] <= 0 and t[4] != 0):
                    t[5] = 59
                    t[4] = t[4] - 1
                    if(t[4]<=0 and t[3] != 0):
                        t[4] = 59
                        t[3] = t[3] - 1

                time_tuple = tuple(t)
                _win_set_time(time_tuple)
                lapsed += 1 
                time.sleep(1)
    else:
        print("ad")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    
    '''
        
    c = 0

    if is_admin():
    # Code of your program here
        if sys.platform == 'win32':
            while(c<=10):
                _win_set_time(time_tuple)
                time.sleep(1)
                t = list(time_tuple)
                t[4] = t[4] - 1
                time_tuple = tuple(t)
                c += 1 
                


    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
'''