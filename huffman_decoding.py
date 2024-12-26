def huffman_decode(encoded_data):
    lines = encoded_data.strip().split('\n')
    n, size = map(int, lines[0].split())
    codes = {}

    for line in lines[1:n + 1]:
        char, code = line.split(': ')
        char = char.strip("'")
        codes[code] = char

    encoded_string = lines[n + 1]
    decoded_string = ""
    buffer = ""

    for bit in encoded_string:
        buffer += bit
        if buffer in codes:
            decoded_string += codes[buffer]
            buffer = ""

    return decoded_string

encoded_data = """12 60
' ': 1011
'.': 1110
'D': 1000
'c': 000
'd': 001
'e': 1001
'i': 010
'm': 1100
'n': 1010
'o': 1111
's': 011
'u': 1101
100011110001001101000111111011001010011000010110011010111110"""

print(huffman_decode(encoded_data))
