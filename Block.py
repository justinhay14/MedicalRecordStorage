import hashlib
import time

class Block:
    def __init__(self, prevHash, records):
        self.prevHash = prevHash
        self.records = records
        self.timestamp = str(int(time.time() + 980347))[2:]
        hash = hashlib.sha256()
        hash.update(str(self).encode("utf-8"))
        self.hash = hash.hexdigest()