def shutdown(answer):
    check=input("Did you save & close all the apps?")
    if check =="yes":
        print("shutdown")
    elif check =="no":
        print("abort shutdown")
    else:
        print("sorry")        

check=input("Did you save & close all the apps?")
print(shutdown)    