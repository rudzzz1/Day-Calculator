y = int(input("Enter the year"))
m = int(input("Enter the month"))
d = int(input("Enter the date"))

if y % 4 == 0:
     
    if m == 1:
         days = d
         
    elif m == 2:
         days = 31 + d
         
    elif m == 3:
         days = 31 + 29 + d
         
    elif m == 4:
         days = 31 + 29 + 31 + d
         
    elif m == 5:
         days = 31 + 29 + 31 + 30 + d
         
    elif m == 6:
         days = 31 + 29 + 31 + 30 + 31 + d
        
    elif m == 7:
         days = 31 + 29 + 31 + 30 + 31 + 30 + d
        
    elif m == 8:
         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + d
        
    elif m == 9:
         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + d
        
    elif m == 10:
         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + d
        
    elif m == 11:
         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + d
         
    elif m == 12:
         days = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + d
         
else:
    
    if m == 1:
         days = d
         
    elif m == 2:
         days = 31 + d
         
    elif m == 3:
         days = 31 + 28 + d
         
    elif m == 4:
         days = 31 + 28 + 31 + d
         
    elif m == 5:
         days = 31 + 28 + 31 + 30 + d
         
    elif m == 6:
         days = 31 + 28 + 31 + 30 + 31 + d
        
    elif m == 7:
         days = 31 + 28 + 31 + 30 + 31 + 30 + d
        
    elif m == 8:
         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + d
        
    elif m == 9:
         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + d
        
    elif m == 10:
         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + d
        
    elif m == 11:
         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + d
         
    elif m == 12:
         days = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + d
         

NumberOfLeapYears = int(y / 4)

TotalDays = y * 365 + NumberOfLeapYears

day = TotalDays + days

m = day % 7
n = m + 5

if n > 7:
    n = n - 7
else:
    pass

if y % 4:
    n = n + 1
else:
    pass

if ( n == 2 ):
    print("Monday")
    
elif( n == 3 ):
    print("Tuesday")
    
elif( n == 4 ):
    print("Wednesday")
        
elif( n == 5 ):
    print("Thursday")
    
elif( n == 6 ):
    print("Friday")
    
elif( n == 7 ):
    print("Saturday")
    
else:
    print("Sunday")
