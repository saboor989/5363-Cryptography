


print( "Playfair Cipher")
print("Enter \n 1 for encrypt\n 2 for decrypt:")
x = input()


alpha= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key=input("please enter the secret key for decoding: ")
key1=''
l=len(key)

key=key.upper()
b=0
while (b<len(key)):
    if(ord(key[b])>=65 and ord(key[b])<=90):
        #print("no spaces"+key[b])
    b=b+1


i=0
#removing spaces:
while(i<l):
    if(ord(key[i])!=32):
        key1=key1+key[i]
       # print("hello")
    i=i+1
print(key1)

#removing duplicates:

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
print("the unique is ")
print(uniq)





#inserting into matrix
Matrix = [[0 for x in range(5)] for x in range(5)] 
#You can now add items to the list:

lenn=len(uniq)

x=0
i=0
j=0
while(x<lenn):
    Matrix[i][j]=uniq[x]
    print("the matrix have")
    print(i)
    print(j)
    print(Matrix[i][j])
    x=x+1
    j=j+1
    if(j==5):
        i=i+1
        j=0
print("the i value \n i")
print(i)
print("j value")
print(j)
ik=i
ij=j
    

y=0
print("the lenn")
print(lenn)
uniq=uniq.upper()
while(y<26):
    c=0
    z=0
    
    while(z<lenn):
        #print("the ord of alpha and uniq ")
        #print(ord(alpha[y]))
        #print(alpha[y])
        #print(ord(uniq[z]))
        #print(uniq[z])
        if(ord(alpha[y])==ord(uniq[z])):
            c=1
            #print("the c value is ::::::::")
            #print(c)
            #print("the above is c value")
        z=z+1
    #print("the z value")
    #print(z)
    if(c==1):
        m=1
    else:
        if(ord(alpha[y])!=74):
            Matrix[i][j]=alpha[y]
            #print("the matrix")
            #print(i)
            #print(j)
            print(Matrix[i][j])
            j=j+1
            if(j==5):
                i=i+1
                j=0
                print("\n")
    y=y+1
    

#print( Matrix[0][0]) # prints 1
#print( Matrix[4][0]) # prints 5


#secretkey=input("please enter the secret key for decoding")

encryptmsg=input("please enter the encryt message to decode")

print("the encryptmsg:"+encryptmsg)

encryptmsg=encryptmsg.upper()

b=0
while (b<len(encryptmsg)):
    #print("\n")
    if(ord(encryptmsg[b])>=65 and ord(encryptmsg[b])<=90):
        #print("no spaces"+encryptmsg[b])
    b=b+1



#####print("the i value :")
#####print(i)
#####print("the j value :")
#####print(j)

# searching for the message charaters in matrix
# and storing values in the variable

sti=0
stj=0
sti1=0
stj1=0
m=0
while(m<len(encryptmsg)):
    ii=0
    js=0
    c=0
    while(ii<5):
        while(js<5):
            if(ord(Matrix[ii][js])==ord(encryptmsg[m])):
                #print("the row and column number matched")
                #print(Matrix[ii][js])
                #print(encryptmsg[m])
                #print(ii)
                #print(js)
                c=1
            js=js+1
        ii=ii+1
    
    m=m+1
    
def position(letter):
	x=y=0
	for i in range(5):
		for j in range(5):
			if (Matrix[i][j]==letter):
				x=i
				y=j

	return x,y

e=0
dmsg=''
#while(e<len(encryptmsg)):
while(e<len(encryptmsg)):
    #print("searching the position")
    p1,q1=position(encryptmsg[e])
    #print(p1)
    #print(q1)
    #print("2nd char:")
    e=e+1
    if(e<len(encryptmsg)):
        
        p2,q2=position(encryptmsg[e])
        #print(p2)
        #print(q2)
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
    print("the e")
    print(e)
    print("the dmsg is:")
    print(dmsg)
    e=e+1




#decrypting the encrypted message

print("the length of dmsg is :")
print(len(dmsg))
g=0
emsg=''
while(g<len(dmsg)):
    #print("searching the position")
    p1,q1=position(dmsg[g])
    #print(p1)
    #print(q1)
    #print("2nd char:")
    g=g+1
    if(g<len(dmsg)):
        
        p2,q2=position(dmsg[g])
        #print(p2)
        #print(q2)
    if(q1==q2):
        if(p1==4):
            emsg=emsg+Matrix[4][q1]
        else:
            emsg=emsg+Matrix[p1-1][q1]
        if(p2==4):
            emsg=emsg+Matrix[4][q2]
        else:
            emsg=emsg+Matrix[p2-1][q2]
    elif(p1==p2):
        if(q1==4):
            emsg=emsg+Matrix[p1][4]
        else:
            emsg=emsg+Matrix[p1][q1-1]
        if(q2==4):
            emsg=emsg+Matrix[q2][4]
        else:
            emsg=emsg+Matrix[p2][q2-1]
    else:
        emsg=emsg+Matrix[p1][q2]
        emsg=emsg+Matrix[p2][q1]
    print("the g")
    print(g)
    print("the decrypted message is is:")
    print(emsg)
    g=g+1

emsg=''





#print("the i is :")
#print(Matrix[0][0])

#flag =1
#if (x == '1'):
#print("hello")
#elif(x=='2'):
#print("hi")
#else:
#print("error")


#fruits = ['banana', 'apple',  'mango']
#for index in range(len(fruits)):
    #print ('Current fruit :', fruits[index])

#print ("Good bye!")
