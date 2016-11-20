Worksheet C  
A) The algorithm checks if there is a duplicate element in the list by going through the list in order to see if a element is repeated, if a element has a duplicate the result will be true. 
B) Because of the loop within the loop so it checks for duplicate values, every pair of values in the list has to be compared to every value to see if they match hence why its quadratic in the worst case.
C) The algorithm is still correct because the values are still being compared because j is comparing the value before i where i has already compared the values, hence every possible output for i and j is still being checked.
D) The algorithm is half as fast because it only makes half the comparisons after removing the duplicate comparisons so it compares more values than it needs to.
E) Yes its quadratic still because ((n^2)-n)/2
F) O(n log n) - Time Complexity https://wiki.python.org/moin/TimeComplexity 
G) O(N^2 Log N)because you multiply the time complexity of the sort function which is O(n log n) by the loop time complexity which is O(N)  
H) The first algorithm with N^2 will run faster because the values of O(N^2 Log N) get larger than that the original one when the numbers get too high. 
I) If they are making a short list with not a lot of values
