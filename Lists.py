nums=[1,4,6,2,5]
>>> nums[2]
6
>>> nums[2:]
[6, 2, 5]
>>> nums[-1]
5



names=['AB','CD','EF']



values=[9.5,'ABC',25]

mil=[nums,names]
>>> mil
[[1, 4, 6, 2, 5], ['AB', 'CD', 'EF']]


#Lists are mutable
>>> nums.append(45)
>>> nums
[1, 4, 6, 2, 5, 45]
>>> mil
[[1, 4, 6, 2, 5, 45], ['AB', 'CD', 'EF']]

>>> nums
[1, 4, 6, 2, 5, 45]
>>> mil
[[1, 4, 6, 2, 5, 45], ['AB', 'CD', 'EF']]
>>> nums.insert(2,27)
>>> nums
[1, 4, 27, 6, 2, 5, 45]
>>> nums.remove(2)
>>> nums.pop(1)
4
>>> nums
[1, 27, 6, 5, 45]
>>> nums.pop()
45
>>> nums
[1, 27, 6, 5]

>>> del nums[3:]
>>> nums
[1, 27, 6]
>>> nums.extend([9,7,8,3])
>>> nums
[1, 27, 6, 9, 7, 8, 3]


>>> min(nums)
1
>>> max(nums)
27
>>> sum(nums)
61

>>> nums
[1, 27, 6, 9, 7, 8, 3]
>>> nums.sort()
>>> nums
[1, 3, 6, 7, 8, 9, 27]