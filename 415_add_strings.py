# def additon(diff):
#     str = list(b)
#     for i in range(diff):
#         str.insert(0, '0')
#     return ''.join(str)
#
# def add(b1,c):
#     y = 0
#     for i, j in zip(reversed(b1), reversed(c)):
#         sum = int(i) + int(j) + y
#         if sum >= 10:
#             sum %= 10
#             k.append(sum)
#             y = 1
#         else:
#             k.append(sum)
#             y = 0
#     if y == 1:
#         k.append(y)
#     for i in reversed(k):
#         print(i, end='')
#     print('\n')
#
#
# a = int(input())
# if a<=20 and a>=1:
#     n = 1
#     while n<=a:
#         b,c = input().split()
#         print(f"case:{n}")
#         k = []
#         if len(b)<len(c):
#             b1 = additon(len(c) - len(b))
#             add(b1,c)
#         elif len(b)>len(c):
#             b,c = c,b
#             b1 = additon(len(c) - len(b))
#             add(b1,c)
#         else:
#             add(b,c)
#         n += 1
# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         y = 0
#         k = []
#         add = ''
#         while len(num1)>len(num2):
#             num2 = '0' + num2
#         while len(num2) > len(num1):
#             num1 = '0' + num1
#         for i,j in zip(reversed(num1),reversed(num2)):
#             sum = int(i) + int(j) + y
#             if sum >= 10:
#                 sum %= 10
#                 k.append(sum)
#                 y = 1
#             else:
#                 k.append(sum)
#                 y = 0
#         if y == 1:
#             k.append(y)
#         print(k)
#         for i in k:
#             add = str(i) + add
#         return add
# t = Solution()
# a,b = input().split()
# print(t.addStrings(a,b))


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        y = 0
        add = ''
        i,j = len(num1)-1, len(num2) - 1
        while i>=0 or j>=0:
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            sum = n1 + n2 + y
            y = sum // 10
            tem = sum % 10
            add = str(tem) + add
            i,j = i-1,j-1
        return '1' + add if y else add
        # while len(num1)>len(num2):
        #     num2 = '0' + num2
        # while len(num2) > len(num1):
        #     num1 = '0' + num1
        # for i,j in zip(reversed(num1),reversed(num2)):
        #     sum = int(i) + int(j) + y
        #     if sum >= 10:
        #         sum %= 10
        #         add = str(sum) + add
        #         y = 1
        #     else:
        #         add = str(sum) + add
        #         y = 0
        # if y == 1:
        #     k.append(y)
        # print(k)
        # for i in k:
        #     add = str(i) + add
        # return add

t = Solution()
a,b = input().split()
print(t.addStrings(a,b))