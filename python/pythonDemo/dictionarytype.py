dict={1:'nik', 2:"john" , 3: 'bob'}

i=dict.items()

for j in i:
    print(j)
    
k= dict.keys()
for o in k:
    print(o)
    
print(dict)

del dict[2]

print(dict)