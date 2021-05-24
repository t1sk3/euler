using System;

namespace ProjectEuler
{
    class euler001
    {
        static void Main()
        {
            Console.WriteLine(Solve());
        }

        static int Solve() {
            const int LIMIT = 1000;
            int res = 0;
        	
            for (int i = 1; i < LIMIT; i++) {
                if (i%3 == 0 || i%5 == 0) {
                    res += i;
                }
            }
            return res;
        }
    }
}