package eulerlib

import (
	"math"
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
func Divisors(n int) []int {
	end := int(math.Sqrt(float64(n)))
	divisors := []int{}
	if end*end == n {
		divisors = append(divisors, end)
	}
	for i := 2; i < end; i++ {
		if n%i == 0 {
			divisors = append(divisors, i)
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
	res := 1
	for i := 2; i < n+1; i++ {
		res *= i
	}
	return res
}
