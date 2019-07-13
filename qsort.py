import random


def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)


n = 5000
nums = [0] * n
for i in range(n):
    nums[i] = random.randint(0, 100000)


quicksort(nums)

for i in range(n):
    print(nums[i])