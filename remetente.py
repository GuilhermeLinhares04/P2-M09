import sys
payload = sys.argv[1]

def bit_stuffing(data):
    stuffed = data.replace("11111", "111110")
    return stuffed
stuffed_payload = bit_stuffing(payload)

def hamming_encode(block):
    # Calcula bits de paridade p1, p2, p3
    d = [int(bit) for bit in block]
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    return f"{p1}{p2}{d[0]}{p3}{d[1]}{d[2]}{d[3]}"

hamming_blocks = [hamming_encode(stuffed_payload[i:i+4]) for i in range(0, len(stuffed_payload), 4)]
encoded_payload = ''.join(hamming_blocks)

frame = "01111110" + encoded_payload + "01111111"
print(frame, flush=True)  # Envia para stdout