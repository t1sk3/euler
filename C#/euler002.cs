using System;

namespace ProjectEuler {
    class euler002 {
        static void Main() {
            Console.WriteLine(Solve());
        }

        static int Solve() {
            int previous = 1;
            int current = 1;
            int temp = -1;
            int res = 0;

            while (current < 4000000) {
                temp = current+previous;
                previous = current;
                current = temp;

                if (current%2 == 0) {
                    res += current;
                }
            }
            return res;
        }
    }
}