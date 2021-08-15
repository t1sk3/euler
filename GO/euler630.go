package main

import (
	"fmt"
)

// very very very inefficient
// I had this run through a night on a pretty beefy computer
// but idk how long it took exactly but long

type Point struct {
	X int
	Y int
}

func (a Point) cmp(b Point) bool {
	return a.X == b.X && a.Y == b.Y
}

type Line struct {
	A Point
	B Point
}

func main() {
	fmt.Println(solve())
}

func solve() (res int) {
	points := removeDuplicatePoints(getPoints())
	fmt.Println(len(points), "points calculated...")
	lines := []Line{}
	for i := 0; i < len(points); i++ {
		for j := i; j < len(points); j++ {
			if j != i {
				lines = append(lines, Line{points[i], points[j]})
			}
		}
	}
	fmt.Println(len(lines), "lines calculated...")
	lines = removeDuplicateLines(lines)
	fmt.Println("Duplicate lines removed...")
	for i := 0; i < len(lines); i++ {
		for j := i + 1; j < len(lines); j++ {
			if checkIntersect(lines[i], lines[j]) {
				res += 2
			}
		}
	}

	return
}

func checkIntersect(l1 Line, l2 Line) bool {
	return float32(l1.A.Y-l1.B.Y)/float32(l1.A.X-l1.B.X) != float32(l2.A.Y-l2.B.Y)/float32(l2.A.X-l2.B.X)
}

func removeDuplicateLines(l []Line) (res []Line) {
	var d float32
	var d2 float32
	var q float32
	var q2 float32
	var g bool
	for _, e := range l {
		g = true
		d = float32(e.A.Y-e.B.Y) / float32(e.A.X-e.B.X)
		q = float32(e.A.Y) - d*float32(e.A.X)
		for _, e2 := range res {
			d2 = float32(e2.A.Y-e2.B.Y) / float32(e2.A.X-e2.B.X)
			q2 = float32(e2.A.Y) - d*float32(e2.A.X)
			if d2 == d && q2 == q {
				g = false
				break
			}
		}
		if g {
			res = append(res, e)
		}
	}
	return
}

func removeDuplicatePoints(p []Point) (res []Point) {
	s := true
	res = append(res, p[0])
	for i := 1; i < len(p); i++ {
		s = true
		for j := 0; j < len(res); j++ {
			if res[j].cmp(p[i]) {
				s = false
				break
			}
		}
		if s {
			res = append(res, p[i])
		}
	}
	return
}

func getPoints() (res []Point) {
	s := 290797
	s0 := s * s % 50515093
	s1 := s0 * s0 % 50515093
	t0 := (s0 % 2000) - 1000
	t1 := (s1 % 2000) - 1000
	res = append(res, Point{t0, t1})
	for i := 1; i < 2500; i++ {
		s0 = s1 * s1 % 50515093
		s1 = s0 * s0 % 50515093
		t0 = (s0 % 2000) - 1000
		t1 = (s1 % 2000) - 1000
		res = append(res, Point{t0, t1})
	}
	return
}
