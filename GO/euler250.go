package main

import (
	"eulerlib"
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() uint64 {
	MODULUS := uint64(10000000000000000)

	numSubs := getUint64ListOfLength(250)
	numSubs[0] = 1
	var tmp int
	var newSlice []uint64

	for i := 1; i <= 250250; i++ {
		tmp = int(eulerlib.PowMod(i, i, 250))
		newSlice = getUint64ListOfLength(250)
		for j := 0; j < 250; j++ {
			newSlice[(j+tmp)%250] = (numSubs[j] + numSubs[(j+tmp)%250]) % MODULUS
		}
		numSubs = newSlice
	}
	return (numSubs[0] - 1 + MODULUS) % MODULUS
}

func getUint64ListOfLength(n int) (res []uint64) {
	for i := 0; i < n; i++ {
		res = append(res, 0)
	}
	return
}
