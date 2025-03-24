#Esse for i em x, é pra fazer ele percorer o os "i" em x, depois que atribuo alguma condição como um if 

x = [1,2,3,4]
y = []
j = []
for i in x:
    y.append(i**2)
print(y)
#----------------
w = [i**2 for i in x]
print(w)
#-------------
for i in x:
    if i % 2 == 0:
        j.append(i)
#-------
j = [1 for i in x if i % 2 == 0]
print()