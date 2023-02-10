# This codec encodes a Curie (coswot:Something) into a bytearray object (DN: 320([1, "Something"]))
from CborEncoder import CBOREncoder

from cbor2 import dumps, CBORTag 

from rdflib import Graph, Literal, URIRef, namespace, XSD


class curieEncoder(CBOREncoder):
    def __init__(self, prefix, suffix):
        CBOREncoder.__init__(self)
        self.prefix = prefix
        self.suffix = suffix
    
    def get_value(self): 
        # Add the curie category tag
        encoded_tag = self.get_tag("curie")
        # check if it is a "well-known" curie
        curie = self.prefix + ":" + self.suffix
        try:
            encoded_value = self.get_curie_index(curie)
        except:
            try:
                # Add the prefix index
                encoded_value = [self.get_prefix_index(self.prefix), self.suffix ]
            except ValueError as e: 
                raise Exception(f"The curie {curie} is not handled!")
        
        encoded_tagged_value = dumps(CBORTag(encoded_tag,encoded_value))
        
        return encoded_tagged_value

a = curieEncoder("coswot","Something")
print (a.get_value().hex())
