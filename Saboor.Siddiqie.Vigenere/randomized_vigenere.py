

#SYMBOLS = """" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~""""


#def keywordFromSeed(seed)
#Does what I showed above.
#def encrypt(plain_text_message,keyword)
#Describes itself
#def decrypt(cipher_text_message,keyword)
#Describes itself
#def buildVigenere()



import random

#symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""



#############################################################################
# keywordFromSeed -
#    Works by peeling off two digits at a time, and using modulo to map it into
#    the proper range of A-Z for use as a keyword.
# Example:
#    This example spells math, and I chose values 0-25 on purpose, but
#    it really doesn't matter what values we choose because 99 % 26 = 21 or 'V' 
#    or any value % 26 for that matter.
#
#    seed = 12001907
#    l1   = 12001907 % 100 = 07 = H
#    seed = 12001907 // 100 = 120019
#    l2   = 120019 % 100 = 19 = T
#    seed = 120019 // 100 = 1200
#    l3   = 1200 % 100 = 0 = A
#    seed = 1200 // 100 = 12
#    l4   = 12 % 100 = 12 = M
#    seed = 12 // 100 = 0
#
# @param {int} seed - An integer value used to seed the random number generator
#                     that we will use as our keyword for vigenere
# @return {string} keyword - a string representation of the integer seed
#############################################################################
def keywordFromSeed(seed):
    Letters = []
    #print("the seed:",seed)
    seed=int(seed)
    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
        #seed=str(seed)
    return ''.join(Letters)

#Usage:

#seed = 12001907

#random.seed(12001907)

#keyWord1 = keywordFromSeed(seed)

#print(keyWord1)   # Prints "MATH"




def buildVigenere(symbols):

    n = len(symbols)

    vigenere = [[0 for i in range(n)] for i in range(n)]

    #Build the vigenere matrix
    for i in range(n):
        temp = symbols
        for j in range(n):
            #r = random.randrange(len(temp))
            #vigenere[i][j] = temp[r]
            #temp.replace(temp[r],'')
            nothing=0
    uniqkey=[]
    i=0
    while(i<n):
        j=0
        k=0
        l=0
        uniq=[]
        while j<n:
            r=random.randrange(len(temp))
            #print("The r value generated is :",r)
            if(j==0):
                if(i==0):
                    uniq.append(r)
                    uniqkey.append(r)
                    vigenere[i][j] = temp[r]
                    temp.replace(temp[r],'')
                    j+=1
                    #print("the uniq 0 is :",uniq[0])
                else:
                    if(r in uniqkey):
                        nothing=0
                    else:
                        uniq.append(r)
                        uniqkey.append(r)
                        vigenere[i][j] = temp[r]
                        temp.replace(temp[r],'')
                        j+=1
                        #print("the uniq 0 is :",uniq[0])
            else:
                if(r in uniq):
                    nothing=1
                    #print("the r value in uniq is :::",r)
                else:                
                    #uniq[l]=r
                    uniq.append(r)
                    vigenere[i][j] = temp[r]
                    temp.replace(temp[r],'')
                    #print("The uniq l+1 is :",uniq[l])
                    l+=1
                    j+=1
            #print("The length of uniq is :",len(uniq),uniq)
        #print(uniq)
        #print("the vigenere is :",vigenere[i])
        i+=1
    return vigenere




    
    
    

# encrypt
# param v : vigenere table
# param k : key
# param m : message
# param ki: key index
# param mi: message index
def encryptionMessage(vigenere,keyword,message,ki,mi):
    #row = ord(message[mi]) - 65
    #col = ord(keyword[ki]) - 65
    #row=(ord(message[mi])-65)
    #col=(ord(keyword[ki])-65)
    #print(row,col)
    #print(vigenere[0][0])
    messagesearch=0;
    keysearchs=0
    #print("the symbols",len(symbols))
    for s in range(len(symbols)):
        if(message[mi]==vigenere[0][s]):
            messagesearch=s
    for k in range(len(symbols)):
        if(keyword[ki]==vigenere[k][0]):
            keysearch=k
    #print("the keysearch and messagesearch:",keysearch,messagesearch)
    return vigenere[keysearch][messagesearch]            
    #return vigenere[row][col]
    


# decrypt
# param v : vigenere table
# param k : key
# param m : decrypt message
# param ki: key index
# param mi: message index
def decryptionMessage(vigenere,keyword,message,ki,mi):
    #row = ord(message[mi]) - 65
    #col = ord(keyword[ki]) - 65
    #row=(ord(message[mi])-65)
    #col=(ord(keyword[ki])-65)
    #print(row,col)
    #print(vigenere[0][0])
    decryptmessagesearch=0;
    keysearch=0
    print("the n is :",len(symbols))
    for k in range(len(symbols)):
        if(keyword[ki]==vigenere[k][0]):
            keysearch=k
    for s in range(len(symbols)):
        if(message[mi]==vigenere[keysearch][s]):
            messagesearch=s
    print("the decrypt :",vigenere[0][messagesearch])
    return vigenere[0][messagesearch]            
    #return vigenere[row][col]

    
    
    
    
    
    
#for line in vigenere:
    #print(line)
#print(vigenere)
###
#SYMBOLS = """" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
#symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#vigenere = buildVigenere(symbols)
#print(vigenere)


def encrypt(Message,mode,seed):
    random.seed(seed)
    keyword=keywordFromSeed(seed)
    #print("The keyword is :",keyword)
    vigenere=buildVigenere(symbols)
    #for line in vigenere:
        #print(line)
        
     
    for line in vigenere:
        print(line)     
    
    #print("The table 0th position :",vigenere[0][0])   
    # we have 
    #keyword
    #message
    #vigenere tableau
    
    if(mode=='encrypt'):        
        cipherText = ""
        
        # encrypt
        # param v : vigenere table
        # param k : key
        # param m : message
        # param ki: key index
        # param mi: message index
        #Message=Message.upper()
        for i in range(len(Message)):
            mi = i
            ki = i % len(keyword)
            #print(Message[i])
            if ord(Message[i]) == 32:
                cipherText = cipherText + ' '
            else:
                #print("the keyword: ,message : and ki and mi are ",keyword,Message,ki,mi)
                cipherText = cipherText + encryptionMessage(vigenere,keyword,Message,ki,mi)
        print(cipherText)    
    return(cipherText)

def decrypt(Message,mode,seed):
    print("the message in decrypt:",Message)
    random.seed(seed)
    keyword=keywordFromSeed(seed)
    #print("The keyword is :",keyword)
    vigenere=buildVigenere(symbols)
    #for line in vigenere:
        #print(line)
        
     
    for line in vigenere:
        print(line)
        
    #print("The table 0th position :",vigenere[0][0])   
    # we have 
    #keyword
    #message
    #vigenere tableau
    
    plainText = ""
        
    # decrypt
    # param v : vigenere table
    # param k : key
    # param m : decryptmessage
    # param ki: key index
    # param mi: message index
    #Message=Message.upper()
    print("the message in decrypt:",Message)
    for i in range(len(Message)):
        mi = i
        ki = i % len(keyword)
        #print(Message[i])
        if ord(Message[i]) == 32:
            plainText = plainText + ' '
        else:
            print("the keyword: ,message : and ki and mi are ",keyword,Message,ki,mi)
            plainText = plainText + decryptionMessage(vigenere,keyword,Message,ki,mi)
    print(plainText)
    return(plainText)
    
    #encryptionMessage(vigenere,keyword,message,ki,mi):
