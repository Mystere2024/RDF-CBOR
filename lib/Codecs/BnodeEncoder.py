from CborEncoder import CBOREncoder
from cbor2 import dumps, CBORTag 

class bnodeEncoder(CBOREncoder):
    # This index generates an identifier for a the blank node (local increment)
    lindex= 0
    def __init__(self):
        CBOREncoder.__init__(self)
        bnodeEncoder.lindex += 1
        self.index = bnodeEncoder.lindex
    
    def get_value(self):

        # Add the variable category tag
        encoded_tag = self.get_tag("bnode")

        # Add the local increment (index)
        encoded_body = self.index
        encoded_tagged_value = dumps(CBORTag(encoded_tag,encoded_body))

        return encoded_tagged_value
