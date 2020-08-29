s="    you are awesome   "
a='how are you'
d='ASASAS'
print(s)

print(type(s))

s1 = '''  you are true 
you are beauty
you are good'''

print(s1)

print(type(s1))

print(s[0])

print(s*3)
print(len(s1))

print('###################################################')
# Slicing of string

print(s[0:5])

print(s[0:])

print(s[:9])

print(s[:-1])

print(s[-1:])

print(s[-4:-1])

print('###################################################')
# Steps in slicing

print(s[::-1])

print(s[4::-1])

print(' Stripping the string   :###################################################')

print(s.strip())

print('Left Strip=***',s.lstrip(),'***')

print('Right strip=****' , s.rstrip(),'***')

print('##########################  : Some more String functions')

print(s.find('awe',2,-1))

print(s.count('a'))
print(s.replace('awesome','super'))
print(s.endswith('asa'))
print(a.capitalize())
print(a.title())
print(a.upper())
print(d.lower())