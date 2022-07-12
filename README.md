Q1: Convert a number into a string that contains raindrop sounds analogous to a set of
certain potential factors. A factor is a number that evenly divides into another number
leaving no remainder.
Rules:
1. If a given number has “3” as a factor, add “Pling” to the result.
2. If a given number has “5” as a factor, add “Plang” to the result.
3. If a given number has “7” as a factor, add “Plong” to the result.
4. If a given number does not have any of the “3”, “5”, “7” as a factor, the result
should be the digits of the number.
Examples:
1. 28 has 7 as a factor, but not 3 or 5, so the result would be “Plong”.
2. 30 has both 3 and 5 as factors, but not 7, so the result would be “PlingPlang”
3. 34 is not factored by 3, 5, or 7, so the result would be ”34”.

Q2: Find the difference between the square of the sum and the sum of the squares of the
first N natural numbers.
The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)² = 55² = 3025.
The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.
Hence the difference between the square of the sum of the first ten natural numbers and
the sum of the squares of the first ten natural numbers is 3025 - 385 = 2640.
You are not expected to discover an efficient solution to this yourself from first principles;
research is allowed and encouraged

Q3:By listing the first six prime numbers - 2, 3, 5, 7, 11, 13 we observe that 6th prime
number is 13.
Given a number n, determine what the nth prime is. (Assume all positive numbers for the
input and do not use any methods in the standard library)
Also, raise an exception when the prime() function receives malformed input which
would be any number < 1.

Q4: Given a number, find the sum of all the unique multiples of particular numbers up to but
not including that number.
If we list all the natural numbers below 20 that are multiples of 3 or 5, we get 3, 5, 6, 9,
10, 12, 15, and 18.
The sum of these multiples is 78.
You can make the following assumptions about the inputs to the sum_of_multiples
function:
● All input numbers are non-negative ints, i.e. natural numbers including zero.
● A list of factors must be given, and its elements are unique and sorted in
ascending order.

Q5: Take a nested list and return a single flattened list with all values except nil/null.
The challenge is to write a function that accepts an arbitrarily-deep nested list-like
structure and returns a flattened structure without any nil/null values.
Eg:
input: [1,[2,3,null,4],[null],5]
output: [1,2,3,4,5]
