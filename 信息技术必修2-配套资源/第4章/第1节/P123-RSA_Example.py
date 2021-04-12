
# coding: utf-8

# In[1]:

# 从SymPy中导入RSA公钥模块
from sympy.crypto.crypto import rsa_public_key


# In[2]:

# p, q是两个不同的素数，e与(p-1)(q-1)互素（没有异于1和自身的公因子）
p, q, e = 3, 5, 7


# In[3]:

# 生成公钥(n,e)，其中n = pq. 
rsa_public_key(p, q, e)


# In[4]:

# 若上面的任何假定不满足，则返回False。
rsa_public_key(p, q, 30)


# In[5]:

# 从SymPy中导入RSA私钥模块
from sympy.crypto.crypto import rsa_private_key


# In[6]:

# p, q是两个不同的素数，d与e模(p-1)(q-1)互逆，即de = 1 (mod (p-1)(q-1)).
p, q, e = 3, 5, 7


# In[7]:

# 生成公钥(n,d)，其中n = pq. 
rsa_private_key(p, q, e)


# In[8]:

# 若上面的任何假定不满足，则返回False。
rsa_private_key(p, q, 30)


# In[14]:

from sympy.crypto.crypto import encipher_rsa, rsa_public_key

# 准备公钥，选取p,q两个不同素数。
p, q, e = 13, 5, 7

# 生成公钥pub_key
pub_key = rsa_public_key(p, q, e)

# 待加密的明文消息
msg = 12

# 使用公钥pub_key对明文进行加密
encipher_rsa(msg, pub_key)


# In[15]:

from sympy.crypto.crypto import decipher_rsa, rsa_private_key
p, q, e = 13, 5, 7

# 生成私钥pri_key
pri_key = rsa_private_key(p, q, e)

# 待解密的密文消息
msg = 38

# 使用私钥pri_key对密文进行解密
decipher_rsa(msg, pri_key)

