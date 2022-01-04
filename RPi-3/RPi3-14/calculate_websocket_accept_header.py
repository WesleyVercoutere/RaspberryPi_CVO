import hashlib, base64

Sec_WebSocket_Key = input("enter Sec-WebSocket-Key:")

#Sec_WebSocket_Key = "dGhlIHNhbXBsZSBub25jZQ=="

h = hashlib.sha1((Sec_WebSocket_Key + "258EAFA5-E914-47DA-95CA-C5AB0DC85B11").encode())
print ("hexdigest:", h.hexdigest()) # hexadecimal string representation of the digest
print ("digest:", h.digest()) # raw binary digest

print ()
print ("right result:", base64.b64encode(h.digest()))
