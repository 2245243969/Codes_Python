import numpy as ny
#创建一个列表list1,包含0-11之间的整数
list1=list(range(0,12,1))
print(list1)
print('\n')

#创建一个一维数组arr1,包含0-11之间的整数，打印shape,size,dtype属性
arr1=ny.arange(0,12,1)
print(arr1.shape,arr1.size,arr1.dtype)
print('\n')

#修改一维数组arr1的形状，将其转换为2行6列的多维数组
arr1.shape=2,6
print(arr1)
print('\n')

#创建一个2行6列的多为实数类型数组arr2,包含0-11之间的实数
arr2=ny.arange(0,12,1)
arr2.shape=2,6
arr2=arr2.astype(float)
print(arr2)
print(arr2.shape,arr2.size,arr2.dtype)
print('\n')

#将arr1的数据转换成列表list2
list2=arr1.tolist()
print(list2)