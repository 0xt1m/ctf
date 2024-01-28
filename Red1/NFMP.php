<?php
   $file = $_GET['key'];
   if(isset($file))
   {
       include("$file");
   }
   else
   {
       include("NetworkFileManagerPHP.php");
   }
   /* VGhhdCBwYXNzd29yZCBhbG9uZSB3b24ndCBoZWxwIHlvdSEgSGFzaGNhdCBzYXlzIHJ1bGVzIGFyZSBydWxlcw== */
   /* That password alone won't help you! Hashcat says rules are rules */ 
?