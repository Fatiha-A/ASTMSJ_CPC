class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_c=nums2.copy()
        intersection=[]
        for num in nums1:
            if num in nums2_c:
                intersection.append(num)
                nums2_c.remove(num)
        return intersection