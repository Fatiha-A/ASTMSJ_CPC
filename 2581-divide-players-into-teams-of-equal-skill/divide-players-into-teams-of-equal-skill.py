class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]
        result = 0
        left, right = 0, len(skill) - 1

        while left < right:
            if skill[left] + skill[right] != target:
                return -1   
            result += skill[left] * skill[right]
            left += 1
            right -= 1

        return result
