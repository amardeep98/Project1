#program for showing license status on speed input
points=10
def Status():
    while True:
        speed=int(input("Enter the speed:"))
        if(speed<=70):
            print("Points=",globals()['points'])
            print("License intact.No need to worry.")
        else:
            check=speed%70                                         #to calculate how much above 70
            globals()['points']-=check//5
            if(globals()['points']>5):
                print("License intact.Slow down.")
                print("Points=",globals()['points'])
            else:
                print("License cancelled")                         #License cancels when points<=5
                break
Status()
