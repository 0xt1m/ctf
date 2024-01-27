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