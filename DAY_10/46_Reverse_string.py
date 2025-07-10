'''Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]'''




class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None. Do not return anything, modify s in-place instead.
        """
        s.reverse()


# Leetcode python - pointer logic

# class Solution(object):
#     def reverseString(self, s):
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1




# C language my logic push and pop

#include <stdio.h>

# void reverseString(char *s, int size) {
#     for (int i = 0; i < size / 2; i++) {
#         char temp = s[i];
#         s[i] = s[size - 1 - i];
#         s[size - 1 - i] = temp;
#     }
# }

# int main() {
#     char s[] = {'h','e','l','l','o'};
#     int size = sizeof(s) / sizeof(s[0]);

#     reverseString(s, size);

#     for (int i = 0; i < size; i++) {
#         putchar(s[i]);
#     }
#     putchar('\n'); // Output: olleh

#     return 0;
# }











# C program swapping posiiton

#include <stdio.h>

# void reverseString(char *s, int size) {
#     char *start = s;              // Pointer to first character
#     char *end = s + size - 1;     // Pointer to last character

#     while (start < end) {
#         // Swap the characters
#         char temp = *start;
#         *start = *end;
#         *end = temp;

#         // Move the pointers
#         start++;
#         end--;
#     }
# }

# int main() {
#     char s[] = {'h', 'e', 'l', 'l', 'o'};
#     int size = sizeof(s) / sizeof(s[0]);

#     reverseString(s, size);

#     for (int i = 0; i < size; i++) {
#         putchar(s[i]);  // Output: olleh
#     }
#     putchar('\n');

#     return 0;
# }
