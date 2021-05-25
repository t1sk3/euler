using System;

namespace ProjectEuler {
    class euler006 {
        static void Main() {
            Console.WriteLine(Solve());
        }

        static int Solve() {
            int LIMIT = 100;
            int sqos = 0;
            int sosq = 0;
            int res = 0;

            for (int i = 1; i <= LIMIT; i++) {
                sosq += i*i;
                sqos += i;
            }
            sqos *= sqos;
            res = sqos-sosq;

            if (res < 0) {
                res *= -1;
            }

            return res;

        }
    }
}