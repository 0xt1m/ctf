# Privilege Escalation

## Linux
`getcap -r / 2>/dev/null`<br>
`find / -perm -u=s -type f 2>/dev/null`<br>
`find -writable 2>/dev/null | cut -d "/" -f 2 | sort -u`<br>
`find / -writable 2>/dev/null | grep home | cut -d "/" -f 2,3 | sort -u`<br>
`sudo -V` to check sudo version, which might be vulnerable.<br>

https://gtfobins.github.io/<br>
linpeas.sh<br>

Get Privilege Escalation vectors:<br>
- LinPeas: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS<br>
- LinEnum: https://github.com/rebootuser/LinEnum<br>
- LES (Linux Exploit Suggester): https://github.com/mzet-/linux-exploit-suggester<br>
- Linux Smart Enumeration: https://github.com/diego-treitos/linux-smart-enumeration<br>
- Linux Priv Checker: https://github.com/linted/linuxprivchecker<br>

## Windows
