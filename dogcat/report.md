# dogcat

We got site on port 80.<br>
We can notice that the url changes according to what we want to see.<br>
`http://dogcat.thm/?view=cat`<br>
I tried to change the value of view parameter to:<br>
`http://dogcat.thm/?view=../../../dog` and got interesting output.
```
Warning: include(../../../dog.php): failed to open stream: No such file or directory in /var/www/html/index.php on line 24

Warning: include(): Failed opening '../../../dog.php' for inclusion (include_path='.:/usr/local/lib/php') in /var/www/html/index.php on line 24
```

### Make some conclusions
When we put our request in the *view* param it takes the word and tries to find a file with name of our value plus extenstion php. Adding `../../` changes working directory. We get the error and that is good because it means that we got LFI there. However, not everything is so easy, the app checks the value if view so it can be only _cat_ or _dog_.<br>
To bypass it we can just put the first word `dog` in the value and that look for what we want. The next problem is that it adds `.php` in the end so we cannot just open everything we want.<br>

This is a good one so I am going to use write-up to learn new things.<br>
https://fmash16.github.io/content/writeups/tryhackme/thm-DogCat.html