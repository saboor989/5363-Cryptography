###############################################
# Name: SABOOR AHMED SIDDIQIE
# Class: CMPS 5363 Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
###############################################
import pprint
import re
import sys

class StringManip:
    """
    Helper class to speed up simple string manipulation
    """

    def generateAlphabet(self):
        #Create empty alphabet string
        alphabet = ""

        #Generate the alphabet
        for i in range(0,26):
            alphabet = alphabet + chr(i+65)

        return alphabet


    def cleanString(self,s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'_','spLetters':'X'}):
        """
        Cleans message by doing the following:
        - up            - uppercase letters
        - spLetters     - split double letters with some char
        - reSpaces      - replace spaces with some char or '' for removing spaces
        - reNonAlphaNum - remove non alpha numeric
        - reDupes       - remove duplicate letters
        @param   string -- the message
        @returns string -- cleaned message
        """
        if 'up' in options:
            s = s.upper()

        if 'spLetters' in options:
            #replace 2 occurences of same letter with letter and 'X'
            s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)

        if 'reSpaces' in options:
            space = options['reSpaces']
            #i replaced space with ""
            s = re.sub(r'[\s]',"", s)

        if 'reNonAlphaNum' in options:
            s = re.sub(r'[^\w]', '', s)

        if 'reDupes' in options:
            s= ''.join(sorted(set(s), key=s.index))
        return s

