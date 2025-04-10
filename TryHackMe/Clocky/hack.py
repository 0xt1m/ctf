import datetime
import hashlib

TIME_DIFFERENCE = datetime.timedelta(hours=4)

def generate_possible_hashes(username, debug=False):
    current_time = datetime.datetime.now() - TIME_DIFFERENCE
    possible_hashes = []
    for i in range(10):
        for j in range(1000):  # Consider milliseconds
            value = current_time - datetime.timedelta(seconds=i, milliseconds=j)
            lnk = str(value)[:-4] + " . " + username.upper()
            lnk_hash = hashlib.sha1(lnk.encode("utf-8")).hexdigest()
            possible_hashes.append(lnk_hash)
            if debug:
                print(f"Debug: Generated hash for {lnk}")
                print(f"Debug: Hash value: {lnk_hash}")
    return possible_hashes

def save_hashes_to_file(username, hashes):
    file_name = username + ".out"
    with open(file_name, "w") as file:
        for hash_value in hashes:
            file.write(hash_value.strip() + "\n")

def main():
    debug = input("Enable debugging? (y/n): ").lower() == 'y'
    username = input("Enter the username: ")
    if debug:
        print(f"Debug: Debugging mode enabled.")
    possible_hashes = generate_possible_hashes(username, debug)
    print("Possible SHA-1 hashes generated in the last 10 seconds:")
    for hash_value in possible_hashes:
        print(hash_value)
    save_hashes_to_file(username, possible_hashes)
    print("Hashes saved to", username + ".out")

if __name__ == "__main__":
    main()