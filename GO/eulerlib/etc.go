package eulerlib

import (
	"math"
	"strings"
	"sort"
	"strconv"
)

// Checks whether the given integer is pandigita
func IsPandigital(n int) bool {
	n_string := []int{}
	reference := []int{}
	temp := -1
	for _, e := range strconv.Itoa(n) {
		temp, _ = strconv.Atoi(string(e))
		n_string = append(n_string, temp)
	}
	for i := 1; i <= len(n_string); i++ {
		reference = append(reference, i)
	}
	sort.Ints(n_string)
	sort.Ints(reference)
	return JoinSlice(n_string) == JoinSlice(reference)
}

// creates a slice containing al ldigits of the given integer as individual integers
func MakeIntSlice(n int64) []int {
	res := []int{}
	n_string := strconv.FormatInt(n, 10)
	temp := -1
	for _, e := range n_string {
		temp, _ = strconv.Atoi(string(e))
		res = append(res, temp)
	}
	return res
}

// Checks whether the given stringis a palindrome
func IsPalindrome(s string) bool {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes) == s
}

// returns the highest value i the given slice
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

// joins a slice of strings into a string
func JoinSliceString(s []string) string {
	res := ""
	for _, e := range s {
		res += e
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

// returns the sum of theintegers in the given slice
func Sum(lst interface{}) int64 {
	switch v := lst.(type) {
	case []int:
		return int64(sumInt(v))
	case []int64:
		return sumInt64(v)
	}
	return -1
}

func sumInt64(lst []int64) int64 {
	res := int64(0)
	for _, element := range lst {
		res += element
	}
	return res
}

func sumInt(lst []int) int {
	res := 0
	for _, element := range lst {
		res += element
	}
	return res
}

// Converts the given integer to the give base and returns it as a string
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

// Returns a substring of the given stri from the beginning up to a given index
func Substring(s string, n int) string {
	res := ""
	if n == 0 {
		return res
	}
	for i, c := range s {
		res += string(c)
		if i >= n-1 {
			return res
		}
	}
	return res
}

func ReverseString(s string) (res string) {
	for i := len(s)-1; i >= 0; i-- {
		res += string(s[i])
	}
	return
}
