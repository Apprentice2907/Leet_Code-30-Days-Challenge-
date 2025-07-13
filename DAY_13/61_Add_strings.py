'''Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"'''












# School logic simple one element at a time

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0

            total = d1 + d2 + carry
            carry = total // 10
            digit = total % 10

            result = chr(digit + ord('0')) + result  
            i -= 1
            j -= 1

        return result








# Rules violation

# class Solution(object):
#     def addStrings(self, num1, num2):
#         a = int(num1)
#         b = int(num2)

#         return str(a+b)
            










# Logic 1

#1 – “Lookup‑table” addition (no ord, no int, no .index)
# Instead of turning characters into numbers, we pre‑compute every possible single‑digit sum (there are only 100 of them: 0‒9 + 0‒9, with or without a carry‑in).


# carry‑in | d1 | d2 |  result‑digit, carry‑out
# ---------------------------------------------
#     0    |  0 |  0 | → 0 , 0
#     0    |  0 |  1 | → 1 , 0
#          ...
#     0    |  9 |  9 | → 8 , 1   (because 9+9 = 18)
#     1    |  0 |  0 | → 1 , 0   (carry‑in adds 1)
#          ...
#     1    |  9 |  9 | → 9 , 1   (19)
# We store this as two 3‑D lists:




# lookup[d1][d2][carry_in]  → result digit as a character
# carry_out[d1][d2][carry_in] → 0 or 1




digits      = "0123456789"
lookup      = [[[None]*2 for _ in range(10)] for _ in range(10)]
carry_out   = [[[0]*2      for _ in range(10)] for _ in range(10)]

for d1 in range(10):
    for d2 in range(10):
        for cin in range(2):
            s = d1 + d2 + cin         # 0‑19
            lookup[d1][d2][cin]    = digits[s % 10]
            carry_out[d1][d2][cin] = 1 if s >= 10 else 0



# Now adding strings is just table look‑ups—no character‑to‑number arithmetic at all:





def addStrings(a: str, b: str) -> str:
    # 1. Make same length (pad with '0' on the left)
    if len(a) < len(b):
        a = a.zfill(len(b))
    else:
        b = b.zfill(len(a))

    carry = 0
    out   = []

    # 2. Walk from right‑most digit to left
    for i in range(len(a) - 1, -1, -1):
        d1 = ord(a[i]) - 48           # *only here* we touch ASCII once,
        d2 = ord(b[i]) - 48           # you can replace these two lines
                                      # by digits.find(a[i]) if even that
                                      # small ord() bothers you.
        out.append(lookup[d1][d2][carry])
        carry = carry_out[d1][d2][carry]

    if carry:
        out.append('1')

    # 3. Reverse because we filled from LSD → MSD
    return ''.join(reversed(out))



# That single—in‑loop—ord() can itself be eliminated if you really want zero built‑ins (replace with digits.find(a[i]), which is still O(1) thanks to the fixed 10‑char string).

# Why this is “different”
# The core addition step is just a dictionary / list lookup, not arithmetic.

# All digit‑to‑digit work happens once up‑front in the table, not inside the main loop.










# logic 2

#  – “Chunk” addition (add 6 or 7 digits at a time)
# If you don’t mind small int conversions (they’re well under 2³¹ or 2⁶³), you can slice the strings into fixed‑width chunks, add them as normal integers, and manage the carry between chunks.

# Take chunks of k = 6 digits (max value 999 999 < 1 000 000 = 1 M < 2³¹).

# Start from the right, just like manual addition.

# Each chunk’s sum is at most 999 999 + 999 999 + 1 = 1 999 999 (needs 7 digits), so carry is at most 1.




def addStringsChunked(a: str, b: str, k: int = 6) -> str:
    carry = 0
    res_chunks = []

    while a or b:
        # Last k chars, or full remaining substring if shorter
        chunk_a, a = a[-k:], a[:-k]
        chunk_b, b = b[-k:], b[:-k]

        # Convert those tiny chunks to int safely
        s = (int(chunk_a) if chunk_a else 0) + \
            (int(chunk_b) if chunk_b else 0) + carry

        res_chunks.append(str(s % (10**k)).zfill(k))  # keep k digits
        carry = s // (10**k)

    if carry:
        res_chunks.append(str(carry))

    # Join, but the left‑most chunk may have leading zeros → lstrip them
    res_chunks = res_chunks[::-1]
    res_chunks[0] = res_chunks[0].lstrip('0') or '0'
    return ''.join(res_chunks)



# Why this is “different”
# The main loop works with integers ≤ 1 000 000, never with large ints.

# We only parse tiny slices, so we stay within the “no big‐int” rule.











# Logic 3

# Align:
#   99
# + 02  (pad with leading 0s)
# -----
#  101

# Left to right:
# Step 1: 9 + 0 = 9 → hold
# Step 2: 9 + 2 = 11 → now we know Step 1 must carry → fix Step 1 to 0, Step 2 = 1
# Step 3: No more digits, but we have carry = 1 → add to front




def addStringsLeftToRight(num1, num2):
    # Pad shorter string with zeros on the left
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)

    char_to_digit = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    digit_to_char = ['0','1','2','3','4','5','6','7','8','9']

    carry = 0
    result = []
    pending = None

    for i in range(max_len):
        d1 = char_to_digit[num1[i]]
        d2 = char_to_digit[num2[i]]
        total = d1 + d2 + carry
        digit = total % 10
        carry = total // 10

        if pending is not None:
            result.append(digit_to_char[pending])

        pending = digit

    # Add the last pending digit
    if carry:
        result.append(digit_to_char[carry])
    result.append(digit_to_char[pending])

    return ''.join(result)





# We process digits from left to right, but don’t immediately write output. Instead:

# Keep a carry from the previous step.

# Store each digit output in a buffer.

# At each step, only finalize the digit two steps behind — because only then we’re sure we won’t get carry from the future.

