class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = []
        even=True
        med = (len(nums1)+len(nums2))//2 
        print(med)
        if (len(nums1)+len(nums2))%2==0 : even = True
        else : even = False

        n1 = 0
        n2 = 0
        while(len(merged_arr)<=med):
            
            if n1<len(nums1) and n2<len(nums2):
                if nums1[n1]>=nums2[n2]:
                    merged_arr.append(nums2[n2])
                    n2+=1
                else:
                    merged_arr.append(nums1[n1])
                    n1+=1
            elif n1 < len(nums1):
                merged_arr.append(nums1[n1])
                n1+=1
            elif n2 < len(nums2):
                merged_arr.append(nums2[n2])
                n2+=1


        if not even:
            return merged_arr[med]
        else:
            return (merged_arr[med]+merged_arr[med-1])/2
            
            
            


        