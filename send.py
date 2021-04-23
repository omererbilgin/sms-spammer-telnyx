import telnyx
import sys

telnyx.api_key = "KEY0178F16E51822582E984953ECBBF48B9_1gYddzeO4FWNim7LXwVBXt" #enter your api key here

path = 'numbers.txt'

your_telnyx_number = "+13115552368"
body = 'BODY TEXT GOES HERE'

with open(path) as fp:
   line = fp.readline()
   
   while line:
       print("Sending SMS to: {}".format(line.strip()))
       telnyx.Message.create(
             from_=your_telnyx_number,
             to=line.strip(),
             text=body,
       )
       line = fp.readline()




