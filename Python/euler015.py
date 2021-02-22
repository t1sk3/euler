def main():
    LIMIT = 20

    grid = [[1] * (LIMIT + 1)]
    for x in range(LIMIT):
        grid += [[1] + [0] * LIMIT]

    for i in range(1,LIMIT + 1):
        for j in range(1,LIMIT + 1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return str(grid[-1][-1])

if __name__ == "__main__":
    print(main())