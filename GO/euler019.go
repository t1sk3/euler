package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	res := 0
	for year := 1901; year <= 2000; year++ {
		for month := 1; month <= 12; month++ {
			if time.Date(year, time.Month(month), 1, 0, 0, 0, 0, time.UTC).Weekday() == 0 {
				res++
			}
		}
	}
	return res
}
