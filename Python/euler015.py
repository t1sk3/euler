

def main():
    for i in range(1,21):
        for j in range(1,21):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return str(grid[-1][-1])

grid = [[1] * 21]
for x in range(20):
    grid += [[1] + [0] * 20]

if __name__ == "__main__":
    print(main())