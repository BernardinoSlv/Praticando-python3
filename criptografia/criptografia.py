from random import randint, seed, random

class Cript(object):
    def __init__(self, name , password):
        self.name = name
        self.password = password
        self.key = self.key_generator()


    # this method will generate a random key
    def key_generator(self):
        size = 0
        for letter in self.name: size += ord(letter)
        seed(size)
        #print(size)
        key = ""
        seed(size)
        for count in range(len(self.password)):
            key += chr(randint(0, 255))
        return key

    
    # This method will encrypt the password
    def encrypt(self, default=True):
        cripher = ""
        for count in range(len(self.password)):
            n_password = ord(self.password[count])
            n_key = ord(self.key[count])
            total = (n_key ^ n_password)
            cripher += hex(total)
        self.password = cripher
        return self.password

    
    def hexconv(self):
        conv = "".join([chr(int(l, 16)) for l in self.password.split("0x") if len(l) >= 1])
        return conv

    
    # This method will decrypt the password
    def decrypt(self, default=True):
        conv = self.hexconv()
        decripher = "".join([str(chr(ord(self.key[p]) ^ ord(conv[p]))) for p in range(0, len(conv))])
        return decripher
    

    def save(self):
        with open("saida.txt", "wb") as file:
            file.write(self.password.encode())


if __name__ == "__main__":
    #name = str(input("Name: "))
    #password = str(input("Password: "))
    name = "B"
    password = "Man sei lá kkkkkkkk"
    print("="*70)
    c = Cript(name, password)
    print(password)
    print(c.encrypt())
    c.decrypt()
    print(c.decrypt())
    print("="*70)
