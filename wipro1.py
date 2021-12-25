# from collections import Counter
# X = int(input())
# lis = list(map(int, input().split()))
# lis.sort()
# lis = Counter(lis)
# print(len(lis))
# print(*lis)

######
# X = int(input())
# lis = list(map(int, input().split()))
# for i in range(1, len(lis)):
#     print(i)
#     if lis[i-1] > lis[i]:
#         lis[i-1] -= 1
#         break
# print(lis)
# for i in range(1, len(lis)):
#     if lis[i-1] > lis[i]:
#         print("No")
#         break
# else:
#     print("Yes")

# X = int(input())
# lis = list(map(int, input().split()))
# mat = []
# for i in range(0, len(lis)):
#     if i % 2 == 0:
#         mat.insert(0, lis[i])
#     else:
#         mat.append(lis[i])
# if len(lis) % 2 == 0:
#     mat.reverse()
# print(*mat)


# num1 = int(input())
# num2 = int(input())
# if(num1 > num2 ):
#     max= num1
# else:
#     max= num2
# while(True):
#     if(max % num1 == 0 and max % num2 == 0):
#         print(max)
#         break
#     max= max+ 1

# X = int(input())
# lis = list(map(int, input().split()))
# flag = 0
# for i in range(1, len(lis)):
#     print(lis[i-1]-1, lis[i])
#     if lis[i-1] - lis[i]+1 < 0:
#         flag = 1
# if flag == 0:
#     print("No")
# else:
#     print("Yes")

# def difference(h1, m1, h2, m2):
#     t1 = h1 * 60 + m1
#     t2 = h2 * 60 + m2
#     if (t1 == t2):
#         return 0
#     else:
#         diff = t2-t1
#     h = (int(diff / 60)) % 24
#     m = diff % 60
#     return h*60 + m


# def solution(A, B):
#     hr1, min1 = A.split(":")
#     hr2, min2 = B.split(":")
#     cuts = ["00", "15", "30", "45"]
#     if min1 not in cuts:
#         if int(min1) // 15 < 3:
#             min1 = cuts[int(min1) // 15+1]
#         else:
#             min1 = "00"
#             hr1 = str(int(hr1)+1)

#     if min2 not in cuts:
#         if int(min2) // 15 <= 3:
#             min2 = cuts[int(min2) // 15]
#     print(int(hr1), int(min1), int(hr2), int(min2))
#     dif = difference(int(hr1), int(min1), int(hr2), int(min2))
#     return dif//15


# solution("12:03", "12:03")


# def differencesum(n, m):
#     suma = 0
#     sumb = 0
#     for i in range(1, m+1):
#         if i % n == 0:
#             suma += i
#         else:
#             sumb += i
#     return sumb-suma


# differencesum(4, 20)

# countinuouss sum set
# def solve(A, B):
#     s = sum(B)
#     if s % 3 != 0:
#         return 0

#     lis = [0 for i in range(A)]
#     s //= 3
#     ss = 0
#     for i in range(A-1, -1, -1):
#         ss += B[i]
#         if (ss == s):
#             lis[i] = 1
#     print(lis)
#     for i in range(A - 2, -1, -1):
#         lis[i] += lis[i + 1]
#     print(lis)
#     ans = 0
#     ss = 0
#     for i in range(0, A - 2):
#         ss += B[i]
#         if (ss == s):
#             ans += lis[i + 2]
#     return ans


# A = 5
# B = [1, 2, 3, 0, 3]
# print(solve(A, B))

# a = 'bubble'
# for i in range(len(a)):
#     a[i].upper()

# a = "sherlock"
# print(a.__getitem__(3))

# l = [3, 4, 2]
# l.sort(reverse=False)
# print(l)
# class change:
#     def __init__(self,x,y):
#         self.a = x+y+z

# x = change(1,3,5)
# y = getattr(x,'a')
# setattr()

