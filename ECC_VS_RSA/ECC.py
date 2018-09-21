from datetime import datetime
while True:
    try:
        # y ^ 2 = x ^ 3 + ax + b .....Elliptic Curve Cryptography
        public_Prime=int(input("Public prime : "))
        public_value=int(input("Public Generator Point : "))
        a=int(input("Private key Alice = "))
        b=int(input("Private key Bob = "))
        x=(public_value**a)%public_Prime
        y=(public_value**b)%public_Prime
        print("Public key alice : "+str(x))
        print("Public key bob :"+str(y))
        plain_text=input("Enter chiper text : ")
        ka = (y ** a) % public_Prime
        kb = (x ** b) % public_Prime
        encrypt_text=''
        print("Secret share key for the Alice is "+ str(ka))
        t1 = datetime.now()
        for i in plain_text:
            x=ord(i)
            encrypt_text+=chr(x+ka)
        t2 = datetime.now()
        print(encrypt_text)
        print("Execution time : " + str((t2 - t1).microseconds))
        print()
        print("Secret share key for the Bob is " + str(kb))
        decrypt_text=''
        t1 = datetime.now()
        for i in encrypt_text:
            x=ord(i)
            decrypt_text+=chr(x-kb)
        t2 = datetime.now()
        print(decrypt_text)
        print("Execution time : " + str((t2 - t1).microseconds))
    except ValueError:
        break
