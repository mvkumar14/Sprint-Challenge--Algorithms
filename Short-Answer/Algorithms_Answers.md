#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime = O(n) 

a increases by a value of n^2 every time.
and the while loop runs until the value of a
(which starts at 0) reaches n^3.

How many n^2s are in n^3 There are n n^2s
in n^3. There are n n^2s in n^3.

for example:
2^3 = 8
2^2 = 4
4 + 4 = 8 

3^3 = 27
3^2 = 9
9 + 9 + 9 = 27

it takes n n^2 to get n^3 

b) Runtime = O(n*log(n))

The outer loop runs n times
The inner loop runs log(n) times for every time
the outer loop runs.

for example:
if n = 3
{for i in range(3) = for i in range [0,1,2]
    j= 1
    while j < 3:
        j *= 2 (j doubles)

the while loop runs log(n) times for each time the for 
loop runs (n)

for something like n=100. log(100) = 6.643
j = 1, 2, 4, 8, 16, 32, 64 ,128 (2^7)

c) Runtime = O(n)

This is a recursive algorithm. but 
the recursive part is called n times
where n is the size of the input. 
expanded you need n lines of code
and once you hit the base case you need to substitute
upwards.

It may be O(2n) including substitutions

ex:
bunnyEars(2) = 2 + bunnyEars(1)
bunnyEars(1) = 2 + bunnyEars(0)
bunnyEars(0) = 0

## Exercise II
first time:
Start from the middle floor. If the egg breaks
go to the floor in the middle in the range between the bottom floor and your current floor and try again
if it doesn't break. Go to floor in the middle between the current floor and the topmost floor, and try again

subsequent times:
if it still doesn't break move upwards cutting distance in half
if it does break move downwards cutting distance in half

This is basically the binary search algorithm, but the stopping condition is when you find the border where on one floor it doesn't break, and on the next it breaks. 

while start != end:
    start = 0
    ende = n
    middle = n/2
    if egg breaks when thrown off middle floor:
        start = start
        end = middle
        middle = start + (start-end)/2 
    else if it doesn't break:
        start = start
        end = middle
        middle = start + (start-end)/2 
return start

COMPLEXITY: the complexity of this solution is log(n) because you are using a binary search strategy.