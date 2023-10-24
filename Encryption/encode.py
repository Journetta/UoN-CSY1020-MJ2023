import base64
string = open ("Encrypton.txt", 'r')
string2 = string.read()
string.close()
encoded_string = base64.b64encode(string2.encode("utf-8")).decode("utf-8")

print(encoded_string)