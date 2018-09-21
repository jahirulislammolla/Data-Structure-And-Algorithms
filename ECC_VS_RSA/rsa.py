from datetime import datetime
while True:
    try:
        a, b = int(input("First Prime number : ")), int(input("Second Prime number : "))
        x = []
        y=[]
        n = (a - 1) * (b - 1)
        mod=a*b
        count=0
        for i in range(2, n):
            c, d = n, i
            while c % d != 0:
                c,d=d,c%d
            if d==1:
                x.append(i)
                count+=1
            if count==5:
                break
        for i in x:
            p=1
            while True:
                if (i * p) % n == 1:
                    break
                p += 1
            y+=[[i,p]]
        print(y)
        encrypt_key=int(input("Encryption Key : "))
        plain_text=input("Enter plaintext : ")
        chiper_text=''
        t1 = datetime.now()
        for i in  plain_text:
            ascii_code=ord(i)
            val=(ascii_code**encrypt_key)%mod
            chiper_text+=chr(val)
        t2 = datetime.now()
        print("Chiper text : "+chiper_text)
        print("Execution time : " +str((t2-t1).microseconds))
        plain_text=''
        decrypt_key=int(input("Decryption key : "))
        t1 = datetime.now()
        for i in chiper_text:
            ascii_code=ord(i)
            val=(ascii_code**decrypt_key)%mod
            plain_text+=chr(val)
        t2 = datetime.now()
        print('Plain text : '+plain_text)
        print("Execution time : "+str((t2-t1).microseconds))
    except ValueError:
        break
