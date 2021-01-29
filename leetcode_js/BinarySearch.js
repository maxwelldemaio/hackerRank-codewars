// Iterative function to implement Binary Search 
let iterativeFunction = function (arr, x) { 

	let start=0, end=arr.length-1; 
		
	// Iterate while start not meets end 
	while (start<=end){ 

		// Find the mid index 
		let mid=Math.floor((start + end)/2); 

		// If element is present at mid, return True 
		if (arr[mid]===x) return [mid, true]; 

		// Else look in left or right half accordingly 
		else if (arr[mid] < x) 
			start = mid + 1; 
		else
			end = mid - 1; 
	} 

	return false; 
} 

// Driver code 
let arr = [0, 1, 2, 3, 4, 5]; 
let x = 2; 

// Returns position and true that it found it
console.log(iterativeFunction(arr, x));
								 
