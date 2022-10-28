numbers=[]

while True:
    ans=input("Number: ")
    if ans=="-1":
        break
    else:
        numbers.append(float(ans))

print(sum(numbers)/len(numbers))
    


