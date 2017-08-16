#font https://codereview.stackexchange.com/questions/108057/simplified-des-encryption
from steganography import steganography
from s_des import s_des

if (__name__ == '__main__'):
    img = steganography.steganography('ola')
    x = '12345'
    x = x[1:] + x[0]
    print(x)

    
    print(s_des.key1('1010000010'))
    print(s_des.key2('1010000010'))
    #print(s_des.getLeft('123456'))
