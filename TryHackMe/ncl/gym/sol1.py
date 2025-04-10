# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 2.7

import sys

def main():
    if len(sys.argv) != 2:
        print 'Invalid args'
        return None
    password = sys.argv[1]
    builder = 0
    for c in password:
        builder += ord(c)
    
    builder = builder << 2
    print("builder1:", builder)
    builder = ~builder
    print("builder2:", builder)
    builder = builder ^ 12648430
    print("builder3:", builder)
    builder = ~builder
    print("builder4:", builder)
    if builder != 12645638:
        print "numbers are wrong"
    if ord(password[0]) != 78:
        print 'First letter is wrong'
    if len(password) != 11:
        print 'password len is wrong'
    else:
        print 'incorrect'

if __name__ == '__main__':
    main()

# N999999999k