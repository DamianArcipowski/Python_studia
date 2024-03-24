import numpy as np

a = np.array([0, 1])
print(a)

a = np.arange(2)
print(a)
print(type(a))

print(a.dtype)

a = np.arange(2, dtype='int32')
print(a.dtype)

b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)

print(a.ndim)

m = np.array((np.arange(2), np.arange(2)))
print(m)
print(m.shape)
print(m.ndim)

matrix = np.array([[1, 2], [5, 4], [5, 6]])
print(matrix)
print(matrix.dtype)
print(matrix.ndim)

zeros_arr = np.zeros((5, 5))
ones_arr = np.ones((4, 4))
print(zeros_arr)
print(ones_arr)
print(zeros_arr.dtype)
print(ones_arr.dtype)

empty_arr = np.empty((2, 2))
print(empty_arr)
pos_1 = empty_arr[1, 1]
pos_2 = empty_arr[0, 1]
print(pos_1)
print(pos_2)

matrix = np.array([[1, 2], [3, 4]])
print(matrix)
my_numbers = np.arange(1, 2, 0.1)
print(my_numbers)

numbers_lin = np.linspace(1, 2, 5, endpoint=False)
print(numbers_lin)

z = np.indices((5, 3))
print(z)

x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

diag_matrix = np.diag([a for a in range(5)], k=1)
print(diag_matrix)

z = np.fromiter(range(5), dtype='int32')
print(z)

chars = b'abcdef' # b is to pass bytes
ch1 = np.frombuffer(chars, dtype='S2')
print(ch1)
ch2 = np.frombuffer(chars, dtype='S3')
print(ch2)

chars = 'abcdef'
ch3 = np.array(list(chars))
ch4 = np.array(list(chars), dtype='S1')
ch5 = np.array(list(b'abcdef'))
ch6 = np.fromiter(chars, dtype='S1')
ch7 = np.fromiter(chars, dtype='U1')
print(ch3)
print(ch4)
print(ch5)
print(ch6)
print(ch7)

mat = np.ones((2, 2))
mat_2 = np.ones((2, 2))
mat = mat + mat_2
print(mat)
print(mat - mat_2)
mat_2 = np.array(([3, 4], [5, 6]))
print(mat * mat_2)
print(mat / mat_2)

a = np.dot(mat, mat_2)
print(a)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
print(a[2:7:2])
print(a[1:])
print(a[1:5])

mat = np.arange(25)

mat = mat.reshape((5, 5))

print(mat[1:])
print(mat[:1])
print(mat[:, -1:])
print(mat[2:6, 1:3])
print(mat[:, range(2, 6, 2)])

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)