from typing import List, Optional
from collections import Counter, deque


# Task 1: Two Sum
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Task 2: First Unique Character
def firstUniqChar(s: str) -> int:
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
    return -1


# Task 3: Isomorphic Strings
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    map_s_to_t = {}
    map_t_to_s = {}

    for ch_s, ch_t in zip(s, t):
        if (ch_s in map_s_to_t and map_s_to_t[ch_s] != ch_t) or \
                (ch_t in map_t_to_s and map_t_to_s[ch_t] != ch_s):
            return False
        map_s_to_t[ch_s] = ch_t
        map_t_to_s[ch_t] = ch_s
    return True


# Task 4: Happy Number
def isHappy(n: int) -> bool:

    def sum_of_squares(num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squares(n)
    return n == 1


# Task 5: Binary Tree Level Order Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:

    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result


# Task 6: Maximum Depth of Binary Tree
def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# Task 7: Symmetric Tree
def isSymmetric(root: Optional[TreeNode]) -> bool:

    def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and \
            isMirror(left.left, right.right) and \
            isMirror(left.right, right.left)

    return isMirror(root, root)


# Task 8: Longest Consecutive Sequence Path
def longestConsecutive(root: Optional[TreeNode]) -> int:

    def dfs(node: Optional[TreeNode], parent_val: int, length: int) -> int:
        if not node:
            return length

        if parent_val is not None and node.val == parent_val + 1:
            length += 1
        else:
            length = 1

        left_len = dfs(node.left, node.val, length)
        right_len = dfs(node.right, node.val, length)

        return max(length, left_len, right_len)

    if not root:
        return 0
    return dfs(root, None, 0)


# Task 9: Sort Colors (Dutch National Flag)
def sortColors(nums: List[int]) -> None:

    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# Task 10: Quick Sort (In-place)
def quickSort(nums: List[int]) -> None:
   

    def partition(low: int, high: int) -> int:
        pivot = nums[high]
        i = low - 1

        for j in range(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

    def _quickSort(low: int, high: int) -> None:
        if low < high:
            pi = partition(low, high)
            _quickSort(low, pi - 1)
            _quickSort(pi + 1, high)

    _quickSort(0, len(nums) - 1)


# Task 11: Merge Sort
def mergeSort(nums: List[int]) -> None:


    def merge(left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def _mergeSort(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = _mergeSort(arr[:mid])
        right = _mergeSort(arr[mid:])
        return merge(left, right)

    sorted_arr = _mergeSort(nums)
    nums[:] = sorted_arr


# Task 12: Heap Sort (In-place)
def heapSort(nums: List[int]) -> None:


    def heapify(n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[left] > nums[largest]:
            largest = left
        if right < n and nums[right] > nums[largest]:
            largest = right

        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(n, largest)

    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)


    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(i, 0)



if __name__ == "__main__":
    print("=== Task 1: Two Sum ===")
    print(twoSum([2, 7, 11, 15], 9))  # [0,1]

    print("\n=== Task 2: First Unique Character ===")
    print(firstUniqChar("leetcode"))  # 0
    print(firstUniqChar("loveleetcode"))  # 2

    print("\n=== Task 3: Isomorphic Strings ===")
    print(isIsomorphic("egg", "add"))  # True
    print(isIsomorphic("foo", "bar"))  # False

    print("\n=== Task 4: Happy Number ===")
    print(isHappy(19))  # True
    print(isHappy(2))  # False

    print("\n=== Task 5 & 6 & 7 & 8: Binary Tree ===")

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("Level Order:", levelOrder(root))  # [[3],[9,20],[15,7]]
    print("Max Depth:", maxDepth(root))  # 3
    print("Is Symmetric:", isSymmetric(root))  # False
    print("Longest Consecutive:", longestConsecutive(root))  # 2

    print("\n=== Task 9: Sort Colors ===")
    nums9 = [2, 0, 2, 1, 1, 0]
    sortColors(nums9)
    print(nums9)  # [0,0,1,1,2,2]

    print("\n=== Task 10: Quick Sort ===")
    nums10 = [10, 7, 8, 9, 1, 5]
    quickSort(nums10)
    print(nums10)  # [1,5,7,8,9,10]

    print("\n=== Task 11: Merge Sort ===")
    nums11 = [38, 27, 43, 3, 9, 82, 10]
    mergeSort(nums11)
    print(nums11)  # [3,9,10,27,38,43,82]

    print("\n=== Task 12: Heap Sort ===")
    nums12 = [12, 11, 13, 5, 6, 7]
    heapSort(nums12)
    print(nums12)  # [5,6,7,11,12,13]