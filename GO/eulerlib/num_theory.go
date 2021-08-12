package eulerlib

import (
	"math"
	"strconv"
	"math/bits"
	"math/big"
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

func Combinations(set []string, n int) (subsets [][]string) {		// https://github.com/mxschmitt/golang-combinations/blob/master/combinations.go
	length := uint(len(set))

	if n > len(set) {
		n = len(set)
	}

	// Go through all possible combinations of objects
	// from 1 (only first object in subset) to 2^length (all objects in subset)
	for subsetBits := 1; subsetBits < (1 << length); subsetBits++ {
		if n > 0 && bits.OnesCount(uint(subsetBits)) != n {
			continue
		}

		var subset []string

		for object := uint(0); object < length; object++ {
			// checks if object is contained in subset
			// by checking if bit 'object' is set in subsetBits
			if (subsetBits>>object)&1 == 1 {
				// add object to subset
				subset = append(subset, set[object])
			}
		}
		// add subset to subsets
		subsets = append(subsets, subset)
	}
	return subsets
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

func DigitSum(a interface{}) int {
	switch v := a.(type) {
	case int:
		return digitSumInt(v)
	case string:
		return digitSumString(v)
	}
	return -1
}

func digitSumInt(n int) (res int) {
	s := strconv.Itoa(n)
	tmp := -1

	for i := 0; i < len(s); i++ {
		tmp, _ = strconv.Atoi(string(s[i]))
		res += tmp
	}
	return
}

func digitSumString(s string) (res int) {
	tmp := -1

	for i := 0; i < len(s); i++ {
		tmp, _ = strconv.Atoi(string(s[i]))
		res += tmp
	}
	return
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

func PrimeFactors(n int) []int {
	primefs := []int{}
	for n%2 == 0 {
		primefs = append(primefs, 2)
		n = n / 2
	}

	for i := 3; i*i <= n; i = i + 2 {
		for n%i == 0 {
			primefs = append(primefs, i)
			n = n / i
		}
	}

	if n > 2 {
		primefs = append(primefs, n)
	}

	return primefs
}

func PowMod(x int, y int, m int) int64 {
	x1 := new(big.Int).SetInt64(int64(x))
	y1 := new(big.Int).SetInt64(int64(y))
	m1 := new(big.Int).SetInt64(int64(m))
	return x1.Exp(x1, y1, m1).Int64()
}

func ToRadians(n float64) float64 {
	return n*math.Pi/180
}
