from Config import prefixes, tags, curies



class CBOREncoder():
    """
    CBOREnCoder is the base Class
    It defines generic methods:
    
    - get_tag
    
    - get_prefix_index 
    
    - get_curie_index
    """

    def __init__(self):
        pass 

    # returns the int corresponding to an item category CBOR tag 
    def get_tag(self, item:str):
        if item in tags.keys():
            return tags[item] 
        else: 
            raise Exception(f"The item {item} has no corresponding tag ! ") 
    
    # returns the index of the prefix 
    def get_prefix_index(self, prefix:str):
        if prefix in prefixes.keys():
            return prefixes[prefix] 
        else: 
            raise Exception(f"The prefix {prefix} has no assigned index !") 
    
    # returns the idex of the curie
    def get_curie_index(self, curie:str):
        if curie in curies.keys():
            return curies[curie] 
        else: 
            raise Exception(f"The curie {curie} has no assigned index ! Consider using the get_prefix_index() !") 