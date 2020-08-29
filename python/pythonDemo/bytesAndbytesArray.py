lst=[10,20,30,40]

b= bytes(lst)
print(b)
print(type(b))

b1= bytearray(lst)
print(b1)
print(type(b1))
# item assignment not supported by bytes 
# no slicing or repetition is allowed on either bytes or bytearray
# b[2] =33
b1[3]=44

