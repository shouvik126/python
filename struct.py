from struct import *
#to convert to byte code
packed_data=pack('iif',5,6,7.8)
print(packed_data)
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

#to convert back in to original form

original_data=unpack('iif',packed_data)
print(original_data)
