import base64
import json


encoded_hostile_word = 'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT'
encoded_less_hostile_word = 'RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=='

def decoded(string:str):
    # Decode the Base64 string to bytes
    decoded_bytes = base64.b64decode(string)
    # Convert the bytes to a string (assuming UTF-8 encoding)
    decoded_string = decoded_bytes.decode('cp1252')
    return decoded_string


decoded_hostile_word = decoded(encoded_hostile_word)
decoded_less_hostile_word = decoded(encoded_less_hostile_word)

list_hostile_word = decoded_hostile_word.split(",")
list_less_hostile_word = decoded_less_hostile_word.split(",")

full_list = {
    "hostile":list_hostile_word,
    "less_hostile": list_less_hostile_word,
}

filename = "../../data/hostile_words.json"

# Open the file in write mode ("w") and use json.dump()
# The 'indent' parameter is optional but recommended for pretty-printing the JSON
with open(filename, "w") as f:
    json.dump(full_list, f, indent=4)

print(f"Decoded hostile_word: {list_hostile_word}")
print(f"Decoded less_hostile_word: {list_less_hostile_word}")