# This script encodes an rdf graph  {(s, p, o)} , input in different serializations,into the RDF CBOR bytearray.


from rdflib import URIRef,Literal, BNode, XSD, namespace
from binascii import hexlify, unhexlify
from datetime import date, datetime, time
from Codecs.CurieEncoder import CurieEncoder
from Codecs.BnodeEncoder import BnodeEncoder
from Codecs.DateTimeEncoder import dateTimeEncoder
from Codecs.TypedLiteral import typedLiteralEncoder

def DatasetEncoder(InputDataset):
    # Default graph

    # Named graph

    pass


def GraphEncoder(InputGraph):
    # For each graph triple, extract RDF terms (subject, predicate, object)
    # RDF terms can be: URIs (Curies for prefixed URIs), Literals (typed or not), Blank nodes. 
    Encoded_Graph = bytearray()
    for s,p,o in InputGraph:
        encoded_subject = TermEncoder(s)
        encoded_predicate = TermEncoder(p)
        encoded_object = TermEncoder (o)
        EncodedTriple = encoded_subject + encoded_predicate + encoded_object
        Encoded_Graph.extend(EncodedTriple)
    
    return Encoded_Graph    

def TermEncoder(input_graph, input_term): 
    """
    This funion endes an rdf term (URIREF, BNODE, LITERAL) into its cbor representation.
    
    Parameters:
    input_graph (RDFlib Graph): The rdf graph ntaining the term.
    input_term (RDFlib term): The rdf term to be encoded in cbor.
    
    Returns:
    CBOR bytes: the cbor encoding of the input_term.
    """
    
    encoded_term = bytearray()

    if isinstance(input_term, URIRef):
        term = input_term.n3(input_graph.namespace_manager)
        prefix, suffix = term.rsplit(":", 1)
        encoded_term = CurieEncoder(prefix, suffix).get_encoded_value()

    elif isinstance(input_term, BNode):
        encoded_term = BnodeEncoder().get_value()
    
    elif isinstance(input_term, Literal):
        term_value = input_term.value
        term_type = input_term.datatype
        try:
            term_lang = input_term.language
        except: 
            pass

        if (term_type in XSD ):
            if term_type == XSD.integer:
                pass
            if term_type == XSD.string:
                pass
            if term_type == XSD.float:
                pass
            if term_type == XSD.boolean:
                pass
            else:
                raise Exception("Unsupported literal datatype")
        
        else: 
            term = term_type.n3(input_graph.namespace_manager)
            prefix, suffix = term.rsplit(":", 1)
            
            encoded_term = typedLiteralEncoder(term_value,prefix, suffix)

    else: 
        raise Exception ("Invalid RDF term !")

        # To DO: Handle concatenating the triples in (as a list ?)
        # To DO: Handle optimization regarding the repeated subjects and predicates
    return encoded_term

