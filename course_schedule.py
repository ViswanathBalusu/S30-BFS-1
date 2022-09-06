from typing import List
from queue import Queue


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # if len(prerequisites) == 0:
        #     return True
        _map = {}
        indegrees = [0] * numCourses
        for prerequisite in prerequisites:
            indegrees[prerequisite[0]] += 1
            if not prerequisite[1] in _map:
                _map[prerequisite[1]] = []
            _map[prerequisite[1]].append(prerequisite[0])

        q = Queue()
        count = 0
        for i, val in enumerate(indegrees):
            if val == 0:
                q.put(i)
                count += 1
        if q.empty():
            return False
        while not q.empty():
            curr = q.get()
            dependents = _map.get(curr)
            if dependents is not None:
                for dependent in dependents:
                    indegrees[dependent] -= 1
                    if indegrees[dependent] == 0:
                        q.put(dependent)
                        count += 1
                        if count == numCourses:
                            return True

        return False


if __name__ == '__main__':
    # courses = [[1, 0], [2, 0], [3, 1], [5, 2], [3, 2], [4, 1], [5, 4]]
    courses = [[0, 1]]
    print(Solution().canFinish(2, courses))
