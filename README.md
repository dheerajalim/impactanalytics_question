# impactanalytics_question

Given an array of integers, calculate the sum of elements, if an element itself is an array, thus increasing the depth, change the multiplier. For an array to be at even index double the multiplier and at odd index triple the multiplier, base parent multiplier is 1, few samples:

[2,4,[3,-4,[2,3],[5]],[6,[9]],8] => Sum would be 1 * (2 + 4 + 2*(3 - 4 + 2 * (2+3) + 3 * (5)) + 3*(6 + 3*9) + 8 = 161

Explanation - Initial multiplier is 1 for all elements in main array, now there's a sub array at the index 2 -[3,-4,[2,3],[5]], therefore the multiplier becomes (Base Parent Multiplier) * 2 = 1 * 2 = 2, inside the sub array there's another set of sub array at the index 2,3 respectively, so the multipliers are further multiplied by 2,3 , they become 4 , 6 for those sub arrays. Index 3 has another sub array, for which the multiplier becomes (Base Parent Multiplier) * 3 = 1 * 3 = 3, which again contains a sub array at the index 1, so the multiplier becomes (Parent Multiplier) * 3 = 3 * 3 = 9, for that sub array elements

Another Example:

[[6,[[[6,8]]]]] = 1 * ( 2*(6 + 3*(2*(2*(6 + 8))))) = 348

Using the same logic at index 0 there's an array, then inside that array at index 1 there's another array, which is a concentric array of 3, final one containing the elements 6,8.


# Assumption
The input will always be a valid python list of integers
