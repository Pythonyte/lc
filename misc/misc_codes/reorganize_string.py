def reorganize_string(S):
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

print(reorganize_string('aab'))
print(reorganize_string('aaab'))
print(reorganize_string('aaabcd'))
print(reorganize_string('bbccdd'))
print(reorganize_string('a'))