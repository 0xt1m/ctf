# Ignite

IP = 10.10.68.248

I went to an admin page using default creds which was admin:admin.<br>
We can try to upload a new page with php script to create a reverse shell.<br>
But there is an easier way. We know that this is *Fuel CMS 1.4* if you google it you will immediately find an exploit. I downloaded the first one and used:<br>
`python3 50477.py -u http://ignite.thm`<br>
Now I'm gonna set a listener on port 4444 on my host machine<br>
`nc -lvnp 4444`<br>
Then I found a php reverse shell that you can find in the same folder. Then I set up python http server, got it to the victim's machine, accessed it via web-browser and got a reverse-shell.<br>
if we go to */home/www-data* we will find our first flag there.<br>
Now we need to find a way to escalate our privileges.