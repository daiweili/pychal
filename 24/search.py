from heapq import heappush, heappop

def manhattanDistance(a,b):
  x0, y0 = a
  x1, y1 = b
  return abs(x1-x0) + abs(y1-y0)

def getNextPositions(pos, grid):
  next = []
  x, y = pos
  if x >= 1 and grid[x-1, y]:
    next.append((x-1,y))
  if y >= 1 and grid[x, y-1]:
    next.append((x, y-1))
  if y < grid.shape[1]-1 and grid[x, y+1]:
    next.append((x, y+1))
  if x < grid.shape[0]-1 and grid[x+1, y]:
    next.append((x+1, y))
  return next

def comparePos(a, b):
  return a[0] == b[0] and a[1] == b[1]

def AStarSearch(start, goal, grid, h=manhattanDistance):
  """
  Performs A* search

  Keyword arguments:
  start -- (x0, y0)
  goal -- (x1, y1)
  grid -- 2D numpy.array of 0's and 1's, where 1's are walkable and 0's are walls
  h -- heuristic function that computes an approximate cost from the current position to the goal,
    must be admissible (computed cost must be <= to actual cost)

  Returns a list of the shortest path (positions)
  """
  # Visited nodes, keeps track of previous node
  closed_set = {start:(None, 0)}
  # Nodes to visit; is a priority queue
  open_set = []
  heappush(open_set, (start, h(start, goal)))

  while True:
    if not open_set:
      return

    pos, cost = heappop(open_set)

    if comparePos(pos, goal):
      positions = []
      while pos:
        positions.append(pos)
        pos, cost = closed_set[pos]
      positions.reverse()
      return positions

    for npos in getNextPositions(pos, grid):
      hcost = h(npos, goal)
      gcost = cost+1
      fcost = gcost + hcost

      if npos not in closed_set or\
          gcost < closed_set[npos][1]:
        heappush(open_set, (npos, fcost))
        closed_set[npos] = (pos, gcost)


