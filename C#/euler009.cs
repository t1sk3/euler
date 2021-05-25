using System;

namespace ProjectEuler {
    class euler009 {
        static void Main() {
            Console.WriteLine(Solve());
        }

        static int Solve() {
            for (int c = 1; c < 999; c++) {
                for (int b = 1; b < 1000-c; b++) {
                    for (int a = 1; a < 1001-b-c; a++) {
                        if (a+b+c == 1000 && is_triplet(a,b,c)) {
                            return a*b*c;
                        }
                    }
                }
            }
            return -1;
        }

        static bool is_triplet(int a, int b, int c) {
            return c*c == a*a + b*b;
        }
    }
}