# class test:
#     def __init__(self):
#         self.vari = "tt"
#         self.c(self.vari)

#     def c(self, var):
#         var = 'fd'


# obj = test()
# print(obj.vari)

# num = int(input())
# order = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10
# result_e, result_o = 0, 0
# for n in str(num):
#     if int(n) % 2 == 0:
#         result_e += int(n)
#     else:
#         result_o += int(n)
# if num == sum:
#     print(result_e)
# else:
#     print(result_o)

# import collections
# X = int(input())
# lis = list(map(int, input().split()))
# lis.sort(reverse=True)
# prev = -92982838
# count = 0
# for i in lis:
#     if prev != lis[i]:
#         count = 0
#     count += 1
#     if count == lis[i] and lis[i+1] != lis[i]:
#         result = lis[i]
#         print(result)
#         break

# x = int(input())
# lis = list(map(int, input().split()))
# pt = list(map(int, input().split()))
# result = []
# for i in range(pt[0]):
#     result.append(lis[i])
# for i in range(pt[1], pt[0]-1, -1):
#     result.append(lis[i])
# for i in range(pt[1]+1, len(lis)):
#     result.append(lis[i])
# print(*result)

# x = int(input())
# a = 0
# b = 1
# ans = 1
# if x == 1:
#     print(0)
# elif x == 1:
#     print(1)
# else:
#     for i in range(2, x):
#         c = a+b
#         a = b
#         b = c
#         ans += c

#     print(ans)


# result = 0
# for m in lis:
#     if round(m**(1/3))**3 == m:
#         result += 1

# print(result)

# import sys

# N = list(map(int, input().split()))
# result = [sys.maxsize for i in range(N[1])]
# for i in range(N[0]):
#     for j, x in enumerate(list(map(int, input().split()))):
#         if result[j] > x:
#             result[j] = x

# print(*result)

# import collections
# lis = list(input().split())
# x = int(input())
# d = dict(collections.Counter(lis))
# result = []
# for key, value in d.items():
#     if value >= x:
#         result.append(key)

# if len(result) == 0:
#     print("NA")
# print(*result)

# how many sentence:
# import collections


# def howManyS(word, sent):
#     anagram = []
#     count = 0
#     result = 1
#     for wor in word:
#         d = dict(collections.Counter(wor))
#         anagram.append(d)
#     for s in sent:
#         for s1 in s:
#             d = dict(collections.Counter(s1))
#             for an in anagram:
#                 if an == d:
#                     count += 1
#             result *= count
#             count = 0
#         print(result)
#         result = 1


# # all input system
# x = int(input())
# word = []
# for i in range(x):
#     word.append(input())
# y = int(input())
# sent = []
# for i in range(y):
#     sent.append(list(input().split()))
# # all input system
# # call def
# howManyS(word, sent)

# the largest string
import collections
from typing import Pattern


# def largestString(string, K):
#     d = dict(collections.Counter(string))
#     wordList = sorted(d.keys(), reverse=True)
#     result = ""
#     i = 0
#     j = 1
#     while(i != len(wordList) and j != len(wordList)):
#         if d[wordList[i]] > K:
#             result += str(wordList[i])*K
#             d[wordList[i]] -= K
#         else:
#             result += str(wordList[i])*d[wordList[i]]
#             d[wordList[i]] = 0


#     print(result)

#    # inputs
# string = input()
# K = int(input())
# largestString(string, K)

# # string reduction
# import collections


# def minDel(string):
#     d = dict(collections.Counter(string))
#     result = 0
#     for key, value in d.items():
#         if value > 1:
#             result += value-1
#     print(result)

# # input
# string = input()
# minDel(string)


#sign in out
# def processLogs(logs, K):
#     d = {"A": 5}
#     result = []
#     logs.sort()
#     for log in logs:
#         id, time, sign = log.split()
#         if sign == "sign-in":
#             d[id] = int(time)
#     for log in logs:
#         id, time, sign = log.split()
#         if sign == "sign-out" and id in d.keys():
#             if K >= int(time) - d[id]:
#                 result.append(int(id))
#     result.sort()
#     result = map(str, result)
#     return result


