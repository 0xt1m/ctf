# Blog

IP: 10.10.152.91<br>

First of all, I have done an Nmap scan. Here are key points of information that I found:<br>
Windows, WordPress 5.0<br>
browsing the website, here are the usernames that I found:<br>
`kwheel`<br>
`bjoel`<br>
This information might also be useful.<br>
Then I used `smbmap -H blog.thm` to see the shares on the specified host.<br>
```
[+] Guest session       IP: blog.thm:445        Name: unknown                                           
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        print$                                                  NO ACCESS       Printer Drivers
        BillySMB                                                READ, WRITE     Billy's local SMB Share
        IPC$                                                    NO ACCESS       IPC Service (blog server (Samba, Ubuntu))
```

So we can see that we have the permissions to read and write on *BillySMB*<br>
`smbclient //blog.thm/BillySMB -U guest`<br>
I used this command to connect to it. I found a couple of files there.<br>
I tried using `stegseek` to find extract something but found myself in a rabbit hole.<br>
Therefore, we literally found nothing.<br>
I went back to the WordPress site, took the first username that I found, and successfully tried to brute-force it.
```
[!] Valid Combinations Found:
 | Username: kwheel, Password: cutiepie1
```

If we do a little research we will find that WordPress 5.0 has vulnerable functions related to images. Something with crop images. We can look for exploits on the internet, but I went to metasploit and found one there.<br>
`multi/http/wp_crop_rce`<br>
Set all the required options, run and here we go.<br>
I created one more shell just to make sure everything would be okay.<br>
I went to `/home/bjoel` and found there `user.txt` but there was no flag. :( <br>
I guessed that the user flag was in `/media/usb` but that give me nothing because I didn't have access to the usb folder.<br>
After many unsuccessful tries to escalate my privileges, I ran `linpeas.sh` and it told me that I could use `[CVE-2021-3156] sudo Baron Samedit` so I googled it, downloaded the script, ran it on the victim's machine and easily got root.

:::success
Just want to check something out
:::
