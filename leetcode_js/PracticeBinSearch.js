
function BinarySearch(array, num){
    // Set start and end indexes
    let start = 0;
    let end = array.length - 1;

    while(start <= end){
        let mid = Math.floor((start + end)/2); // middle of subarray
        // Check if we found the value
        if (array[mid] === x){
            return true;
        }
        // Change subarray based on if higher/lower
        if (array[mid] < x){
            start = mid + 1; // We've already checked mid
        } else {
            end = mid - 1;
        }
    }
    return false;  
}


// Driver code 
let arr = [1, 3, 5, 7, 8, 9, 10]; 
let x = 5; 

// Returns position and true that it found it
console.log(BinarySearch(arr, x));
