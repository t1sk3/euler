limit := 1000000
sum := 0
i := 1
p := makePalindromeBase2(i,true)
while p < limit
 if isPalindrome(p,10) then sum := sum + p
 i := i+1
 p := makePalindromeBase2(i,true)
i := 1
p := makePalindromeBase2(i,false)
while p < limit
 if isPalindrome(p,10) then sum := sum + p
 i := i+1
 p := makePalindromeBase2(i,false)
output sum