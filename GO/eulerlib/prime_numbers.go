package eulerlib

import (
	"math"
)

// checks to see if the given number is a prime
func IsPrime(p int) bool {
	end := int(math.Sqrt(float64(p)))
	if end*end == p {
		return false
	}
	end++
	for i := 2; i < end; i++ {
		if p%i == 0 {
			return false
		}
	}
	return true
}

func ListPrimality(n int) []bool {
	res := []bool{false, false}
	if n >= 2 {
		res = append(res, true)
	}
	for i := 3; i <= n; i++ {
		if IsPrime(i) {
			res = append(res, true)
		} else {
			res = append(res, false)
		}
	}
	return res
}
