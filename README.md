# Global Description of the library

This library implements a CBOR-based serialiation of RDF graphs and datasets. Concise Binary Object Representation [CBOR](https://cbor.io/) is a binary data format designed to optimize data exange, storing, and prossing within constrained devices. 


The library ensures two features:

- Encoding input RDF data serialized in (N3, turtle, trig, json-ld..) into a Cbor binary file. The structure of the Cbor file follows one of the following specifications: 
  1.  CBOR-LD [CBOR-LD](https://docs.google.com/document/d/1m62Rr1ul3REZc1Fkp7_cHWluX3wxgS0y1hJXHy33L2E/edit#heading=h.r0k9vsrl1zt4) 
  2.  RDF/CBOR  [RDF-CBOR](https://openengiadina.codeberg.page/rdf-cbor/)
  3.  COSWOT [COSWOT] [Draft in progress here] () is a mixed version of preivous spefications. It allows an encoding independetly from the input serialization and produces a CBOR-based data file. Cbor bytes are structured as arraysx each for a triple ([s, p, o]), a named graph ([g,[s,p,o], [s1,p1,o1],....[sn,pn,on]]), or a dataset [d]. 


- Decoding a CBOR bytes as RDF data. A target serialization can be spefied as an option (turtle, trig, json-ld,...). 


## Examples of encoding options

| RDF data | CBOR-LD | RDF-CBOR  | COSWOT |
|----------|----------|----------|----------|
| CURIE |     |     |       |
| BNODE |     |     |       |
| Variable |  tagged-value 2019(local_index)   |  NS.   |   tagged-value 2019(local_index)     |
| xsd:DateTime |     |     |       |
| xsd:Int |     |     |       |
| ....... |     |     |       |

## Running Examples

