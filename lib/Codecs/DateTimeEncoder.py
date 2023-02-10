# This codec encodes a xsd:DateTime 
from CborEncoder import CBOREncoder

from cbor2 import dumps, CBORTag 

from datetime import datetime

import time
from datetime import datetime

class dateTimeEncoder(CBOREncoder):
    def __init__(self, date_time):
        CBOREncoder.__init__(self)
        if not isinstance(date_time, datetime):
            raise TypeError("The argument must be a datetime object")
        self.datetime = date_time
    
    def get_value(self):

        seconds_epoch = int(time.mktime(self.datetime.timetuple()))
        datetime_tag = self.get_tag("datetime")
        encoded_tagged_value = dumps(CBORTag(1,seconds_epoch))

        return encoded_tagged_value


#t = datetime.now()
#print (t)

#et= dateTimeEncoder(t).get_value()
#print(et.hex())