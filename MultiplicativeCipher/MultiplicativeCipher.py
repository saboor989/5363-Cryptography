import fractions
#import cryptoMath

from math import log
import time
import os
import sys
import re
import operator
import pprint



# Extended Euclidean algorithm
#   returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)



class Modgcd:
    
# Mod Inverse V1
#   returns the modular multiplicative inverse (x) of a and m.
#   where ax = 1 (mod m) (= means congruent here)
    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            #raise Exception('modular inverse does not exist')
            return None
        else:
            return x % m
            



            


class MultiplicativeCipher:

    SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    Ciphertext = ""
    Plaintext = ""

    def __init__(self,multiplier=1025,shifter=7):

        modgcd=Modgcd
        # If key sent in is not relatively prime with the length of
        # symbols then keep adding 1 until it is.
        while modgcd.modinv(multiplier,len(self.SYMBOLS)) == None:
            multiplier += 1

        # Set Multiplier to the possibly adjusted Multiplier
        self.Multiplier = multiplier
        self.Shifter = shifter

        print(self.Multiplier,self.Shifter)
        lengthofsymbol=len(self.SYMBOLS)
        # Get the inverse key using our mod inverse function
        self.InverseMultiplier = modgcd.modinv(self.Multiplier,lengthofsymbol)

    

            
    def encrypt(self,plaintext):
        #print("in encrypt")
        self.Ciphertext = ''
        for symbol in plaintext:
            if symbol in self.SYMBOLS:
                # encrypt this symbol
                symIndex = self.SYMBOLS.find(symbol)
                self.Ciphertext += self.SYMBOLS[(symIndex * self.Multiplier + self.Shifter) % len(self.SYMBOLS)]
            else:
                self.Ciphertext += symbol # just append this symbol unencrypted
        return self.Ciphertext

    def decrypt(self,ciphertext):
        #print("In decrypt : ",ciphertext)
        self.Plaintext = ''
        for symbol in ciphertext:
            if symbol in self.SYMBOLS:
                # encrypt this symbol
                symIndex = self.SYMBOLS.find(symbol)
                self.Plaintext += self.SYMBOLS[((symIndex - self.Shifter) * self.InverseMultiplier) % len(self.SYMBOLS)]
            else:
                self.Plaintext += symbol # just append this symbol unencrypted
        return self.Plaintext

    def setKeys(self,m,s):
        self.Multiplier = m
        self.Shifter = s

    def getKeys(self):
        return  [self.Multiplier,self.Shifter]

    # GCD
#   returns the greatest common denominator. Thats it.
    def gcd(self,a):
        b=95
        while a != 0:
            a, b = b % a, a
        return b
    
    


def main():
    print("in main")
    multi = MultiplicativeCipher()
    cipherText = multi.encrypt("this is a super awesome year '2000' message!!!")
    print(cipherText)
    print(multi.encrypt(cipherText))
    
    print(multi.decrypt(cipherText))
    f = open('.\Output.txt', 'w')
    for i in range(5):
        for j in range(5):
            b=multi.gcd(i)
            if  b== 1:
                multi.setKeys(i,j)
                decoded = multi.decrypt(cipherText)
                print(decoded)
                f.write(decoded+"\n")
    f.close()

    def load_frequency_dictionary(freq_dictionary):
        rootdir = "./books"
        f2= open('.\dictionary_output.txt', 'w')
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                path =  os.path.join(subdir, file)
                print(path)
                f=open(path,'r')
                for line in f.readlines():
                    line = line.split(' ')
                    line[-1] = line[-1].strip('\n')
                    if len(line) == 1 and line[0] == '':
                        continue
                    for word in line:
                        word = word.upper()
                        word = re.sub('[^A-Za-z]+', '', word)
                        if word == '':
                            continue
                        freq_dictionary[word] = freq_dictionary.get(word, 0) + 1
                        #f2.write(word+"\n")
                print(len(freq_dictionary))
                le=len(freq_dictionary)
                
                for l in freq_dictionary:
                    f2.write(l+"\n")
                f.close()
        f2.close()
    
    frequency_dictionary = {}

    load_frequency_dictionary(frequency_dictionary)
    

#if __name__ == '__main__':
main()







# Open the file with read only permit
f2 = open('.\Output.txt')
## Read the first line 
line = f2.readline()

## If the file is not empty keep reading line one at a time
## till the file is empty
while line:
    print(line)
    line = f2.readline()
    
f2.close()



# reading the dictionary and loading it into a set
DictionarRdr = open('.\dictionary.txt', 'r')
DictLstVal = []
DictSetVal = {}
# loading all the values from the text file into list
for line in DictionarRdr:
    line = line.upper()
    line = re.sub(r'[^\w]', '', line)
    DictLstVal.append(line)
# pushing all the values into the sets
DictSetVal = set(DictLstVal)
# closing the file
DictionarRdr.close()
# Reading the data from the file
# Empty dict
FileRdr = open('.\Output.txt', 'r')
fWrite = open('.\OutputNew.txt', 'w')
MaxVal=0
StrVal=""
for line in FileRdr:
    Count = 0
    # reading the data from the file
    for word in line.split():
        # cleaning the data from the text
        word = word.upper()
        word = re.sub(r'[^\w]', '', word)
        fWrite.writelines(word + "\n")
        fWrite.write(str(word in DictLstVal))
        # checking if the value is present in the dictionary
        if(word in DictLstVal):
            Count += 1
        # count represents the score
        fWrite.writelines(str(Count) + "\n")
    # each time re-assigning the string based on the score
    if(MaxVal<Count):
        MaxVal = Count
        StrVal = line
# Closing the files
FileRdr.close()
fWrite.close()
# Printing the best line
print("************************")
print(StrVal)



