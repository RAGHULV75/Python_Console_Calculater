def cal():
    print(" \n\n\t\t\t Welcome to calculater ")
    print(''' \n\t
            1. Addtion Operation         ( Press 1 )
            2. Subtraction Operation     ( Press 2 )
            3. Multiplication Operation  ( Press 3 )
            4. Divition Operation        ( Press 4 )
            5. Modulo Operation          ( Press 5 )
            ''')
    a=int(input("Enter the 1st value : "))
    option=int(input("Select your Operation : "))
    b=int(input("Enter the 2nd value : "))
    
    if(option==1):
        c=a+b
        print(c)
        t=input("S to Reload & anything to Exit : ")
        if(t=='s'):
            return cal()
        else:
            print (" Bye Have a Good Day ! ")     
    elif(option==2):
        c=a-b
        print(c)
        return cal()
        t=input("S to Reload & anything to Exit : ")
        if(t=='s'):
            return cal()
        else:
            print (" Bye Have a Good Day ! ")
    elif(option==3):
        c=a*b
        print(c)
        t=input("S to Reload & anything to Exit : ")
        if(t=='s'):
            return cal()
        else:
            print (" Bye Have a Good Day ! ")
    elif(option==4):
        c=a/b
        print(c)
        t=input("S to Reload & anything to Exit : ")
        if(t=='s'):
            return cal()
        else:
            print (" Bye Have a Good Day ! ")
    elif(option==5):
        c=a%b
        print(c)
        t=input("S to Reload & anything to Exit : ")
        if(t=='s'):
            return cal()
        else:
            print (" Bye Have a Good Day ! ")
    else:
        print(" Try Again ! ")
        return cal()
cal()


