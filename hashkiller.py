import hashlib
def encrypt(text,hashtype):
	text = text.encode("utf-8")
	hash_hash = hashlib.new(hashtype)
	hash_hash.update(text)
	return hash_hash.hexdigest()
def read1(filename):
	file = open(filename,"r")
	return file.readlines()
print("1-TO encrypt text")
print("2-TO decrypt text")
print("3-Exit")
try:	
	enter = int(input("Enter the number of the option: "))
	if enter == 1:
		text = str(input("Enter your text: "))
		the_hash_type = str(input("Enter the hashtype: "))
		print("\n")
		print(encrypt(text,the_hash_type))
	elif enter == 2:
		hash_hash = str(input("Enter the hash: "))
		wordlist = str(input("Enter name of wordlist: "))
		the_hashtype = str(input("Enter the hash type: "))
		print("\n")
		alltext = read1(wordlist)
		for i in alltext:
			i = i.rstrip("\n")
			encrypt_text = encrypt(i,the_hashtype)
			if encrypt_text == hash_hash:
				print("[Hash: {} = Value: {}]".format(encrypt_text,i))
				break
			else:
				print("Faild")
	elif enter == 3:exit(code=None)
	else:print("the number that you choose was not in the list")
except KeyboardInterrupt:
	print("\n")
	print("Error in Input")
except ValueError:
	print("\n")
	print("Error in the Value")
except:
	print("\n")
	print("Error !")