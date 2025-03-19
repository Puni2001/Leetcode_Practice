class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
          graph[prereq].append(course)

        state = {i:0 for i in range(numCourses)}

        def has_cycle(course):
          if state[course] == 1:
            return True 
          
          if state[course] == 2:
            return False 

          state[course] = 1 
          for neighbor in graph[course]:
            if has_cycle(neighbor):
              return True 
          state[course] = 2
          return False 



        
        for course in range(numCourses):
          if has_cycle(course):
            return False 

        return True 