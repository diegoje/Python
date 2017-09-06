"""
Unix Password Cracker
//NOTE if you are getting a problem where your program says Password Not Found
//but your code is correct, try copying the words from the dictionary.txt file and pasting them in a new dictionary.txt file
// mediafire changes the .txt files encoding to a non python friendly format.
"""
import crypt
import optparse


def test_pass(crypt_pass, dname):
    salt = crypt_pass[0:2]
    dict_file = open(dname, 'r')
    for word in dict_file.readlines():
        word = word.strip()
        crypt_word = crypt.crypt(word, salt)
        if crypt_word == crypt_pass:
            print("[+] Found Password: " + word + "\n")
            return
    print('[-] Password Not Found.\n')
    return


def main():
    parser = optparse.OptionParser("usage %prog " + "-f <passwordFile> -d <dictionary>")
    parser.add_option('-f', dest='pname', type='string', help='specify password file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.pname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        pname = options.pname
        dname = options.dname

    pass_file = open(pname, 'r')
    for line in pass_file.readlines():
        if ":" in line:
            user = line.split(':')[0]
            crypt_pass = line.split(':')[1].strip(' ')
            print("[*] Cracking Password For: " + user)
            test_pass(crypt_pass, dname)


if __name__ == '__main__':
    main()

