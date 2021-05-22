package main

import (
	"fmt"
	"strconv"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 1000
	num := ""
	res := []int{}
	for i := LIMIT - 1; i >= LIMIT/10; i-- {
		for j := LIMIT - 1; j >= LIMIT/10; j-- {
			num = strconv.Itoa(i * j)
			if is_palindrome(num) {
				res = append(res, i*j)
			}
		}
	}
	return max_in_slice(res)
}

func is_palindrome(s string) bool {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	if string(runes) == s {
		return true
	}
	return false
}

func max_in_slice(s []int) int {
	m := -1
	for i, e := range s {
		if i == 0 || e > m {
			m = e
		}
	}
	return m
}
