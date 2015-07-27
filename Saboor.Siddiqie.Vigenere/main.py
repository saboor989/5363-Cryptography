import argparse
import sys
import randomized_vigenere as rv


#python3 main.py -m encrypt -seed 7487383487438734 -i plainText.txt -o encryptedText.txt
#
#C:\Users\saboor>python C:\Users\saboor\Desktop\cryptography\5363-Cryptography-Sa
#boor\Saboor.Siddiqie.Vigenere\main.py -m encrypt -i plainText.txt -o encryptedTe
#xt.txt -s 1234
#args.type
#the seed : encrypt
#args.inputfile,plaintext.txt
#C:\Users\saboor>

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", dest="seed",help="Integer seed")

    args = parser.parse_args()

    print("args.type")
    print("the seed :",args.mode)
    print("the seed :",args.inputFile)
    print("the seed :",args.outputFile)
    print("the seed :",args.seed)
    if(args.inputFile == 'plainText.txt'):
        print("args.inputfile,plaintext.txt")
    else:
        c=0
	
    #l=str(sys.argv)
    #print(l)
    
    f = open(args.inputFile,'r')
    message = f.read()
    #f.close()
    
    #o.write(str(data))
    if(args.mode == 'encrypt'):
        print("in the encrypt if :",message)
        #o = open(args.outputFile,'w')
        data = rv.encrypt(message,args.mode,args.seed)
        #o.write(str(data))
        #f.close()
        #o.close()
    else:
        print("In the decrypt :")
        #f = open(args.outputFile,'r')
        #o = open(args.inputFile,'w')
        #message = f.read()
        print("In the decrypt message:",message)
        data = rv.decrypt(message,args.mode,args.seed)
        #print("the data in decrypt is :",data)
        #o.write(str(data))
        #f.close()
        #o.close()
    #o = open(args.outputFile,'w')
    #o.write(str(data))


if __name__ == '__main__':
    main()
