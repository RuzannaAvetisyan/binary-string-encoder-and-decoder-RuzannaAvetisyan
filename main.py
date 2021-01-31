import re


def check_bits(s, search=re.compile(r'[^0-1.]').search):
    return not bool(search(s))


def encode(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def decode(bits, encoding='utf-8', errors='surrogatepass'):
    try:
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    except UnicodeDecodeError:
        return "Invalid input"


def commands():
    while True:
        command = input("Enter commands encode, decode or exit: ")
        if command == "encode":
            call_encode()
        if command == "decode":
            call_decode()
        if command == "exit":
            break


def call_encode():
    s = input("Enter any string: ")
    print(encode(s))


def call_decode():
    s = input("Enter any bits: ")
    if check_bits(s) and len(s) % 8 == 0:
        print(decode(s))
    else:
        print("Invalid input")


if __name__ == '__main__':
    commands()
