class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        for sandwitch in sandwiches:
            if count[sandwitch] == 0:
                break
            count[sandwitch] -= 1
        return count[0] + count[1]