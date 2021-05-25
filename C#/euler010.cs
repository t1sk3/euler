using System;

namespace ProjectEuler {
    class euler010 {
        static void Main() {
            Console.WriteLine(Solve());
        }

        static Int64 Solve() {
            Int64 res = 0;
            for (Int64 i = 2; i < 2000000; i++) {
                if (is_prime(i)) {
                    res += i;
                }
            }
            return res;
        }

        static bool is_prime(Int64 n) {
            long end = Convert.ToInt64(Math.Sqrt(n));
            for (Int64 i = 2; i <= end; i++) {
                if (n%i == 0) {
                    return false;
                }
            }
            return true;
        }
    }
}