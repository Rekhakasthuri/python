import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
print (" OUTPUT IS ")
print("ONE DIMENSIONAL ARRAY IS:\n",a)
b=np.array([[10,20],[40,50]])
print (" TWO DIMENSIONAL ARRAY IS:\n",b)
c=np.array([[10,20,30],[40,50,60],[70,80,90]])
print (" THREE DIMENSIONAL ARRAY IS:\n", c)
#array indexing and numpy array atributes
x1 = np.array([45,89,64,33])
x2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Array indexing and numpy array atributes")
print(x1)
print("x2 ndim:",x2.ndim)
print("x2 shape:",x2.shape)
print("x2 size:",x2.size)

#accessing single elements
print("accessing single elements")
print(x1[-2])
print(x2)
x2[1,2] = 60
print(x2)

#array slicing
print("array slicing")
x = np.arange(10)
print(x[5:9])
print(x[:5])
print(x[1::3])
print(x2)
print(x2[0:2,0:2])

#concatenation of arrays
print("concatenation of arrays")
p = np.array([1,2,3])
q = np.array([8,12,14])
print(np.concatenate([p,q]))

#splitting of array
print("splitting of array")
y = [1,2,3,99,99,3,2,1]
d,e = np.split(x,[2])
print(d,e)

#Functions
print("Function:")
print("add")
t = np.array([1,2,3])
print(np.add(t,2))
print("Subtract")
print(np.subtract(t,2))
print("negative")
print(np.negative(t))
print("multiply")
print(np.multiply(t,2))
print("divide")
print(np.divide(t,5))
print("floor divide")
print(np.floor_divide(t,2))
print("power")
print(np.power(t,2))
print("modulus")
print(np.mod(t,2))

#absloute
print("Absolute")
print(np.absolute([-1,-2,0,1,2]))

#Trigonometric
print("trignometric")
theta = [0,1.57,3.14]
print(np.sin(theta))
print(np.cos(theta))
print(np.tan(theta))

#exponent
print("Exponent")
print(np.exp(x))
print(np.exp2(x))
print(np.power(x,3))

print("Log")
o = [1,10,100]
print(np.log(o))
print(np.log2(o))
print(np.log10(o))
