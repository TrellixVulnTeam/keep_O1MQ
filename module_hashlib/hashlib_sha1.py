import hashlib

from module_hashlib.hashlib_data import lorem

h = hashlib.sha1()
h.update(lorem.encode("utf-8"))
print(h.hexdigest())
