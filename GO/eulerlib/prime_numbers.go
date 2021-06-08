package eulerlib

import (
	"math"
)

// checks to see if the given number is a prime
func IsPrime(a interface{}) bool {
	switch v := a.(type) {
	case int:
		return isPrimeInt(v)
	case uint:
		return isPrimeUint(v)
	case int64:
		return isPrimeInt64(v)
	case uint64:
		return isPrimeUint64(v)
	}
	return false
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

func isPrimeInt(p int) bool {
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

func isPrimeUint(p uint) bool {
	end := uint(math.Sqrt(float64(p)))
	if end*end == p {
		return false
	}
	end++
	for i := uint(2); i < end; i++ {
		if p%i == 0 {
			return false
		}
	}
	return true
}

func isPrimeInt64(p int64) bool {
	end := int64(math.Sqrt(float64(p)))
	if end*end == p {
		return false
	}
	end++
	for i := int64(2); i < end; i++ {
		if p%i == 0 {
			return false
		}
	}
	return true
}

func isPrimeUint64(p uint64) bool {
	end := uint64(math.Sqrt(float64(p)))
	if end*end == p {
		return false
	}
	end++
	for i := uint64(2); i < end; i++ {
		if p%i == 0 {
			return false
		}
	}
	return true
}
