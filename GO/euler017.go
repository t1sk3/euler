package main

import (
	"fmt"
)

func main() {
	fmt.Println(solve())
}

func solve() int {
	ONES := []string{"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"}
	TENS := []string{"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"}
	LIMIT := 1000
	res := 0

	for i := 1; i <= LIMIT; i++ {
		res += len(to_english(i, ONES, TENS))
	}
	return res
}

func to_english(n int, ONES []string, TENS []string) string {
	temp := ""
	if 0 <= n && n < 20 {
		return ONES[n]
	} else if 20 <= n && n < 100 {
		if n%10 != 0 {
			temp = ONES[n%10]
		}
		return TENS[int(n/10)] + temp
	} else if 100 <= n && n < 1000 {
		if n%100 != 0 {
			temp = "and" + to_english(n%100, ONES, TENS)
		}
		return ONES[int(n/100)] + "hundred" + temp
	} else if 1000 <= n && n < 1000000 {
		if n%1000 != 0 {
			temp = to_english(n%1000, ONES, TENS)
		}
		return to_english(int(n/1000), ONES, TENS) + "thousand" + temp
	}
	return ""
}
