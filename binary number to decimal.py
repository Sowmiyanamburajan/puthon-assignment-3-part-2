num=int(input("enter any binary number:"))
sum=0
i=0
while num!=0:
      rem=num%10
      sum=sum+rem*(2**i)
      num=num//10
      i=i+1
print("decimal value",sum)
