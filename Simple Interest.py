def simple_interest(p,t,r):
    print('The principal amount is :',p)
    print('The time period is : ',t)
    print('The rate of interest is:',r)
    si = (p*t*r)/100
    print('The simple interest is :' , si)


    return si
principle = int(input("Enter Amount ."))
time =  int(input("\nTime period."))
rate =  float(input("\nRate of interest.."))

print("Simple interest",simple_interest(principle,time,rate))

simpl = principle*time*rate/100
per_year = simpl/5
print("Total :",per_year)
per_month = per_year/12
print("Every Moth",per_month)
