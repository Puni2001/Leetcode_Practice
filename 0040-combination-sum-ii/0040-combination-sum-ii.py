class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start,path,target):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break  # Optimization: Stop if the number is greater than the remaining target
            
                path.append(candidates[i])
                backtrack(i+1,path,target-candidates[i])
                path.pop()
        backtrack(0,[], target)
        return result 