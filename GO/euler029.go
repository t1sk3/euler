package main

import (
	"fmt"
	"math/big"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	LIMIT := 100
	res := []string{}
	num := new(big.Int)
	bigA := new(big.Int)

	for a := 2; a <= LIMIT; a++ {
		for b := 2; b <= LIMIT; b++ {
			bigA = new(big.Int).SetInt64(int64(a))
			num = new(big.Int).Mul(bigA, bigA)
			for i := 0; i < b-2; i++ {
				num.Mul(num, bigA)
			}
			res = append(res, num.Text(10))
		}
	}
	return len(remove_duplicates_from_slice(res))
}

func remove_duplicates_from_slice(s []string) []string {
	res := []string{}
	keys := make(map[string]bool)

	for _, entry := range s {
		if _, value := keys[entry]; !value {
			keys[entry] = true
			res = append(res, entry)
		}
	}
	return res
}
