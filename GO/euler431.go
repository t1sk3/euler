package main

import (
	"eulerlib"
	"fmt"
	"math"
)

// inefficient but gets the right answer

var (
	RADIUS float64
	REPOSE float64
)

func main() {
	fmt.Println(solve())
}

func solve() string {
	RADIUS = 6
	REPOSE = eulerlib.ToRadians(40)

	res := float64(0)
	for i := 20; i <= 25; i++ {
		res += findRootSecant(0, RADIUS, float64(i*i))
	}
	return fmt.Sprintf("%.9f", res)
}

func findRootSecant(x0 float64, x1 float64, v float64) float64 {
	sam := 1000
	y0 := volume(x0, sam)
	y1 := volume(x1, sam)

	var x2 float64
	var y2 float64

	for math.Abs(x0-x1) > math.Pow(10, -12) {
		x2 = (v-y0)/(y1-y0)*(x1-x0) + x0
		y2 = volume(x2, sam)
		x0 = x1
		x1 = x2
		y0 = y1
		y1 = y2
		if math.Abs(x0-x1) > math.Pow(10, -4) {
			sam = int(math.Max(1000000, float64(sam)))
		}
		if math.Abs(x0-x1) > math.Pow(10, -6) {
			sam = int(math.Max(10000000, float64(sam)))
		}
		if math.Abs(x0-x1) > math.Pow(10, -8) {
			sam = int(math.Max(100000000, float64(sam)))
		}
	}
	return x1
}

func volume(x float64, sam int) float64 {
	dVol := math.Pow(RADIUS+x, 3) / 3 * math.Pi * 2

	var scal float64
	var r2px2 float64
	var rec2x float64
	var res float64
	var r float64
	var r2 float64

	if x > 0 {
		scal = x * 2 / float64(sam)
		r2px2 = RADIUS*RADIUS + x*x
		rec2x = 1 / (x * 2)
		res = 0

		for i := 0; i < sam; i++ {
			r = RADIUS - x + (float64(i)+0.5)*scal
			r2 = r * r

			res += math.Acos(((r2px2-r2)*rec2x-x)/r) * r2
		}
		dVol -= res * 4 * x / float64(sam)
	}
	return dVol * math.Tan(REPOSE)
}
