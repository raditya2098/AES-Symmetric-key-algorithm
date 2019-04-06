

mix_col=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
mix_coli=[[14,11,13,9],[9,14,11,13],[13,9,14,11],[11,13,9,14]]
Rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a]
Sbox_inv = [
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
 ]

Sbox = [
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
            ]

def check_256(a):
    if a>255:
        a-=256
        ans=a^27
    else:
        ans=a
    return (ans)

def mat_mul(y,x):
    tmp2=int(str(x),16)
    tmp1=(int(str(x),16))*2
    tmp=check_256(tmp1)
    if tmp==256:
        tmp=27
    z1=z2=z3=z4=0
    if y==9:
        if tmp2==64:
            z=(54)^64
        else:
            z1=tmp*2
            z2=check_256(z1)
            z3=z2*2
            z4=check_256(z3)
            z=z4^tmp2
            
    elif y==11:
        if tmp2==64:
            z=(check_256((27^64)*2))^64
        else:
            z1=tmp*2
            z2=check_256(z1)
            z3=z2^tmp2
            z4=z3*2
            z1=check_256(z4)
            z=z1^tmp2
            
    elif y==13:
        if tmp2==137:
            z=54^137
        else:
            z1=tmp^tmp2
            z2=z1*2
            z3=check_256(z2)
            z4=z3*2
            z1=check_256(z4)
            z=z1^tmp2
            
    else:
        if tmp2==137:
            z1=27^137
            z2=z1*2
            z=check_256(z2)
        else:
            z1=tmp^tmp2
            z2=z1*2
            z3=check_256(z2)
            z4=z3^tmp2
            z1=z4*2
            z=check_256(z1)
            
        
    z1=z
    z=check_256(z1)
    return (z)


def shift_right3(l):
    l2=[]
    for i in range(1,len(l)):
        l2.append(l[i])
    l2.append(l[0])
    return(l2)

def shift_right(l,n):
    l2=[]
    x=0
    for i in range((len(l)-n),len(l)):
        l2.append(l[i])
    for i in range(0,(len(l)-n)):
        l2.append(l[i])
    
    return (l2)

def check_256(a):
    if a>256:
        a-=256
        ans=a^27
    else:
        ans=a
    return (ans)
        
def check_x(str_1):
    lst=[]
    for i in range(2,len(str_1)):
        lst.append(str_1[i])
    lst=''.join(map(str,lst))
    return(lst)

