using System;

namespace ProjectEuler {
    class euler004 {
        static void Main() {
            Console.WriteLine(Solve());
        }

        static int Solve() {
            int largest = -1;

            for (int i = 100; i < 1000; i++) {
                for (int j = 100; j < 1000; j++) {
                    if (is_palindrome(i*j) && i*j > largest) {
                        largest = i*j;
                    }
                }
            }
            return largest;
        }

        static bool is_palindrome(int num) {
            string n = Convert.ToString(num);
            string n2 = "";

            for (int i = n.Length-1; i >= 0; i--) {
                n2 += n[i];
            }
            return n2 == n;
        }
    }
}