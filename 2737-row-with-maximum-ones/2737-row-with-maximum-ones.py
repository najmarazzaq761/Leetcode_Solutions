class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count=0
        max_row=0
        for i,row in enumerate(mat):
            count=sum(row)
            if count> max_count:
                max_count=count
                max_row=i
        return [max_row, max_count]