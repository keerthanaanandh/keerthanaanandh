import random
def temp(k):
    if c>0 and c<44.0:
        print("the temperature is : ",c,"which is safe")
        print("correct temperature")
    elif c<0:
        print("the temperature is",c,"which is too low")
        print("danger: LOW TEMPERATURE!!!")
    elif c>44.0:
        print("the temperature is",c,"which is too high")
        print("danger:HIGH TEMPERATURE!!!")
c=random.randint(-22.0,60.0)
temp(c)
