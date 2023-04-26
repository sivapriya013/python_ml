# year = int(input("year:"))
# if year%4==0:
#     print("its a leapyear")
#
# elif year%100==0:
#     print("its a leap year")
#
# elif year%400==0:
#     print("its a leap year")
#
# else:
#     print("its not a leap year")

year = int(input("enter a year:"))
if year%4==0 and year%100==0 and year%400==0:
    print("its a leap year")

else:
    print("its not a leap year")
