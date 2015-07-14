#key modification
import sys
def alphabet():
    #alpha= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Entering the alphabets in string.
    alpha= ""
    #Generate the alphabet
    for i in range(0,26):
        alpha = alpha + chr(i+65)
    return alpha

def Remove_dup_specialchar(key):
    #Removing numbers or special characters from key
    key1=''
    key=key.upper()
    b=0
    while (b<len(key)):
        if(ord(key[b])>=65 and ord(key[b])<=90):
            key1=key1+key[b]
        b=b+1
    
    jreplace=key1
    key1=''
    v=0
    while(v<len(jreplace)):
        if(jreplace[v]=='J'):
            key1=key1+'I'
        else:
            key1=key1+jreplace[v]
        v=v+1
    #now key is in key1
    #removing duplicates from the key:
    le=len(key1)    
    uniq=''
    j=0
    c=0
    m=0
    while(j<le):
        c=0
        #print("the j value")
        if(j==0):
            uniq=uniq+key1[0]
        k=0
        leng=len(uniq)
        while(k<leng):
            if(ord(key1[j])==ord(uniq[k])):
                c=1
            k=k+1
        if(c==1):
            m=1
        else:
            uniq=uniq+key1[j]
        j=j+1
    return uniq

def Generate_Matrix(uniq,alpha):
    #the unique key is in uniq variable
    #Inserting the unique key into matrix
    Matrix = [[0 for x in range(5)] for x in range(5)] 
    lenn=len(uniq)
    x=0
    i=0
    j=0
    while(x<lenn):
        Matrix[i][j]=uniq[x]
        #print("the matrix have")
        x=x+1
        j=j+1
        if(j==5):
            i=i+1
            j=0
    ik=i
    ij=j
    y=0
    uniq=uniq.upper()
    while(y<26):
        c=0
        z=0
    
        while(z<lenn):
            #print("the uniq[z]=",uniq[z],z,alpha[y])
            if(ord(alpha[y])==ord(uniq[z])):
                c=1
            z=z+1
        if(c==1):
            m=1
        else:
            if(ord(alpha[y])!=74):
                Matrix[i][j]=alpha[y]
                #print(i,j,"matrix :",Matrix[i][j])
                #print(Matrix[i][j])
                j=j+1
                if(j==5):
                    i=i+1
                    j=0
        y=y+1
    #printing the matrix
    ###
    #print("The matrix is :\n")
    for line in Matrix:
        #print(line) 
        m=0
    return Matrix
    #####
def Clean_message(encryptmsg):
    #removing numbers or special character from the message 
    msg=encryptmsg
    msg=msg.upper()
    message=''
    b=0
    while (b<len(msg)):
        if(ord(msg[b])>=65 and ord(msg[b])<=90):
            message=message+msg[b]
        b=b+1
    print("The message is :",message)
    return message


def Encrypt():
    key=input("please enter the secret key : ")
    encryptmsg=input("please enter the message to encrypt :")

    #generating alphabets    
    alpha=alphabet()
    
    #cleaning the key
    uniq= Remove_dup_specialchar(key)
    #print("The unique key is :",uniq)

    #generating matix
    Matrix=Generate_Matrix(uniq,alpha)

    #cleanning the message
    message=Clean_message(encryptmsg)
    

    

    #inserting x if their is a double characters in message
    #print("the message is :",message)
    msg=message
    le=len(message)
    xmsg=''
    j=0
    i=0
    c=0
    m=0
    while(i<le):
        c=0
        if(i==0):
            xmsg=xmsg+msg[0]
            i=i+1
        if(i<len(msg)):
            if(ord(xmsg[j])==ord(msg[i])):
                xmsg=xmsg+'X'
                xmsg=xmsg+msg[i]
                j=j+2
            else:
                xmsg=xmsg+msg[i]
                j=j+1
        else:
            m=0
        i=i+1
    #print("\nThe x inserted message is : ",xmsg)
    #the x inserted message is in variable xmsg
    
    l=len(xmsg)
    if(l%2==1):
        xmsg=xmsg+'X'
        
    #print("the x inserted at end msg :",xmsg)


    encryptmsg=xmsg
    #print("The encryptedmsg",encryptmsg)
    #encrypting the message    
    e=0
    dmsg=''
    while(e<len(encryptmsg)):
        p1,q1=position(encryptmsg[e],Matrix)
        e=e+1
        if(e<len(encryptmsg)):
            p2,q2=position(encryptmsg[e],Matrix)
        if(q1==q2):
            if(p1==4):
                dmsg=dmsg+Matrix[0][q1]
            else:
                dmsg=dmsg+Matrix[p1+1][q1]
            if(p2==4):
                dmsg=dmsg+Matrix[0][q2]
            else:
                dmsg=dmsg+Matrix[p2+1][q2]
        elif(p1==p2):
            if(q1==4):
                dmsg=dmsg+Matrix[p1][0]
            else:
                dmsg=dmsg+Matrix[p1][q1+1]
            if(q2==4):
                dmsg=dmsg+Matrix[q2][0]
            else:
                dmsg=dmsg+Matrix[p2][q2+1]
        else:
            dmsg=dmsg+Matrix[p1][q2]
            dmsg=dmsg+Matrix[p2][q1]
        #print("the e")
        #print(e)
        
        e=e+1
    print("\nThe encrypted message is :",dmsg)


#function to find the position of letters in matrix
def position(letter,Matrix):
	x=y=0
	if(letter=='J'):
	    letter='I'
	for i in range(5):
		for j in range(5):
			if (Matrix[i][j]==letter):
				x=i
				y=j

	return x,y
	
	
def Decrypt():
    #Re
    key=input("please enter the secret key : ")
    decryptmsg=input("please enter the Encrypted message :")

    #generating alphabets    
    alpha=alphabet()
    
    #cleaning the key
    uniq= Remove_dup_specialchar(key)
    #print("The unique key is :",uniq)

    #generating matix
    Matrix=Generate_Matrix(uniq,alpha)
    
    #cleanning the message
    dmsg=Clean_message(decryptmsg)
    

    
    #decrypting the encrypted message
    g=0
    emsg=''
    while(g<len(dmsg)):
        p1,q1=position(dmsg[g],Matrix)
        g=g+1
        if(g<len(dmsg)):
            p2,q2=position(dmsg[g],Matrix)
        if(q1==q2):
            if(p1==0):
                emsg=emsg+Matrix[4][q1]
            else:
                emsg=emsg+Matrix[p1-1][q1]
            if(p2==0):
                emsg=emsg+Matrix[4][q2]
            else:
                emsg=emsg+Matrix[p2-1][q2]
        elif(p1==p2):
            if(q1==0):
                emsg=emsg+Matrix[p1][4]
            else:
                emsg=emsg+Matrix[p1][q1-1]
            if(q2==0):
                emsg=emsg+Matrix[q2][4]
            else:
                emsg=emsg+Matrix[p2][q2-1]
        else:
            emsg=emsg+Matrix[p1][q2]
            emsg=emsg+Matrix[p2][q1]
        g=g+1
    print("The decoded message is :",emsg)    

	
#requesting user for input
print( "Welcome to Playfair Cipher ->")
print("Enter: \n1.Encrypt\n2.Decrypt \n3.Quit")
x = input()
while(x=='1' or x=='2' or x=='3'):
    if(x=='1'):
        Encrypt()
    elif(x=='2'):
        Decrypt()
    else:
        sys.exit()
    x=input("\nEnter: \n1.Encrypt\n2.Decrypt \n3.Quit :\n")
