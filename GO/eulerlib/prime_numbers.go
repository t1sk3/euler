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
	for i := 2; i < end; i++ {
		if p%i == 0 {
			return false
		}
	}
	return true
}
