# BoilCTF
IP: 10.10.8.187
<br>
First of all went to the ip in the browser and found apache2 server running. Then I went to robot.txt and found some interesting stuff there:

```
User-agent: *
Disallow: /

/tmp
/.ssh
/yellow
/not
/a+rabbit
/hole
/or
/is
/it

079 084 108 105 077 068 089 050 077 071 078 107 079 084 086 104 090 071 086 104 077 122 073 051 089 122 085 048 077 084 103 121 089 109 070 104 078 084 069 049 079 068 081 075
```

Interesting pages on joomla/:
- _test
- administrator
- build
- tests

```
MYSQL_DATABASE: joomla_ut
     MYSQL_USER: joomla_ut
     MYSQL_PASSWORD: joomla_ut
     MYSQL_ROOT_PASSWORD: joomla_ut
```

Joomla version is: 3.9.12

> Joomla! Core 1.5.0 - 3.9.4 - Directory Traversal / Authenticated Arbitrary File Deletion 
> Joomla! 3.9.0 < 3.9.7 - CSV Injection

tests/codeception/\_support/Shared/UserCredentials.php

http://boilctf.thm/joomla/media/editors/

```
codemirror/
none/
tinymce/
```

![log.txt](./imgs/log.txt.png)