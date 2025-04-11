/*
Name: Sum of Two Integers (#371)
URL: https://leetcode.com/problems/sum-of-two-integers/

Time Complexity: O(32)
Space Complexity: O(1)
*/

function getSum(a: number, b: number): number {
	while (b != 0) {
		let sum = a ^ b;
		let carry = a & b;

		a = sum;
		b = carry << 1;
	}

	return a;
}
