package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	grid := [][]int{}
	temp := []int{}
	for i := 0; i < 21; i++ {
		temp = []int{}
		for j := 0; j < 21; j++ {
			if i == 0 || j == 0 {
				temp = append(temp, 1)
			} else {
				temp = append(temp, 0)
			}
		}
		grid = append(grid, temp)
	}

	for i := 1; i < 21; i++ {
		for j := 1; j < 21; j++ {
			grid[i][j] = grid[i-1][j] + grid[i][j-1]
		}
	}
	return grid[len(grid)-1][len(grid[len(grid)-1])-1]
}
