'''1-Easy
https://leetcode.com/problems/two-sum/
найти индексы списка, которые дадут в сумме "таргет"
'''
# list_exe = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_exe = [3, 3]


# def two_sum_func(list_ex: list, target: int) -> list[int]:
#     for ct, el in enumerate(list_ex):
#         for elem in list_ex:
#             if ct == list_ex.index(elem):
#                 pass
#             else:
#                 answer = el + elem
#                 if answer == target:
#                     return ct, list_ex.index(elem)
#     return 'Нужные элементы не найдены'

# def two_sum_func(nums: list, target: int) -> list[int]:
#     for ct, el in enumerate(nums):
#         nums_2 = nums[ct:]
#         for elem in nums_2:
#             answer = el + elem
#             if answer == target:
#                 ans = ct, nums_2.index(elem) # пока нет решения как сделать так что бы он не брал индекс первого числа
#                 return ans

# def two_sum_func(nums: list, target: int) -> list[int]:
#     hash_dict = {}
#     for ct, el in enumerate(nums):
#         diff = target - el
#         if diff in hash_dict:
#             return [hash_dict[diff], ct]
#         else:
#             # hash_dict.update({el: ct})
#             hash_dict[el] = ct
#
#
# print(two_sum_func(list_exe, 6))

'''2-Easy
https://leetcode.com/problems/running-sum-of-1d-array/solution/
создать новый массив который в каждом новом элементе сложит предыдущие
'''
# def runningSum(nums: list[int]) -> list[int]:
#     out_list = []
#     prev_num = 0
#     for num in nums:
#         out_list.append(num + prev_num)
#         prev_num += num
#     return out_list
#
#
# def runningSum(nums: list[int]) -> list[int]:
#     for i in range(1, len(nums)):
#         nums[i] += nums[i - 1]
#     return nums
#
# from itertools import accumulate
# def runningSum(nums: list[int]) -> list[int]:
#     return list(accumulate(nums))

'''3-Easy
https://leetcode.com/problems/find-pivot-index/submissions/
'''
# def pivotIndex(nums: list[int]) -> int:
#     sum_nums = sum(nums)
#     for cnt, i in enumerate(nums):
#         left_sum = sum(nums[:cnt])
#         if sum_nums - left_sum - i == left_sum:
#             return cnt
#     return -1
#
# print(pivotIndex([2,1,-1]))

# def pivotIndex(nums: list[int]) -> int:
#     total_sum = sum(nums)
#     print(f"Total sum - {total_sum}")
#     left_sum = 0
#
#     for i, num in enumerate(nums):
#         if left_sum == (total_sum - left_sum - num):
#             return i
#         left_sum += num
#         print(f"Left sum is {left_sum}")
#         print(f"total_sum - left_sum - num = {(total_sum - left_sum - num)}")
#     return -1

# def pivotIndex(nums: list[int]) -> int:
#     total_sum = sum(nums)
#     left_sum = 0
#
#     for i, num in enumerate(nums):
#         if left_sum == (total_sum - left_sum - num):
#             return i
#         left_sum += num
#     return -1

'''4-Easy
https://leetcode.com/problems/isomorphic-strings
'''
# def isIsomorphic(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     else:
#         def num_list(incoming_string):
#             val_dict = {}
#             num = 0
#             val_list = []
#             for val in incoming_string:
#                 if val in val_dict:
#                     val_list.append(val_dict[val])
#                 else:
#                     val_dict[val] = num
#                     val_list.append(num)
#                     num += 1
#             return val_list
#         if num_list(s) == num_list(t):
#             return True
#         else:
#             return False
# print(isIsomorphic('foo', 'boo'))

# def isIsomorphic(s: str, t: str) -> bool:
#     str_dict = {}
#
#     if len(s) == 0 or len(t) == 0:
#         return False
#
#     for i in range(len(s)):
#         if s[i] not in str_dict:
#             if t[i] in str_dict.values():
#                 return False
#             str_dict[s[i]] = t[i]
#         else:
#             if str_dict[s[i]] != t[i]:
#                 return False
#     return True
#
# print(isIsomorphic('foo', 'boo'))

# def transformString(s: str) -> str:
#     index_mapping = {}
#     new_str = []
#
#     for i, c in enumerate(s):
#         if c not in index_mapping:
#             index_mapping[c] = i
#         new_str.append(str(index_mapping[c]))
#
#     return " ".join(new_str)
#
# def isIsomorphic(self, s: str, t: str) -> bool:
#     return self.transformString(s) == self.transformString(t)

'''5-Easy
https://leetcode.com/problems/is-subsequence/
'''
# s = "acb"
# t = "ahbgdc"
# def isSubsequence(s: str, t: str) -> bool:
#     t = list(t)
#     for i in s:
#         if i in t:
#             index = t.index(i)
#             del t[:index + 1]
#         else:
#             return False
#     return True
# print(isSubsequence(s, t))

'''6-Easy
https://leetcode.com/problems/merge-two-sorted-lists/
'''
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         head = list1
#         head2 = list2
#         head3 = ListNode()
#         node3 = head3
#         while head !=None and head2 != None:
#             if head.val > head2.val:
#                 node3.next = head2
#                 head2 = head2.next
#             else:
#                 node3.next = head
#                 head = head.next
#             node3 = node3.next
#         if head:
#             node3.next = head
#         if head2:
#             node3.next = head2
#         return head3.next

'''7-Easy
https://leetcode.com/problems/reverse-linked-list
'''
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node = head
#         prev = None
#         while node:
#             next_node = node.next
#             node.next = prev
#             prev = node
#             node = next_node
#         return prev

'''8-Easy
https://leetcode.com/problems/middle-of-the-linked-list/
'''
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node = head
#         cnt = 0
#         while node:
#             node = node.next
#             cnt+=1
#         cnt = cnt//2
#         cnt_2 = 0
#         node = head
#         while cnt_2 != cnt:
#             node = node.next
#             cnt_2+=1
#         print(cnt_2)

'''9-Middle
https://leetcode.com/problems/linked-list-cycle-ii/
'''
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None
#
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         node = head
#         s = set()
#         while node:
#             if node in s:
#                 return node
#             s.add(node)
#             if node.next == None:
#                 return node.next
#             node = node.next

'''10-Easy
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
'''
prices = [7,1,5,3,6,4]


def best_sell(prices):
    # low_price_dict = {}
    # high_price_dict = {}
    # first_start = True
    # for i in range(len(prices)):
    #     if first_start == True:
    #         low_price = prices[i]
    #         low_price_dict[i] = prices[i]
    #         first_start = False
    #     else:
    #         if low_price > prices[i]:
    #             low_price_dict[i] = prices[i]
    #             low_price = prices[i]
    #         else:
    #             high_price_dict[i] = prices[i]
    # result = []
    # for i in low_price_dict:
    #     for j in high_price_dict:
    #         if i < j and low_price_dict[i] < high_price_dict[j] :
    #             result.append(high_price_dict[j] - low_price_dict[i])
    # if result:
    #     print(max(result))
    # else:
    #     result = 0
    #     print(result)
    # return result
    price_dict = {}
    ft = True
    increase = False
    for i in range(len(prices)):
        if ft:
            low = prices[i]
            ft = False
        else:
            if increase == True:
                if prices[i] > max_price:
                    max_price = prices[i]
            elif prices[i] <= low:
                low = prices[i]
                increase = False
            else:
                max_price = prices[i]
                increase = True


best_sell(prices)
