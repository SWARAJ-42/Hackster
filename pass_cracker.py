import hashlib

def password_cracker(Hash_type, file_path, hash_to_decrypt):
    print("\n[+] Started Hash Password Cracker")
    Hash_type = Hash_type.strip()
    with open(file_path, 'r') as file:
        for line in file.readlines():
            if Hash_type == 'md5':
                hash_object = hashlib.md5(line.strip().encode())
                hashed_word = hash_object.hexdigest()
                if hashed_word == hash_to_decrypt:
                    print(f"[+] Found MD5 Password: {line.strip()}")
                    return

            if Hash_type == 'sha1':
                hash_object = hashlib.sha1(line.strip().encode())
                hashed_word = hash_object.hexdigest()
                if hashed_word == hash_to_decrypt:
                    print(f"[+] Found SHA1 Password: {line.strip()}")
                    return
            
            if Hash_type == 'sha256':
                hash_object = hashlib.sha256(line.strip().encode())
                hashed_word = hash_object.hexdigest()
                if hashed_word == hash_to_decrypt:
                    print(f"[+] Found SHA256 Password: {line.strip()}")
                    return

        print("Password not in the file !")