def AESdecryption():
    key=input("Enter The Key:\t")
    key_val=[]
    for i in range(len(key)):
        key_val.append(hex(ord(key[i])))
    add_k=[]
    new_l_k=[]
    for ch in key_val:
        x=check_x(ch)
        new_l_k.append(x)

    list_1=[]
    list_2=[]
    list_3=[]
    list_0=[]

    for i in range(len(new_l_k)):
        if i<4:
            list_0.append(new_l_k[i])
        elif i>3 and i <8:
            list_1.append(new_l_k[i])
        elif i>7 and i <12:
            list_2.append(new_l_k[i])
        elif i>11 and i <16:
            list_3.append(new_l_k[i])

    list_x=[]
    for i in range(len(list_0)):
        list_x.append(list_0[i])
    for i in range(len(list_1)):
        list_x.append(list_1[i])
    for i in range(len(list_2)):
        list_x.append(list_2[i])
    for i in range(len(list_3)):
        list_x.append(list_3[i])
    add_k.append(list_x)

    i_key=1

    while(i_key!=11):
        prelim1=[]
        prelim1=shift_right3(list_3)
        prelim2=[]
        for ch in prelim1:
            prelim2.append(check_x(hex(Sbox[int(ch,16)])))
        prelim3=[]
        tmp=(int(str(prelim2[0]),16)^Rcon[i_key])
        prelim3.append(check_x(hex(tmp)))
        for i in range(1,len(prelim2)):
            prelim3.append(prelim2[i])

        list_4=[]
        list_5=[]
        list_6=[]
        list_7=[]
        for i in range(len(prelim3)):
            list_4.append(check_x(hex(int(str(list_0[i]),16)^int(str(prelim3[i]),16))))
        for i in range(len(list_4)):
            list_5.append(check_x(hex(int(str(list_4[i]),16)^int(str(list_1[i]),16))))
        for i in range(len(list_5)):
            list_6.append(check_x(hex(int(str(list_5[i]),16)^int(str(list_2[i]),16))))
        for i in range(len(list_6)):
            list_7.append(check_x(hex(int(str(list_6[i]),16)^int(str(list_3[i]),16))))

        list_1=[]
        list_2=[]
        list_3=[]
        list_0=[]

        for ch in list_4:
            list_0.append(ch)
        for ch in list_5:
            list_1.append(ch)
        for ch in list_6:
            list_2.append(ch)
        for ch in list_7:
            list_3.append(ch)

        list_x=[]
        for i in range(len(list_0)):
            list_x.append(list_0[i])
        for i in range(len(list_1)):
            list_x.append(list_1[i])
        for i in range(len(list_2)):
            list_x.append(list_2[i])
        for i in range(len(list_3)):
            list_x.append(list_3[i])

        add_k.append(list_x)
        i_key+=1
        
    file=open('aes_values.txt','r')
    cipher_textk=file.readline()
    count=0
    add_k1=[]
    while(count!=11):
        i=0
        tmp=file.readline()
        add_k1.append(tmp.split())
        count+=1
    cipher_text=cipher_textk.split()
    append_length=file.readline()
    file.close()
    flag=0
    if flag!=1:
        for i in range(len(add_k)):
            for j in range(len(add_k[i])):
                if add_k[i][j]==add_k1[i][j]:
                    flag=0
                else:
                    flag=1
                    break
            if flag==1:
                break


    add_k.reverse()

    if flag==1:
        print("Invalid key, can't decipher the message")

    else:
        new_l=[]
        x=0
        for i in range(0,1):
            for j in range(len(add_k[i])):
                z=hex(int(add_k[i][j],16)^int(cipher_text[j],16))
                new_l.append(check_x(z))
                x+=1
        mat1=[]
        mat2=[]
        mat3=[]
        mat0=[]

        for i in range(len(new_l)):
            if i==0 or i==4 or i==8 or i==12:
                mat0.append(new_l[i])
            elif i==1 or i==5 or i==9 or i==13:
                    mat1.append(new_l[i])
            elif i==2 or i==6 or i==10 or i==14:
                mat2.append(new_l[i])
            else:
                mat3.append(new_l[i])

        mat=[]
        mat.append(mat0)
        mat.append(shift_right(mat1,1))
        mat.append(shift_right(mat2,2))
        mat.append(shift_right(mat3,3))
        #print(mat)

        m=0
        nxt=[]
        while(m!=4):
            for i in range(len(mat)):
                z=mat[i][m]
                nxt.append(check_x(hex(Sbox_inv[int(z,16)])))
            m+=1
        i_main=1
        while(i_main!=10):
            #print(i_main)
            new_l=[]
            for i in range(i_main,i_main+1):
                for j in range(len(add_k[i])):
                    z=hex(int(add_k[i][j],16)^int(nxt[j],16))
                    new_l.append(check_x(z))
            #print(new_l)
            new_l1=[]
            new_l2=[]
            new_l3=[]
            new_l0=[]
            ab=0
            for i in range(len(new_l)):
                if i==0 or i==4 or i==8 or i==12:
                    new_l0.append(new_l[i])
                elif i==1 or i==5 or i==9 or i==13:
                    new_l1.append(new_l[i])
                elif i==2 or i==6 or i==10 or i==14:
                    new_l2.append(new_l[i])
                else:
                    new_l3.append(new_l[i])

            mtr=[]
            mtr.append(new_l0)
            mtr.append(new_l1)
            mtr.append(new_l2)
            mtr.append(new_l3)
            #print(mtr)
            tmp1=[]
            tmp2=[]
            tmp3=[]
            tmp0=[]
            cnt=0
            while(cnt!=4):
                x=0
                z=0
                for i in range(0,1):
                    for j in range(len(mtr[i])):
                        z=mat_mul(mix_coli[i][j],mtr[j][cnt])
                        x=x^z
                    tmp0.append(check_x(hex(x)))
                cnt+=1
        
            cnt=0
            while(cnt!=4):
                x=0
                z=0
                for i in range(1,2):
                    for j in range(len(mtr[i])):
                        z=mat_mul(mix_coli[i][j],mtr[j][cnt])
                        x=x^z
                    tmp1.append(check_x(hex(x)))
                cnt+=1

            cnt=0
            while(cnt!=4):
                x=0
                z=0
                for i in range(2,3):
                    for j in range(len(mtr[i])):
                        z=mat_mul(mix_coli[i][j],mtr[j][cnt])
                        x=x^z
                    tmp2.append(check_x(hex(x)))
                cnt+=1

            cnt=0
            while(cnt!=4):
                x=0
                z=0
                for i in range(3,4):
                    for j in range(len(mtr[i])):
                        z=mat_mul(mix_coli[i][j],mtr[j][cnt])
                        x=x^z
                    tmp3.append(check_x(hex(x)))
                cnt+=1

            inv_col=[]
            inv_col.append(tmp0)
            inv_col.append(shift_right(tmp1,1))
            inv_col.append(shift_right(tmp2,2))
            inv_col.append(shift_right(tmp3,3))
            #print(inv_col)

            nxt=[]
            cnt=0
            while(cnt!=4):
                for i in range(len(inv_col)):
                    tmp=Sbox_inv[check_256(int(inv_col[i][cnt],16))]
                    nxt.append(check_x(hex(tmp)))
                cnt+=1
            #print(nxt)
            i_main+=1


        new_l=[]
        for i in range(i_main,i_main+1):
            for j in range(len(add_k[i])):
                #print(add_k[i][j])
                z=hex(int(add_k[i][j],16)^int(nxt[j],16))
                new_l.append(check_x(z))
        #print(new_l)
        ascii_l=[]
        for i in range(len(new_l)):
            ascii_l.append(int(new_l[i],16))
        #print(append_length)

        final_l=[]
        for i in range(0,16-int(append_length)):
            final_l.append(chr(ascii_l[i]))

        decrypt_msg=''.join(map(str,final_l))
        print("Decrypted Message:\t",decrypt_msg)
        
AESdecryption()
