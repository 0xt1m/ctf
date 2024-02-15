import hashlib

numbers = []

for first in range(10):
	for second in range(10):
		for third in range(10):
			for fourth in range(10):
				fourth_stage = str(first) + str(second) + str(third) + str(fourth)
				numbers.append(fourth_stage)


creds = []

# result = hashlib.md5(b'SKY-HQNT-8765')
# print(result.hexdigest())

for number in numbers:
	password = "SKY-HQNT-" + str(number)
	p_hash = hashlib.md5(password.encode('utf-8')).hexdigest()
	creds.append((password, p_hash))


while True:
	hash_input = input("Enter the hash: ")
	if hash_input == "stop":
		break
	else:
		for i in creds:
			if hash_input == i[0] or hash_input == i[1]:
				print(i)
