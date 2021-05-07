from numpy import array

# python list has fixed shape and dynamic size
xs = [1, 2, 3]
ys = [4, 5, 6]
print(f'{xs + ys = }') #structure-wise, concstenation
print(f'{xs * 3 = }') # repetition

# np has contiguous machine typed integers
# dtype = windows:int32, unix/osX:int64
xt = array([1, 2, 3])
yt = array([4, 5, 6])
print(f'{xt.dtype = }') # element-wise
print(f'{xt * 3 = }') # element-wise

# np array has got dynamic shape and fixed size
print(f'{xt.__array_interface__["data"][0] = :#_x}') # shows particular memory
print(f'{xt.dtype = }') # looks it s bunch of 32 ints

# now you can take bloc of raw memory and tell numpy
# they r not int32 they r int8
# there is not 3 of them, the are actually 12 of them
xt.dtype = 'int8'
print(f'{xt =}')

# np array is a raw view of memory that gives you the
# abillity to mathematical types that can control those types
# that can perform no-dynamic dispatch on aggregated
# operations on machine-typed unboxed types of contiguous
# memory and it has an interpreter layer on top of it
# that gives you abillity to say what is the dtype
# of this and what is the shape and strides of this --
# so you can simply reshape and it is a free operation
print(f'{xt.reshape(2, 6) = }')