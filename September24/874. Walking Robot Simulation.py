# A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:
#
# -2: Turn left 90 degrees.
# -1: Turn right 90 degrees.
# 1 <= k <= 9: Move forward k units, one unit at a time.
# Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.
#
# Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).
#
# Note:

class Solution:
    def robotSim(self, commands, obstacles):
        x, y, d = 0, 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_distance = 0
        obstacles = set(map(tuple, obstacles))

        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d - 1) % 4
            else:
                for _ in range(cmd):
                    nx, ny = x + direction[d][0], y + direction[d][1]
                    if (nx, ny) in obstacles:
                        break
                    x, y = nx, ny
                    max_distance = max(max_distance, x * x + y * y)

        return max_distance