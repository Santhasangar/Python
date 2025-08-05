class Multifunction:
    def oddEven():
        n=int(input("Enter a Number:"))
        if((n%2)==0):
            print(f"{n} is Even number")
        else:
            print(f"{n} is odd number")

    def subfield():
        list1 = ['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are:")
        for i in list1:
            print(i)

    def Eligible():
        gender=input("your Gender")
        Age=int(input("your Age"))
        if(gender =="Male"):
            if(Age >=21):
                print("Eligible")
            else:
                print("Not Eligible")
        elif(gender == "Female"):
            if(Age>=18):
                print("Eligible")
            else:
                print("Not Eligible") 

    def Percentage():
        sub1=int(input("subject1= "))
        sub2=int(input("subject2= "))
        sub3=int(input("subject3= "))
        sub4=int(input("subject4= "))
        sub5=int(input("subject5= "))
        Total=int(sub1+sub2+sub3+sub4+sub5)
        Per=((Total)/500)*100
        print(f"Total:{Total}")
        print(f"percentage:{Per}")

    def triangle():
        H=int(input("Height: "))
        B=int(input("Breadth: "))
        print("Area Formula: Height*Breadth/2 ")
        Area=(H*B)/2
        print(f"Are of triangle: {Area}")
        H1=int(input("Height1: "))
        H2=int(input("Height2: "))
        B=int(input("Breadth: "))    
        print("Perimeter Formula: Height1+Height2+Breadth")
        peri=H1+H2+B
        print(f"Perimeter of Triangle:{peri}") 

    def BMI():
        BMI=float(input("Enter the BMI Index:"))
        if(BMI < 18.5):
              print("Under Weight")
        elif(BMI > 18.5 and BMI <= 25):
              print("Normal Weight")
        elif(BMI > 25 and BMI <= 30):
              print("Over Weight")
        else:
              print("Very Overweight")
    