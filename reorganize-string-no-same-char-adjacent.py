https://leetcode.com/problems/reorganize-string/description/

class Solution:
    """
    The idea is to build a max heap with freq. count
a) At each step, we choose the element with highest freq (a, b) where b is the element, to append to result.
b) Now that b is chosen. We cant choose b for the next loop. So we dont add b with decremented value count immediately into the heap. Rather we store it in prev_a, prev_b variables.
c) Before we update our prev_a, prev_b variables as mentioned in step 2, we know that whatever prev_a, prev_b contains, has become eligible for next loop selection. so we add that back in the heap.

In essence,

at each step, we make the currently added one ineligible for next step, by not adding it to the heap
at each step, we make the previously added one eligible for next step, by adding it back to the heap
    """
    def reorganizeString(self, S: str) -> str:
        from collections import Counter
        import heapq
        # for aab => pq = [(-2,a),(-1,b)]
        # DOING NETAGIVE FOR MIN HEAP USAGE OF HEAPQ
        pq = [(-value, key) for key, value in Counter(S).items()]
        heapq.heapify(pq)
        prev_freq, prev_char, result = 0, '', ''

        while pq:
            freq, char = heapq.heappop(pq)
            result += char

            if prev_freq < 0:
                heapq.heappush(pq, (prev_freq, prev_char))

            prev_freq, prev_char = freq+1, char

        if len(result) != len(S): return ""
        return result
