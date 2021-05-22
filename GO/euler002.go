package main

import "fmt"

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 4000000
	fibo := []int{1, 2, 3, 5, 8, 13, 21, 34, 55, 89}
	res := 0

	for fibo[len(fibo)-1] < LIMIT {
		fibo = append(fibo, fibo[len(fibo)-1]+fibo[len(fibo)-2])
	}

	for _, element := range fibo {
		if element%2 == 0 {
			res += element
		}
	}
	return res
}
