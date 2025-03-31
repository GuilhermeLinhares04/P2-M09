import sys
frame = sys.stdin.read().strip()

start = frame.find("01111110") + 8
end = frame.find("01111111")
encoded_payload = frame[start:end]

def bit_unstuffing(data):
    unstuffed = data.replace("111110", "11111")
    return unstuffed
unstuffed_payload = bit_unstuffing(encoded_payload)

def hamming_correct(block):
    bits = [int(bit) for bit in block]
    p1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6]
    p2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6]
    p3 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6]
    syndrome = p3 * 4 + p2 * 2 + p1
    
    if syndrome != 0:
        bits[syndrome - 1] ^= 1  # Corrige o bit errado
    return f"{bits[2]}{bits[4]}{bits[5]}{bits[6]}"

# Divide em blocos de 7 bits e decodifica
decoded = []
for i in range(0, len(unstuffed_payload), 7):
    block = unstuffed_payload[i:i+7]
    decoded_block = hamming_correct(block)
    decoded.append(decoded_block)
original_payload = ''.join(decoded)
print(original_payload)