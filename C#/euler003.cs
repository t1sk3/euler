using System;

namespace ProjectEuler {
    class euler003 {
        static void Main() {
            Console.WriteLine(Solve());
        }

        static int Solve() {
            double num = 600851475143;
            int end = Convert.ToInt32(Math.Sqrt(num));

            for (int i = end; i > 1; i--) {
                if (is_prime(i) && num%i == 0) {
                    return i;
                }
            }
            return -1;
        }

        static bool is_prime(int n) {
            int end = Convert.ToInt32(Math.Sqrt(n));
            for (int i = 2; i <= end; i++) {
                if (n%i == 0) {
                    return false;
                }
            }
            return true;
        }
    }
}