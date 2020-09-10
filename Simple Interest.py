def simple_interest(p,t,r):
    print('The principal amount is :',p)
    print('The time period is : ',t)
    print('The rate of interest is:',r)
    global si
    si = (p*t*r)/100
    print('The simple interest is :' , si)
    return si

principle = int(input("Enter Amount ."))
time =  int(input("\nTime period."))
rate =  float(input("\nRate of interest.."))
simple_interest(principle,time,rate)


annually = si/5
print("Annually:",annually)
monthly = annually/12
print("Monthly: ",monthly)
