class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, target, path):
          if target == 0:
            result.append(path.copy())
            return

          if target < 0:
            return

          for i in range(index, len(candidates)):
            path.append(candidates[i])
            backtrack(i,target-candidates[i],path)
            path.pop()

        backtrack(0,target,[])

        return result
        