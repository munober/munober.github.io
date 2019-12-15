import hashlib
import time
from datetime import datetime

password = "engagingAfterburners" ## Password to hash

ts = int(time.time())
ts_s = str(time.time()).encode('utf-8')
timestamp = datetime.fromtimestamp(ts)

hash = hashlib.sha256(password.encode('utf-8'))
hash.update(ts_s) ## Adding timestamp as salt to hash
hash = hash.hexdigest()

### Prints for debugging
print ("Generated hash: ", hash)
# print(timestamp)

string = """<head>
    <!-- well done, little padawan -->
    <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
</head>

<html>
    <body>
        <img src="resources/pics_minions_santa_helpers.jpg" alt="pics_minions_santa_helpers" height="160">
        
        <p style="font-family: Arial, Helvetica, sans-serif;">
            (hash.hexdigest()[:10])    
            <br />
        </p>

 </body>
</html>"""

string1 = """<head>
    <!-- well done, little padawan -->
    <link rel="shortcut icon" type="image/x-icon" href="favicon.ico">
    <!-- <Cache-Control: no-store></Cache-Control:> -->
    <meta http-equiv="Cache-control" content = "No-cache">
</head>

<html>
    <body>
        <img src="resources/pics_minions_santa_helpers.jpg" alt="pics_minions_santa_helpers" height="160">
        
        <p style="font-family: Arial, Helvetica, sans-serif;">"""

string2 =             """<br />
            Timestamp: """
string3 = """<br />
        </p>
        

 </body>
</html>"""

output = open("key.html","w+")
output.write(string1)
output.close()

output = open("key.html","a+")
output.write(hash)
output.write("*")
output.write(string2)
output.write(str(timestamp))
output.close()

with open("generatedHash.txt","w+") as textfile:
    textfile.write(hash)
