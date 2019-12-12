import hashlib
import time
import datetime

ts = int(time.time())
ts_s = str(time.time()).encode('utf-8')
password = "engagingAfterburners".encode('utf-8')

hash = hashlib.sha256()
hash.update(password)
hash.update(ts_s)

# print (hash)
# print (hash.hexdigest()[:10])
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
        </p>

 </body>
</html>"""

output = open("key.html","w+")
output.write(string1)
output.close()

output = open("key.html","a+")
output.write(hash.hexdigest()[:10])
output.write(string2)
output.close()