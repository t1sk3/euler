package eulerlib

import (
	"strconv"
	"math"
	"strings"
)

// Checks whether the given string is a palindrome
func IsPalindrome(s string) bool {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes) == s
}

// returns the highest value in the given slice
func MaxInSlice(s []int) int {
	m := -1
	for i, e := range s {
		if i == 0 || e > m {
			m = e
		}
	}
	return m
}

// returns the highest of 2 integers
func MaximumBetweenInts(a int, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

// joins a slice of integers into a string
func JoinSlice(s []int) string {
	res := ""
	for _, e := range s {
		res += strconv.Itoa(e)
	}
	return res
}

// removes any duplicates fm a slice
func RemoveDuplicates(s []string) []string {
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

// returns the sum of the integers in the given slice
func Sum(lst []int) int {
	res := 0
	for _, element := range lst {
		res += element
	}
	return res
}

// Converts the given integer to the given base and returns it as a string
func DecimalToBase(n int, b int) string {
	alphabet := "abcdefghijklmnopqrstuvwxyz"
	if b == 10 {
		return strconv.Itoa(n)
	}
	basebase := 1
	iteration := -1
	newlst := []string{}

	for basebase <= n {
		basebase *= b
		iteration++
	}
	multiplier := int(math.Pow(float64(b), float64(iteration)))
	var new int

	for i := 0; i <= iteration; i++ {
		if n >= multiplier {
			new = (n - (n % multiplier)) / multiplier
			newlst = append(newlst, strconv.Itoa(new))
			n -= multiplier * new
		} else {
			newlst = append(newlst, "0")
		}
		if multiplier != 1 {
			multiplier /= b
		} else if multiplier == 1 {
			multiplier = 0
		}
	}
	
	for i := 0; i < len(newlst); i++ {
		for j := 10; j < 36; j++ {
			if newlst[i] == strconv.Itoa(j) {
				newlst[i] = string(alphabet[j-10])
			}
		}
	}
	return strings.Join(newlst[:], "")
}
