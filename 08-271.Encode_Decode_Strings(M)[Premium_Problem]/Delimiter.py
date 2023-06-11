# input_str = ["lint","code","love","you"]
# encoded = "4#lint4#code4#love3#you"


def encode(strs):
    encoded_str = ""

    for each_str in strs:
        encoded_str += f"{len(each_str)}#{each_str}"

    return encoded_str  # 4#lint4#code4#love3#you


def decode(encoded_str):
    decoded, i = [], 0

    while i < len(encoded_str):
        j = i

        while encoded_str[j] != "#":
            j += 1

        length = int(encoded_str[i:j])

        i = j + 1

        decoded.append(encoded_str[i:i + length])

        i = i + length

    return decoded


encoded_string = encode(["lint", "code", "love", "you"])
print("Encoded string", encoded_string)
print("Decoded string", decode(encoded_string))
