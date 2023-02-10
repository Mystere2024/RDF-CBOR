
from CborEncoder import CBOREncoder
from CurieEncoder import curieEncoder
from cbor2 import dumps, CBORTag 
from rdflib import Namespace, term, Literal, XSD

class typedLiteralEncoder(CBOREncoder):
    """
    The typedLiteralEncoder encodes
    "a1b2c3d4"^^ex:myType
    330([a1b2c3d4, 320([5, "myType"]])
    
    """
    def __init__(self, value, prefix, suffix):
        CBOREncoder.__init__(self)
        self.value = value
        self.prefix = prefix
        self.suffix = suffix
    
    def get_value(self):
        encoded_tag = self.get_tag("typedLiteral") #330
        term_type = curieEncoder(self.prefix, self.suffix).get_value()   #320([5, "myType"]
        encoded_value = dumps(CBORTag(encoded_tag, [self.value, term_type]))
        return encoded_value


a = Literal(39, datatype=XSD.integer)
value = a.value 
print (a.datatype)
prefix, suffix = a.datatype.rsplit("#", 1)
print(prefix)

encoded = typedLiteralEncoder(a.value,prefix, suffix)

print(encoded.get_value().hex())