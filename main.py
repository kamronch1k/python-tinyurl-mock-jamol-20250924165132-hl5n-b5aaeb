import hashlib
s='jamoltool'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
