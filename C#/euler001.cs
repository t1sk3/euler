using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjectEuler
{
    class ProjectEuler
    {
        static void Main(string[] args)
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