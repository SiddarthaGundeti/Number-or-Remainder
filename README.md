# Number-or-Remainder

Input: 9 

Output: 4 2 

Question Explanation:

This program is designed to assess a number N against two specific conditions:

Whether N is divisible by both 5 and 7.
Whether N is less than 7.
Depending on the evaluation, the program either prints N itself if any of the conditions are met, or it prints the remainders of N when divided by 5 and 7, each on a new line.

Logical Approach:

Read Input:
The program reads an integer N.

Check Divisibility by 5 and 7:
The program checks if N is divisible by both 5 and 7 (i.e., N % 5 == 0 and N % 7 == 0). If true, it prints N.

Check if N is Less Than 7:
If N is not divisible by both 5 and 7, the program checks if N is less than 7. If true, it prints N.

Calculate and Print Remainders:
If neither condition is met, the program calculates the remainder of N when divided by 5 (N % 5) and the remainder of N when divided by 7 (N % 7), printing each on a separate line.

Example for Clarity:

If N is 3:
3 is not divisible by both 5 and 7.
3 is less than 7. Thus, the condition is satisfied, and the output is 3.

If N is 9:
9 is not divisible by both 5 and 7.
9 is not less than 7. Neither condition is satisfied.
The remainder of 9 divided by 5 is 4, and by 7 is 2.

The output will be: 4 2 
