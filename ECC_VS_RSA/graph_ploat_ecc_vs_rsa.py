import matplotlib.pyplot as plt
from datetime import datetime
plain_text="I love my country"
xx=[[11,5,10,20],[29,20,30,40],[43,50,35,100],[109,50,1000,2000],[191,100,2000,3000]]
yy=[[7,11,17,53],[23,29,15,575],[41,43,23,1607],[191,199,29,5189],[107,109,17,8081]]
time1=[]
time2=[]
for m in xx:
    t1 = datetime.now()
    public_Prime, public_value, a, b = m
    x = (public_value ** a) % public_Prime
    y = (public_value ** b) % public_Prime
    ka = (y ** a) % public_Prime
    kb = (x ** b) % public_Prime
    encrypt_text = ''
    for i in plain_text:
        x = ord(i)
        encrypt_text += chr(x + ka)
    decrypt_text = ''
    t1 = datetime.now()
    for i in encrypt_text:
        x = ord(i)
        decrypt_text += chr(x - kb)
    t2 = datetime.now()
    time1.append((t2 - t1).microseconds)
for m in yy:
    t1 = datetime.now()
    a,b,encrypt_key,decrypt_key= m
    x = []
    y = []
    n = (a - 1) * (b - 1)
    mod = a * b
    chiper_text = ''
    for i in plain_text:
        ascii_code = ord(i)
        val = (ascii_code ** encrypt_key) % mod
        chiper_text += chr(val)
    t2 = datetime.now()
    plai_text = ''
    for i in chiper_text:
        ascii_code = ord(i)
        val = (ascii_code ** decrypt_key) % mod
        plai_text += chr(val)
    t2 = datetime.now()
    time2.append((t2 - t1).microseconds)
print("ECC TIME :",time1)
print("RSA TIME :",time2)
plt.plot([1,2,3,4,5],time1,label='ECC')
plt.plot([1,2,3,4,5],time2,label='RSA')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title("ECC VS RSA")

plt.legend()

plt.show()
