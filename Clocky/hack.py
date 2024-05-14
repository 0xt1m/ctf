import datetime
import hashlib

username = "charlie"

value = datetime.datetime.now()
lnk = str(value)[:-4] + " . " + username.upper()
lnk = hashlib.sha1(lnk.encode("utf-8")).hexdigest()

print(lnk)