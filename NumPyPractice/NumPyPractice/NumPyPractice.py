import numpy as np
import matplotlib.pyplot as plt
import random
def main():
    """
    data = np.array([[1,2,3], 
                     [4,5,7], 
                     [7,8,9]])
    print(data[:2]) # [1,2,3], [4,5,7]
    print(data[:2, :2]) # [1,2], [4,5]
    print(data[:2, 1:]) # [2,3], [5,7]
    print(data[1:, 1:]) # [5,7], [8,9]
    data1 = np.array([[[1,2,3], 
                       [4,5,7], 
                       [7,8,9]], 
                      
                      [[10,11,12], 
                       [13,14,15], 
                       [15,16,17]]])
    print(data1[:1, :2, :1]) # [1], [4]
    print(data1[1:, 1:, 1:]) # [14, 15], [16, 17]
    # Sums in 1D array
    print(data.sum(axis = 0)) # [12 15 19]
    print(data.sum(axis = 1)) # [6 16 24]
    # Sums in 2D array
    print(data1.sum(axis = 0)) # [11 13 15], [17 19 22], [22 24 26]
    print(data1.sum(axis = 1)) # [12 15 19], [38 41 44]
    print(data1.sum(axis = 2)) # [6 16 24], [33 42 48]
    matrix = []
    x = np.random.randn(8)
    y = np.random.randn(8)
    print(x)
    print(y)
    print(np.maximum(x,y))    
    arr = np.random.rand(7) * 5
    print(arr)
    print(np.modf(arr))
    points = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(points, points)
    print(xs)
    print(ys)
    z = np.sqrt(xs ** 2 + ys ** 2)
    print(z)
    plt.imshow(z, cmap = plt.cm.gray)
    plt.colorbar()
    plt.show()
    arr = np.arange(16).reshape((2,2,4))
    print(arr)
    print(arr.transpose((0,2,1)))
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])
    result = np.where(cond, xarr, yarr)
    print(result)
    arr = np.random.rand(5,4)
    print(arr)
    print(arr.mean())
    print(np.mean(arr))
    print(arr.sum())
    """
    ints = np.array([3, 3, 3, 2, 2, 1, 1, 4])
    print(np.in1d(ints, [1, 3, 5]))
    """
    nsteps = 1000
    draws = np.random.randint(0, 2, size = nsteps)
    steps = np.where(draws > 0, 1, -1)
    walk = steps.cumsum()
    x = np.arange(1000)
    plt.plot(x, walk)
    plt.show()
    """
if __name__ == "__main__":
    main()
