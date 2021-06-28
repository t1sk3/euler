package eulerlib

import (
	"math"
	"strconv"
)

// returns the number of divisors the given integer has
func CountDivisors(n int) int {
	count := 0
	end := int(math.Sqrt(float64(n)))
	for i := 1; i < end; i++ {
		if n%i == 0 {
			count += 2
		}
	}
	if end*end == n {
		count++
	}
	return count
}

// returns all divisors of the given integer
func Divisors(a interface{}) []int64 {
	switch v := a.(type) {
	case int:
		return divisorsInt(v)
	case int64:
		return divisorsInt64(v)
	}
	return []int64{}
}

func divisorsInt(n int) []int64 {
	end := int(math.Sqrt(float64(n)))
	divisors := []int64{}
	if end*end == n {
		divisors = append(divisors, int64(end))
	}
	for i := 2; i < end; i++ {
		if n%i == 0 {
			divisors = append(divisors, int64(i))
			divisors = append(divisors, int64(n/i))
		}
	}
	return divisors
}

func divisorsInt64(n int64) []int64 {
	end := int64(math.Sqrt(float64(n)))
	divisors := []int64{}
	if end*end == n {
		divisors = append(divisors, end)
	}
	for i := int64(2); i < end; i++ {
		if n%i == 0 {
			divisors = append(divisors, i)
			divisors = append(divisors, n/i)
		}
	}
	return divisors
}

// returns a slice with all permutations of the given slice
func Permutations(arr []int) [][]int {
	var helper func([]int, int)
	res := [][]int{}

	helper = func(arr []int, n int) {
		if n == 1 {
			tmp := make([]int, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(arr, len(arr))
	return res
}

// Calculates the factorial of the given integer
func Factorial(n int) int {
	if n == 0 {
		return 1
	}
	res := 1
	for i := 2; i < n+1; i++ {
		res *= i
	}
	return res
}

// Calculates factorial digital sum
func FactorialDigitSum(n int) int {
	s := strconv.Itoa(n)
	i := -1
	res := 0

	for j := 0; j < len(s); j++ {
		i, _ = strconv.Atoi(string(s[j]))
		res += Factorial(i)
	}
	return res
}

// Calculates gcd for the given integers
func Gcd(a int, b int) int {
	if a == 0 {
		return b
	} else if b == 0 {
		return a
	}
	for i := b; ; i-- {
		if a%i == 0 && b%i == 0 {
			return i
		}
	}
}
