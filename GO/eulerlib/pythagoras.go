package eulerlib

// checks if the given triplet is a pythagorean triplet
func IsTriplet(a int, b int, c int) bool {
	return c*c == b*b+a*a
}
