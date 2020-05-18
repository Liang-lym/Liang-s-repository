my_dict={'0':'ling','1':'yi','2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu','-':'fu'}
s=input()
s=s.strip()
for i in s[0:-1]:    
    print(my_dict[i],end=' ')
print(my_dict[s[-1]])
