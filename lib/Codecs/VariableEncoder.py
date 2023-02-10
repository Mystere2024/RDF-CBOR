from CborEncoder import CBOREncoder
from cbor2 import dumps, CBORTag 

class VariableEncoder(CBOREncoder):
    lindex= 0
    def __init__(self):
        CBOREncoder.__init__(self)
        VariableEncoder.lindex += 1
        self.index = VariableEncoder.lindex
    
    def get_value(self):

        # Add the variable category tag
        encoded_tag = self.get_tag("variable")
        # Add the local index
        encoded_value = self.index
        tagged_Value = dumps(CBORTag(encoded_tag,encoded_value))

        return tagged_Value

#v = VariableEncoder()
#v2 = VariableEncoder()

#print(v.get_value().hex())
#print(v2.get_value().hex())
