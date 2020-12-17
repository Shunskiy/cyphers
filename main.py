import numpy as np
import random

def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)
    
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
    
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def BGW_enc(p, q, a, b, x, m):
    n = p * q

    assert a*p + b*q == 1

    k = int(np.log2(n))
    h = int(np.log2(k))

    t = len(m) / h
    t = int(t)

    xi = x
    c = ''
    for i in range(t):
        mi = m[i*h:(i + 1)*h]
        xi = (xi ** 2) % n
        xi_bin = bin(xi)
        pi = xi_bin[-h:]

        mi_int = int(mi, 2)
        pi_int = int(pi, 2)

        ci = pi_int ^ mi_int
        ci_bin = format(ci, '0' + str(h) + 'b')
        c += ci_bin

    xt = (xi ** 2) % n
    return c, xt
        
    

def BGW_dec(p, q, a, b, xt, c):
    n = p * q
    
    k = int(np.log2(n))
    h = int(np.log2(k))

    t = int(len(c) / h)
    
    d1 = (((p + 1) / 4)**(t + 1)) % (p - 1)
    d1 = int(d1)
    d2 = (((q + 1) / 4)**(t + 1)) % (q - 1)
    d2 = int(d2)

    u = (xt**d1) % p
    v = (xt**d2) % q

    x0 = (v*a*p + u*b*q) % n

    xi = x0
    m = ''
    for i in range(t):
        ci = c[i*h:(i + 1)*h]
        xi = (xi**2) % n
        xi = int(xi)
        xi_bin = bin(xi)
        pi = xi_bin[-h:]
        ci_int = int(ci, 2)
        pi_int = int(pi, 2)

        mi = pi_int ^ ci_int
        mi_bin = format(mi, '0' + str(h) + 'b')
        m += mi_bin

    return m



if __name__ == "__main__":
    reserv = 1
    
    while reserv:
        print("Encrypt, Decrypt, eXit(e/d/x): ")
        check = input()
        if check == "e":
            m = str(input("Enter plaintext: " ))
            m = str(text_to_bits(m))
            p = int(input("Enter p: "))
            q = int(input("Enter q: "))
            x0 = random.randint(10, p*q)
            _, a, b = gcd_extended(p, q)
            c, xt = BGW_enc(p, q, a, b, x0, m)
            print ("ciphertext:", c, "final x: ", xt)
        elif check == "d":
            c = str(input("Enter cipher: " ))
            p = int(input("Enter p: "))
            q = int(input("Enter q: "))
            x0 = random.randint(10, p*q)
            _, a, b = gcd_extended(p, q)
            xt = int(input("Enter final x: "))
            d = str(BGW_dec(p, q, a, b, xt, c))
            d = text_from_bits(d)
            print("plaintext:", d)
        elif check == "x":
            reserv = 0
        else:
            cls()
        
    
