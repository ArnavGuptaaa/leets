/*
Name: Create Hello World Function (#2667)
URL: https://leetcode.com/problems/create-hello-world-function/

Time Complexity: O(1)
Space Complexity: O(1)
*/

function createHelloWorld() {
	const helloWorld = "Hello World";

	return function (...args): string {
		return helloWorld;
	};
}