# print(processLogs(["100 15 sign-out", "99 1 sign-in", "100 10 sign-in", "50 20 sign-in",
#                    "50 26 sign-out", "99 2 sign-out"], 5))


# maximum sum

# for test in range(int(input())):
#     X = int(input())
#     lis = list(map(int, input().split()))
#     result = 0
#     temp = lis[-1]
#     for i in range(X-1, -1, -1):
#         if lis[i] > temp:
#             result += temp
#         else:
#             result += lis[i]
#             temp = lis[i]
#     print(result)


# table of content
# def tableOfContents(text):
#     result = []
#     chapter = 0
#     topic = 1
#     for sent in text:
#         if sent.startswith("## "):
#             result.append(str(chapter)+"."+str(topic)+"."+sent[2:])
#             topic += 1
#         if sent.startswith("# "):
#             chapter += 1
#             topic = 1
#             result.append(str(chapter)+"."+sent[1:])
#     return result


# text = ['# Games',
#         '## Board',
#         '## Computer',
#         '## Zero sum',
#         '## Multiplayer',
#         '# Strategies',
#         '## Greedy',
#         '## Tree pruning',
#         '## Others',
#         '# Summary']
# result = tableOfContents(text)
# for r in result:
#     print(r)

# disk space analysis

# import sys


# def segment(x, space):
#     if x == 1:
#         return max(space)
#     elif x > len(space):
#         return min(space)
#     else:
#         return max(min(space[:x]), max(space[x:len(space)-x]), min(space[len(space)-x:]))


# print(segment(4, [1, 2, 3, 5, 4]))

# even subarray
# def nc(x):
#     return len(x)


# def evenSubarray(k, array):
#     result = []
#     for i in range(len(array) + 1):
#         for j in range(i):
#             count = 0
#             for x in array[j: i]:
#                 if x % 2 != 0:
#                     count += 1
#                 if count > k:
#                     break
#             if count <= k:
#                 result.append(array[j: i])
#     result.sort(key=nc)
#     return result


# print(evenSubarray(1, [1, 2, 3, 4]))


# def findBeforeMatrix(after):
#     m = len(after)
#     n = len(after[0])
#     for i in range(m-1, -1, -1):
#         for j in range(n-1, 0, -1):
#             after[i][j] -= after[i][j-1]

#     for i in range(m-1, 0, -1):
#         for j in range(n-1, -1, -1):
#             after[i][j] -= after[i-1][j]

#     return after


# after = [[2, 1], [5, 4]]
# print(findBeforeMatrix(after))


# import collections
# lis = []
# for test in range(int(input())):
#     lis.append(input())
# lis = reversed(sorted(lis))
# x = dict(collections.Counter(lis))
# d = dict(reversed(sorted(x.items(), key=lambda item: item[1])))
# print(len(d))
# for i in d:
#     print(i)


# import math

# def LCA(n, m):
#     if (n > m):
#         n, m = m, n
#     a = int(math.log2(n))
#     b = int(math.log2(m))

#     while (n != m):
#         if (n < m):
#             m = m >> 1
#         if (n > m):
#             n = n >> 1

#     v = int(math.log2(n))
#     return a + b - 2 * v


# for test in range(int(input())):
#     lis = list(input().split())
#     print(LCA(int(lis[0]), int(lis[1])))


# Python Program to detect cycle in an undirected graph


# from collections import defaultdict


# class Graph:

#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = defaultdict(list)

#     def addEdge(self, v, w):
#         self.graph[v].append(w)
#         self.graph[w].append(v)

#     def isCyclicUtil(self, v, visited, parent):
#         visited[v] = True
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 if(self.isCyclicUtil(i, visited, v)):
#                     return True
#             elif parent != i:
#                 return True
#         return False

