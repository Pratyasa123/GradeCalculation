n=int(input("input no. of weights"))
su=0 
wesu=0
for i in [1,n+1]:
    a=int(input("input the numeric value"))
    b=int(input("input the weight"))
    su=su+(a*b)
    wesu=wesu+b
grade=su/wesu   
print("grade is ",grade)
