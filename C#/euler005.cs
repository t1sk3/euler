using System;

namespace ProjectEuler {
    class euler005 {
        static void Main() {
            Console.WriteLine(Solve());
        }

        static int Solve() {
            for (int i = 1; ; i++) {
                if (divisble(i)) {
                    return i;
                }
            }
        }

        static bool divisble(int n) {
            int LIMIT = 20;
            for (int i = 1; i <= LIMIT; i++) {
                if (n%i != 0) {
                    return false;
                }
            }
            return true;
        }
    }
}