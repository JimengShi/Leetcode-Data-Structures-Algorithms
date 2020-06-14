# Method 1: two sets
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
    
# Time: O(m+n), O(n) is used to convert nums1 into set, O(m) is used to convert nums2 to set.
# Space: O(m+n) in the worst case all elements are different.
    
    
# Method 2: dictionary    
class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        # 
        dict1 = dict()
        for i in nums1:
            dict1[i] = dict1.get(i, 0) + 1
            # if i not in dict1:
            #     dict1[i] = 1
            # else:
            #     dict1[i] += 1
                
        res = []
        for i in nums2:
            if i in dict1 and i not in res:
                res.append(i)
        return res

# Time: O(m+n), where n and m are arrays' lengths.
# Space: O(min(m,n)) in the worst case all elements are different.
    

# Method 3: two pointers but sorted nums in advance
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        
        l1, l2 = sorted(nums1), sorted(nums2)
        res = []
        
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] == l2[j]:
                if l1[i] not in res:
                    res.append(l1[i])
                i += 1
                j += 1
            elif l1[i] < l2[j]:
                i += 1
            else:
                j += 1
                
        return res

# Time: O(nlogn+mlogm), where n and m are arrays' lengths.
# Space: O(min(m,n)) in the worst case all elements are different.