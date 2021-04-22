import hashlib
hash_object = hashlib.sha512(b'Hello World')
import hashlib
v = [b"mama", b"papa", b"dick", b"upload", b"telephone"]
d = []
hex_dig = hash_object.hexdigest()
for i in v:
    hash = hashlib.sha512(i)
    d.append(hash.hexdigest())

print(d)
