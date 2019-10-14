                                                         


S = "a"
S1 = "aAs"
A = "bs"
S3=S1

List = ['a','b','a','a','b','a','a']

length = len(List)
print ("total no.of output string:"" "+str(length))

#p = input("enter your choice : 1] LEFT 2] RIGHT")

#print(length)

print("Left most tree")

print("\t"+'[''a','A','s'']')

S1 = [sub.replace('A', 'bs') for sub in S1]
print (S1)


S1 = [sub.replace('bs', 'ba') for sub in S1]
print (S1)

S1 = [sub.replace('s', 'aAs') for sub in S1]
print (S1)

S1 = [sub.replace('aAs', 'abss') for sub in S1]
print (S1)

S1 = [sub.replace('abss', 'abas') for sub in S1]
print (S1)

S1 = [sub.replace('abas', 'abaa') for sub in S1]
print (List)

#S2=len(S1)
#print(S2)


print("Right most ")

print("\t"+'[''a','A','s'']')

S3 = [sub.replace('s', 'aAs ') for sub in S3]
print (S3)


S3 = [sub.replace('aAs', 'aAa') for sub in S3]
print (S3)

S3 = [sub.replace('aAa', 'absa') for sub in S3]
print (S3)

S3 = [sub.replace('absa', 'abaa') for sub in S3]
print (S3)

S3 = [sub.replace('A', 'abs') for sub in S3]
print (S3)

S3 = [sub.replace('abs', 'aba') for sub in S3]
print (S3)
print(List)







    