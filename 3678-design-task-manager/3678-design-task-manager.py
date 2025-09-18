import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}  # taskId -> (userId, priority)
        self.heap = []   # stores (-priority, -taskId, taskId)
        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.tasks[taskId]
        self.tasks[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        # Just delete from map (lazy deletion in heap)
        if taskId in self.tasks:
            del self.tasks[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, negTaskId, taskId = heapq.heappop(self.heap)
            if taskId in self.tasks and self.tasks[taskId][1] == -priority:
                userId, _ = self.tasks.pop(taskId)
                return userId
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()