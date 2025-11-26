age = int(input("enter your age:"))
def election(age):
    if (age>18):
        print("elligible to vote")
    elif(age<18):
        print("not elligible")

election(age)

