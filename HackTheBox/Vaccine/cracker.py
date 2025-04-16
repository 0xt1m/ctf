import hashlib

target_hash = "2d58e0637ec1e94cdfba3d1c26b67d01"
username = "postgres"

with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin1") as wordlist:
    for line in wordlist:
        password = line.strip()
        first = hashlib.md5((password + username).encode()).hexdigest()
        final = hashlib.md5(first.encode()).hexdigest()
        print(password)

        if final == target_hash:
            print(f"[+] Password found: {password}")
            break
