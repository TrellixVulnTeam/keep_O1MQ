from module_codecs.codecs_to_hex import to_hex


text = "中国"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")

print("Original: ", repr(text))
print("Encoded: ", to_hex(encoded, 1), type(encoded))
print("Decoded: ", repr(decoded), type(decoded))
