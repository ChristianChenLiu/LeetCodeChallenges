class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        toVisitStack = [0]
        roomVisited = {}
        for i in range(len(rooms)):
            roomVisited[i] = 0
        visitedCount = 0

        while toVisitStack:
            toVisit = toVisitStack.pop()
            if roomVisited[toVisit] != 1:
                roomVisited[toVisit] = 1
                visitedCount += 1
                for k in rooms[toVisit]:
                    toVisitStack.append(k)

        return visitedCount == len(rooms)