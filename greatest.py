a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if(a>b):
    if(a>c):
        print(f"the largest no is:{a}")
    else:
        print(f"the largest no is:{c}")
else:
    if(b>c):
        print(f"the largest no is:{b}")
    else:
        print(f"the largest no is :{c}")

 
if(a<b):
    if(a<c):
        print(f"the smallest no is:{a}")
    else:
        print(f"the smallest no is:{c}")
else:
    if(b<c):
        print(f"the smallest no is:{b}")
    else:
        print(f"the smallest no is:{c}") 