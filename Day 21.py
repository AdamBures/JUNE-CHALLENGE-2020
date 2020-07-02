class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
    #If at any point his health point drops to 0 or below, he dies immediately.
    #have to make sure at any point health is > 0
    #dp[i][j] is minimum health needed when arriving at this grid
    #dp[i][j] = min(max(1, dp[right]-right_grid_value), max(1, dp[down]-down_grid_value))
        row, col = len(dungeon), len(dungeon[0])
        dp = [[0 for x in range(col)] for x in range(row)]
        dp[row-1][col-1] = 1
        for i in range(row-2, -1, -1):
            dp[i][col-1] = max(1, dp[i+1][col-1]-dungeon[i+1][col-1])
        for i in range(col-2, -1, -1):
            dp[row-1][i] = max(1, dp[row-1][i+1]-dungeon[row-1][i+1])
        for i in range(row-2, -1, -1):
            for j in range(col-2, -1, -1):
                right = max(1, dp[i][j+1]-dungeon[i][j+1])
                down = max(1, dp[i+1][j]-dungeon[i+1][j])
                dp[i][j] = min(right, down)
        return max(1, dp[0][0]-dungeon[0][0])
