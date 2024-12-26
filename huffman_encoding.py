from collections import Counter
import heapq


def huffman_encode(text):
    class Node:
        def __init__(self, char, freq, left=None, right=None):
            self.char, self.freq, self.left, self.right = char, freq, left, right

        def __lt__(self, other): return self.freq < other.freq

    freq = Counter(text)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        a, b = heapq.heappop(heap), heapq.heappop(heap)
        heapq.heappush(heap, Node(None, a.freq + b.freq, a, b))

    def build_codes(node, prefix="", code={}):
        if node.char:
            code[node.char] = prefix
        else:
            build_codes(node.left, prefix + "0", code); build_codes(node.right, prefix + "1", code)
        return code

    codes = build_codes(heap[0])
    encoded = ''.join(codes[c] for c in text)
    print(len(codes), len(encoded))
    print('\n'.join(f"'{c}': {code}" for c, code in sorted(codes.items())))
    print(encoded)


huffman_encode("Errare humanum est.")
