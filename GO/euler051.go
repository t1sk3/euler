package main

import (
	"eulerlib"
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	isPrime := eulerlib.ListPrimality(1000000)
	var n []int
	var digs []int
	var count int
	for i := 0; i < len(isPrime); i++ {
		if !isPrime[i] {
			continue
		}
		n = to_digs(i)
		for mas := 0; mas < (1 << len(n)); mas++ {
			digs = do_mas(n, mas)
			count = 0
			for j := 0; j < 10; j++ {
				if digs[0] != 0 && isPrime[to_num(digs)] {
					count++
				}
				digs = add_mas(digs, mas)
			}

			if count == 8 {
				digs = do_mas(n, mas)
				for j := 0; j < 10; j++ {
					if digs[0] != 0 && isPrime[to_num(digs)] {
						return to_num(digs)
					}
					digs = add_mas(digs, mas)
				}
			}
		}
	}
	return -1
}

func to_digs(n int) []int {
	res := []int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	i := 10
	for n != 0 {
		i--
		res[i] = n % 10
		n /= 10
	}
	return res[i:]
}

func do_mas(digs []int, mas int) []int {
	res := []int{}
	for j := 0; j < len(digs); j++ {
		res = append(res, 0)
	}
	for i := 0; i < len(digs); i++ {
		res[i] = digs[i] * ((^mas >> i) & 1)
	}
	return res
}

func add_mas(digs []int, mas int) []int {
	res := []int{}
	for j := 0; j < len(digs); j++ {
		res = append(res, 0)
	}
	for i := 0; i < len(digs); i++ {
		res[i] = digs[i] + ((mas >> i) & 1)
	}
	return res
}

func to_num(digs []int) int {
	res := 0
	for _, e := range digs {
		res = res*10 + e
	}
	return res
}
