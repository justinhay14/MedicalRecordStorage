from Block import Block

class Blockchain:
    def __init__(self):
        genesisBlock = Block(0, ["genesis block"])
        self.chain = [] + genesisBlock
        self.previousBlock = genesisBlock