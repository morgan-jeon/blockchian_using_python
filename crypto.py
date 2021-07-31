import hashlib

class crypto:
    def hexhash(content):
        encoding = 'utf-8'
        return hashlib.sha256(content.encode(encoding)).hexdigest()