class PlayFair:
    """
    Class to encrypt via the PlayFair cipher method
    Methods:
    - generateSquare
    - transposeSquare
    -
    """

    def __init__(self,key,message):
        self.Key = key
        self.Message = message
        self.Square = []
        self.Transposed = []
        self.StrMan = StringManip()
        self.Alphabet = ""
       

        self.generateSquare()
        self.transposeSquare()

        self.Message = self.StrMan.cleanString(self.Message,{'up':1,'reSpaces':'_','reNonAlphaNum':1,'spLetters':1})
        lengthMessage=len(self.Message)
        #print("the length of message is :",lengthMessage)
        if(lengthMessage%2 == 1):
            #print("the lengthMessage inside:")
            self.Message=self.Message+'X'
        #print("the 'x' added message is :",self.Message)

    def generateSquare(self):
        """
        Generates a play fair square with a given keyword.
        @param   string   -- the keyword
        @returns nxn list -- 5x5 matrix
        """
        row = 0     #row index for sqaure
        col = 0     #col index for square

        #Create empty 5x5 matrix
        self.Square = [[0 for i in range(5)] for i in range(5)]

        self.Alphabet = self.StrMan.generateAlphabet()

        #uppercase key (it meay be read from stdin, so we need to be sure)
        self.Key = self.StrMan.cleanString(self.Key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})

        #Load keyword into square
        for i in range(len(self.Key)):
            self.Square[row][col] = self.Key[i]
            self.Alphabet = self.Alphabet.replace(self.Key[i], "")
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

        #Remove "J" from alphabet
        self.Alphabet = self.Alphabet.replace("J", "")

        #Load up remainder of playFair matrix with
        #remaining letters
        for i in range(len(self.Alphabet)):
            self.Square[row][col] = self.Alphabet[i]
            col = col + 1
            if col >= 5:
                col = 0
                row = row + 1

    def transposeSquare(self):
        """
        Turns columns into rows of a cipher square
        @param   list2D -- playFair square
        @returns list2D -- square thats transposed
        """
        #Create empty 5x5 matrix
        self.Transposed = [[0 for i in range(5)] for i in range(5)]

        for col in range(5):
            for row in range(5):
               self.Transposed[col][row] = self.Square[row][col]


    def getCodedDigraph(self,messageReturn):
        """
        Turns a given digraph into its encoded digraph whether its on
        the same row, col, or a square
        @param   list -- digraph
        @returns list -- encoded digraph
        """
        #print("the message is in coded :",messageReturn)
        Enc=''
        newDigraph = ['','']
        i=0
        j=0
        while(i<len(messageReturn)):
            #Check to see if digraph is in same row
            j=i+1
            if(i<len(messageReturn) and j<len(messageReturn)):
                findinglocation1 = self.getLocation(messageReturn[i])
                findinglocation2 = self.getLocation(messageReturn[j])
                #print("the locations1[0]:",findinglocation1[0])
                #print("the locations1[1]:",findinglocation1[1],messageReturn[i])
                #print("the locations2[0]:",findinglocation2[0])
                #print("the locations2[1]:",findinglocation2[1],messageReturn[j])
                if(findinglocation1[0]==findinglocation2[0]):
                    for row in self.Square:
                        if messageReturn[i] in row and messageReturn[j] in row:
                            newDigraph[0] = row[((row.index(messageReturn[i])+1)%5)]
                            newDigraph[1] = row[((row.index(messageReturn[j])+1)%5)]
                            Enc=Enc+newDigraph[0]
                            Enc=Enc+newDigraph[1]
                            #return newDigraph
                
                elif(findinglocation1[1]==findinglocation2[1]):    
                    #Check to see if digraph is in same column
                    for row in self.Transposed:
                        if messageReturn[i] in row and messageReturn[j] in row:
                            newDigraph[0] = row[((row.index(messageReturn[i])+1)%5)]
                            newDigraph[1] = row[((row.index(messageReturn[j])+1)%5)]
                            Enc=Enc+newDigraph[0]
                            Enc=Enc+newDigraph[1]
                            #return newDigraph
        
                else:
                    #Digraph is in neither row nor column, so it's a square
                    location1 = self.getLocation(messageReturn[i])
                    location2 = self.getLocation(messageReturn[j])
            
                    #print(location1)
                    #print(location2)
            
                    #print(self.Square[location1[0]][location2[1]])
                    #print(self.Square[location2[0]][location1[1]])
                    Enc=Enc+self.Square[location1[0]][location2[1]]
                    Enc=Enc+self.Square[location2[0]][location1[1]]
                    #return [self.Square[location1[0]][location2[1]],self.Square[location2[0]][location1[1]]]
            i=i+2
        ###################################
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: SABOOR AHMED SIDDIQIE")
        print("*********************************************************")
        print("Your encrypt message is\n=>",Enc)
        print("*********************************************************")
    def getDecodedDigraph(self,messageReturn):
        """
        Turns a given digraph into its encoded digraph whether its on
        the same row, col, or a square
        @param   list -- digraph
        @returns list -- encoded digraph
        """
        #print("the message is in coded :",messageReturn)
        deEnc=''
        newDigraph = ['','']
        i=0
        j=0
        while(i<len(messageReturn)):
            #Check to see if digraph is in same row
            j=i+1
            if(i<len(messageReturn) and j<len(messageReturn)):
                findinglocation1 = self.getLocation(messageReturn[i])
                findinglocation2 = self.getLocation(messageReturn[j])
                #print("the locations1[0]:",findinglocation1[0])
                #print("the locations1[1]:",findinglocation1[1],messageReturn[i])
                #print("the locations2[0]:",findinglocation2[0])
                #print("the locations2[1]:",findinglocation2[1],messageReturn[j])
                if(findinglocation1[0]==findinglocation2[0]):
                    for row in self.Square:
                        if messageReturn[i] in row and messageReturn[j] in row:
                            newDigraph[0] = row[((row.index(messageReturn[i])-1)%5)]
                            newDigraph[1] = row[((row.index(messageReturn[j])-1)%5)]
                            deEnc=deEnc+newDigraph[0]
                            deEnc=deEnc+newDigraph[1]
                            #return newDigraph
                
                elif(findinglocation1[1]==findinglocation2[1]):    
                    #Check to see if digraph is in same column
                    for row in self.Transposed:
                        if messageReturn[i] in row and messageReturn[j] in row:
                            newDigraph[0] = row[((row.index(messageReturn[i])-1)%5)]
                            newDigraph[1] = row[((row.index(messageReturn[j])-1)%5)]
                            deEnc=deEnc+newDigraph[0]
                            deEnc=deEnc+newDigraph[1]
                            #return newDigraph
        
                else:
                    #Digraph is in neither row nor column, so it's a square
                    location1 = self.getLocation(messageReturn[i])
                    location2 = self.getLocation(messageReturn[j])
                    #print(location1)
                    #print(location2)
            
                    #print(self.Square[location1[0]][location2[1]])
                    #print(self.Square[location2[0]][location1[1]])
                    deEnc=deEnc+self.Square[location1[0]][location2[1]]
                    deEnc=deEnc+self.Square[location2[0]][location1[1]]
                    #return [self.Square[location1[0]][location2[1]],self.Square[location2[0]][location1[1]]]
            i=i+2
        ##################################
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: SABOOR AHMED SIDDIQIE")
        print("*********************************************************")
        print("Your decrypted message is\n=>",deEnc)
        print("*********************************************************")
    
    def getLocation(self,letter):
        row = 0
        col = 0

        count = 0
        for list in self.Square:
            if letter in list:
                row = count
            count += 1

        count = 0
        for list in self.Transposed:
            if letter in list:
                col = count
            count += 1
        return [row,col]

    #############################################
    # Helper methods just to see whats going on
    #############################################
    def printNewKey(self):
        #print(self.Key)
        return(key)

    def printNewMessage(self):
        #print(self.Message)
        return(self.Message)

    def printSquare(self):
        for list in self.Square:
            print(list)
        print('')

    def printTransposedSquare(self):
        for list in self.Transposed:
            print(list)
        print('')