#     def isCyclic(self):
#         visited = [False]*(self.V)
#         for i in range(self.V):
#             if visited[i] == False:
#                 if(self.isCyclicUtil
#                         (i, visited, -1)) == True:
#                     return True
#         return False


# for test in range(int(input())):
#     N, M = input().split()
#     g = Graph(int(M))
#     lis = list(map(int, input().split()))
#     index = 0
#     for i in range(int(M)):
#         g.addEdge(lis[index], lis[index+1])
#         index += 2

#     if g.isCyclic():
#         print("1")
#     else:
#         print("0")


# def solve(A, B):
#     union = [None for _ in range(A+1)]

#     def unionFind(node):
#         if not union[node]:
#             return node
#         union[node] = unionFind(union[node])
#         return union[node]

#     for x, y in B:
#         parentX = unionFind(x)
#         parentY = unionFind(y)
#         if parentX == parentY:
#             return 1
#         else:
#             union[parentX] = parentY

#     return 0

# lcs count
# def count(a, b):
#     m = len(a)
#     n = len(b)

#     # Create a table to store results of sub-problems
#     lookup = [[0] * (n + 1) for i in range(m + 1)]

#     # If first string is empty
#     for i in range(n+1):
#         lookup[0][i] = 0

#     # If second string is empty
#     for i in range(m + 1):
#         lookup[i][0] = 1

#     # Fill lookup[][] in bottom up manner
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):

#             # If last characters are same,
#             # we have two options -
#             # 1. consider last characters of
#             # both strings in solution
#             # 2. ignore last character of first string
#             if a[i - 1] == b[j - 1]:
#                 lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]

#             else:
#                 # If last character are different, ignore
#                 # last character of first string
#                 lookup[i][j] = lookup[i - 1][j]

#     return lookup[m][n]

# # Driver code
# if __name__ == '__main__':
#     a = "GeeksforGeeks"
#     b = "Gks"


# for test in range(int(input())):
#     X, N, M = input().split()
#     print(count(a, b))


# from math import sqrt

# # Function calculates distance
# # between two points


# def maxTime(cls, input1, input2, input3):

#     n = len(input3)
#     maxm = 0
#     for i in range(n):
#         for j in range(i + 1, n):6

#             # Update maxm
#             x0 = input3[i][0] - input3[j][0]
#             y0 = input3[i][1] - input3[j][1]
#             maxm = max(maxm, x0 * x0 + y0 * y0)

#     return round(sqrt(maxm)/input1, 6)

# # Driver Code


# print(maxTime(2, 3, [[0, 0], [0, 2], [2, 0]]))


# def isPrime(num):
#     if num > 1:
#        # check for factors
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return i
#         else:
#             return 1


# # if input number is less than
# # or equal to
# print(isPrime())

# def doubleSize(arr, b):
#     for i in arr:
#         if i == b:
#             b = b*2
#     return b


# print(doubleSize([1, 2, 4, 11, 12, 8], 2))

# regd = r"^([a-b]).*\1$|^[a-b]{1}$"
# pattern = compile(regd)

# q = int(input())


# for i in range(q):
#     s = input()
#     if pattern.match(s):
#         print("true")

# def performOperations(arr, opertaions):
#     for item in opertaions:
#         i, j = item[0], item[1]
#         arr[i:j+1] = arr[i:j+1][::-1]

#     return arr


# print(performOperations([1, 2, 3], [[0, 2], [1, 2], [0, 2]]))

# from collections import defaultdict

# # Sort by Frequency


# def sortByFreq(arr, n):
#     d = defaultdict(lambda: 0)
#     result = []
#     for i in range(n):
#         d[arr[i]] += 1

#     arr.sort(key=lambda x: (-d[x], x))
#     temp = arr[0]
#     for i in range(1

#     return (arr)


# if __name__ == "__main__":
#     arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
#     n = len(arr)
#     solution = sortByFreq(arr, n)
#     print(*solution)

