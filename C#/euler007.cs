using System;

namespace ProjectEuler {
    class euler007 {
        static void Main() {
            Console.WriteLine(Solve());
        }

        static int Solve() {
            int counter = 0;

            for (int i = 2; ; i++) {
                if (is_prime(i)) {
                    counter++;
                }
                if (counter == 10001) {
                    return i;
                }
            }
        }

        static bool is_prime(int n) {
            int end = Convert.ToInt32(Math.Sqrt(Convert.ToDouble(n)));

            for (int i = 2; i <= end; i++) {
                if (n%i == 0) {
                    return false;
                }
            }
            return true;
        }
    }
}