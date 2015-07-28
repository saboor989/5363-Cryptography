###############################################
# Name      : SABOOR AHMED SIDDIQIE
# Class     : CMPS 5363 Cryptography
# Date      : 28 July 2015
# Program 2 : Vigenere Cipher
###############################################

import argparse
import sys
import randomized_vigenere as rv

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")

    args = parser.parse_args()

    #replacing / with \ in the file path
    address=args.outputFile    
    matrixtext=address.replace('\\','/')

    
    if(args.mode == 'encrypt'):
        #Encryption method
        #opening a file for reading the message
        f = open(args.inputFile,'r')
        message = f.read()
        f.close()
    
        #calling the encrypt method for encrytion method present in random vigenere
        data = rv.encrypt(message,args.mode,args.seed)
        
        #opening the output file in write mode for writing the output
        o=open(args.outputFile,'w')
        o.write(str(data))
        o.close()

    else:
        #Decrypt method
        #opening the file in read mode to read the data
        f = open(args.inputFile,'r')
        message = f.read()
        f.close()
        
        #calling the decrypt method for decryption        
        data = rv.decrypt(message,args.mode,args.seed)
        
        #opening the file in write mode for writing the encrypted message
        o=open(args.outputFile,'w')
        o.write(str(data))
        o.close()

if __name__ == '__main__':
    main()