# def numberOfConnections(gridOfNodes):
#     result = 0
#     temp = 0
#     for grid in gridOfNodes:
#         length = grid.count(1)
#         result += temp * length
#         if length != 0:
#             temp = length
#     return result


# print(numberOfConnections(
#     [[1, 0, 1, 1], [0, 1, 1, 0], [0, 0, 0, 0], [1, 0, 0, 0]]))


# def sub(s):
#     s = s[::-1]
#     s = list(s)
#     for i in range(len(s)):
#         if s[i] == "A":
#             s[i] = "T"
#         elif s[i] == "T":
#             s[i] = "A"
#         elif s[i] == "G":
#             s[i] = "C"
#         elif s[i] == "C":
#             s[i] = "G"
#     return "".join(s)
# print(sub("TTTTGCACAA"))


# def binarySearch(nums, target):
#         start ,end = 0,len(nums)-1
#         while start <= end:
#             mid = start + (end- start)//2
#             if target < nums[mid]:
#                 end = mid-1
#             elif target > nums[mid]:
#                 start = mid+1
#             elif target == nums[mid]:
#                 return mid

#         return -1

# def searchInsert(self, nums: List[int], target: int) -> int:
#         start , end  = 0 , len(nums)-1
#         while start < end:
#             mid =  start +(end-start)//2
#             if nums[mid] == target:
#                 return  mid
#             elif target < nums[mid]:
#                 end= mid-1
#             else:
#                 start = mid+1

#         if nums[start]>=target:
#             return start
#         else:
#             return  start+1

# def sortedSquares(self, nums: List[int]) -> List[int]:
#     start,end = 0,len(nums)-1
#     lis = []
#     while start <= end:
#         if abs(nums[start]) >= abs(nums[end]):
#             lis.insert(0,nums[start]*nums[start])
#             start+=1
#         else:
#             lis.insert(0,nums[end]*nums[end])
#             end-=1
#     return lis

# def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#     result = []
#     intervals.sort(key = lambda x: x[0])
#     for i in intervals:
#         if len(result) == 0 or result[-1][1] < i[0]:
#             result.append(i)
#         else:
#             result[-1][1] = max(result[-1][1],i[1])
#     return result

# def twoSum(self, numbers: List[int], target: int) -> List[int]:
#     diff = {}
#     for i,num in enumerate(numbers):
#         if diff.get(num) != None:
#             return [diff[num],i+1]
#         else:
#             diff[target- num] = i+1

# def moveZeroes(self, nums: List[int]) -> None:
#     count = 0
#     length  = len(nums)
#     for i in range(0,length):
#         while nums[i] == 0:
#             nums.insert(length,nums.pop(i))
#             count+=1
#             if count > length-i+1:
#                 break

# def lengthOfLongestSubstring(self, s: str) -> int:
#     l = 0
#     result = 0
#     charset = set()
#     for r in range(len(s)):
#         print(charset)
#         while s[r] in charset:
#             charset.remove(s[l])
#             l+=1
#         charset.add(s[r])
#         result = max(result,r-l+1)
#     return result


# def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#     mid = (len(nums1)+len(nums2))//2
#     cur1,cur2 = 0,0
#     x,y = 0,0
#     while True:
#         if cur1 <len(nums1) and cur2 <len(nums2):
#             if nums1[cur1] <nums2[cur2]:
#                 x,y =y,nums1[cur1]
#                 cur1+=1
#             else:
#                 x,y =y,nums2[cur2]
#                 cur2+=1
#         elif cur1 <len(nums1):
#             x,y =y,nums1[cur1]
#             cur1 +=1
#         elif cur2 <len(nums2):
#             x,y =y,nums2[cur2]
#             cur2 +=1

#         if cur1 +cur2 > mid:
#             if (len(nums1)+len(nums2)) % 2 == 0:
#                 return (x+y)/2
#             else:
#                 return y