print("Playfair Encryption Tool (P.E.T)")
print("Written By: SABOOR AHMED SIDDIQIE")
print("*********************************************************")
print(" 1.Encrypt\n 2.Decrypt\n 3.Quit")
print("=>")
choice=input()
print("*********************************************************")

while(choice=='1' or choice=='2' or choice=='3'):
    if(choice=='1'):
        #if __name__ == "__main__":
        #message = "The fox has foot problems and has been hoodwinked. Can you beleive it?"
        #key = 'Mathematics is Awesome foxy lady!!'
        
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: SABOOR AHMED SIDDIQIE")
        print("*********************************************************")
        print("Please enter a keyword:\n=>")
        key=input()
        
        ## removing j from the key replacing it with i 
        jkey=key
        key=''
        size=0
        while(size<len(jkey)):
            if(jkey[size]=='J' or jkey[size]=='j'):
                key=key+'I'
            else:
                key=key+jkey[size]
            size=size+1
        #print("the key without j is :",key)
        
        print("*********************************************************")
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: SABOOR AHMED SIDDIQIE")
        print("*********************************************************")
        print("Please enter a message\n=>")
        message=input()
        # removing j from the message replacing it with i 
        jmessage=message
        message=''
        size=0
        while(size<len(jmessage)):
            if(jmessage[size]=='J' or jmessage[size]=='j'):
                message=message+'I'
            else:
                message=message+jmessage[size]
            size=size+1
        #print("the key without j is :",message)
        print("*********************************************************")
        #print("the length is : the key length is :",len(message),len(key))
        if(len(message)==0 or len(key)==0):
            print("Message cannot be Null, select the proper method and enter the proper message")
            print("*********************************************************")
            choice=1
        else:
            myCipher = PlayFair(key,message)
            #print("the  new key is :")
            myCipher.printNewKey()
            #print("the new message is :")
            messageReturn=myCipher.printNewMessage()
            #print("the message Return:",len(messageReturn))
            #myCipher.printSquare()
            #myCipher.printTransposedSquare()
            #print(myCipher.getCodedDigraph(['I','T']))
            myCipher.getCodedDigraph(messageReturn)
    elif(choice=='2'):
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: SABOOR AHMED SIDDIQIE")
        print("*********************************************************")
        print("Please enter a keyword:\n=>")
        decryptkey=input()
        jkey=decryptkey
        decryptkey=''
        size=0
        while(size<len(jkey)):
            if(jkey[size]=='J' or jkey[size]=='j'):
                decryptkey=decryptkey+'I'
            else:
                decryptkey=decryptkey+jkey[size]
            size=size+1
        #print("the key without j is :",key)
        
        print("*********************************************************")
        print("Playfair Encryption Tool (P.E.T)")
        print("Written By: SABOOR AHMED SIDDIQIE")
        print("*********************************************************")
        print("Enter the encrypted message:\n=>")
        decryptmessage=input()
        
        # removing j from the message replacing it with i 
        jmessage=decryptmessage
        decryptmessage=''
        size=0
        while(size<len(jmessage)):
            if(jmessage[size]=='J' or jmessage[size]=='j'):
                decryptmessage=decryptmessage+'I'
            else:
                decryptmessage=decryptmessage+jmessage[size]
            size=size+1
            
        print("*********************************************************")
        if(len(decryptmessage)==0 or len(decryptkey)==0):
            print("Message cannot be Null,Please enter the proper message")
            print("*********************************************************")
            choice=2
        else:
            dmyCipher=PlayFair(decryptkey,decryptmessage)
            dmyCipher.printNewKey()
            demessageReturn=dmyCipher.printNewMessage()
            dmyCipher.getDecodedDigraph(demessageReturn)
    else:
        sys.exit()
    print("Playfair Encryption Tool (P.E.T)")
    print("Written By: SABOOR AHMED SIDDIQIE")
    print("*********************************************************")
    print(" 1.Encrypt\n 2.Decrypt\n 3.Quit\n=>")    
    choice=input()
    