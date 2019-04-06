import sys

mix_col=[[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]
Rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a]
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

def shift_right3(l):
    l2=[]
    '''l2[0]=l[1]
    l2[1]=l[2]
    l2[2]=l[3]
    l2[3]=l[0]'''
    for i in range(1,len(l)):
        l2.append(l[i])
    l2.append(l[0])
    return(l2)

def shift_left(l,n):
    l2=[]
    for i in range(n,len(l)):
        l2.append(l[i])
    for i in range(0,n):
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
def encryption_main():
    key='abcdefghijklmnop'
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

    msg=input("Enter Message(<16 char):\t")
    append_length=16-len(msg.encode('utf-8'))
    for i in range(0,16-len(msg.encode('utf-8'))):
        msg+=' '
        msg_val=[]
    for i in range(len(msg)):
        msg_val.append(hex(ord(msg[i])))

    new_l1=[]
    i_msg=0
    for ch in msg_val:
        x=check_x(ch)
        new_l1.append(x)

    new_l=[]
    for i in range(len(new_l1)):
        abc=(int(str(new_l1[i]),16)^int(str(add_k[i_msg][i]),16))
        new_l.append(check_x(hex(abc)))
    i_msg+=1

    while(i_msg!=10):
        current_l=[]
        for i in range(len(new_l)):
            current_l.append(check_x(hex(Sbox[int(str(new_l[i]),16)])))

        m1l1=[]
        m1l2=[]
        m1l3=[]
        m1l0=[]
        
        for i in range(len(current_l)):
            if i==0 or i==4 or i==8 or i==12:
                m1l0.append(current_l[i])
            elif i==1 or i==5 or i==9 or i==13:
                m1l1.append(current_l[i])
            elif i==2 or i==6 or i==10 or i==14:
                m1l2.append(current_l[i])
            elif i==3 or i==7 or i==11 or i==15:
                m1l3.append(current_l[i])

        mat_1=[]
        m1l1=shift_left(m1l1,1)
        m1l2=shift_left(m1l2,2)
        m1l3=shift_left(m1l3,3)
        mat_1.append(m1l0)
        mat_1.append(m1l1)
        mat_1.append(m1l2)
        mat_1.append(m1l3)
        nxt_mat=[]
        n1m0=[]
        n1m1=[]
        n1m2=[]
        n1m3=[]

        for i in range(0,1):
            cnt=0
            while(cnt<4):
                y=0
                y1=0
                x1=0
                z=0
                for j in range(len(mix_col[i])):
                    if mix_col[i][j]<=2:
                        y1=int(mix_col[i][j]*int(mat_1[j][cnt],16))
                        y=check_256(y1)
                    else:
                        z=2*int(mat_1[j][cnt],16)
                        y1=check_256(z)
                        y=int(int(y1)^int(mat_1[j][cnt],16))
                    x1=x1^y

                n1m0.append(check_x(hex(x1)))
                cnt+=1

        for i in range(1,2):
            cnt=0
            while(cnt<4):
                y=0
                y1=0
                x1=0
                z=0
                for j in range(len(mix_col[i])):
                    if mix_col[i][j]<=2:
                        y1=int(mix_col[i][j]*int(mat_1[j][cnt],16))
                        y=check_256(y1)
                    else:
                        z=2*int(mat_1[j][cnt],16)
                        y1=check_256(z)
                        y=int(int(y1)^int(mat_1[j][cnt],16))
                    x1=x1^y

                n1m1.append(check_x(hex(x1)))
                cnt+=1
    
        for i in range(2,3):
            cnt=0
            while(cnt<4):
                y=0
                y1=0
                x1=0
                z=0
                for j in range(len(mix_col[i])):
                    if mix_col[i][j]<=2:
                        y1=int(mix_col[i][j]*int(mat_1[j][cnt],16))
                        y=check_256(y1)
                    else:
                        z=2*int(mat_1[j][cnt],16)
                        y1=check_256(z)
                        y=int(int(y1)^int(mat_1[j][cnt],16))
                    x1=x1^y

                n1m2.append(check_x(hex(x1)))
                cnt+=1

        for i in range(3,4):
            cnt=0
            while(cnt<4):
                y=0
                y1=0
                x1=0
                z=0
                for j in range(len(mix_col[i])):
                    if mix_col[i][j]<=2:
                        y1=int(mix_col[i][j]*int(mat_1[j][cnt],16))
                        y=check_256(y1)
                    else:
                        z=2*int(mat_1[j][cnt],16)
                        y1=check_256(z)
                        y=int(int(y1)^int(mat_1[j][cnt],16))
                    x1=x1^y

                n1m3.append(check_x(hex(x1)))
                cnt+=1
    
        nxt_mat.append(n1m0)
        nxt_mat.append(n1m1)
        nxt_mat.append(n1m2)
        nxt_mat.append(n1m3)
        new_l=[]
        index_cnt=0
        '''while(index_cnt!=16):
        print(check_x(hex(int(str(add_k[i_msg][index_cnt]),16))))
        index_cnt+=1    index_cnt=0'''
        for i in range(len(nxt_mat)):
            for j in range(len(nxt_mat[i])):
                tmp=(int(nxt_mat[j][i],16))^(int(str(add_k[i_msg][index_cnt]),16))
                new_l.append(check_x(hex(tmp)))
                index_cnt+=1
    
        i_msg+=1

    current_l=[]
    for i in range(len(new_l)):
        current_l.append(check_x(hex(Sbox[check_256(int(new_l[i],16))])))

    m1l1=[]
    m1l2=[]
    m1l3=[]
    m1l0=[]

    for i in range(len(current_l)):
        if i==0 or i==4 or i==8 or i==12:
            m1l0.append(current_l[i])
        elif i==1 or i==5 or i==9 or i==13:
            m1l1.append(current_l[i])
        elif i==2 or i==6 or i==10 or i==14:
            m1l2.append(current_l[i])
        elif i==3 or i==7 or i==11 or i==15:
            m1l3.append(current_l[i])

    mat_1=[]
    m1l1=shift_left(m1l1,1)
    m1l2=shift_left(m1l2,2)
    m1l3=shift_left(m1l3,3)
    mat_1.append(m1l0)
    mat_1.append(m1l1)
    mat_1.append(m1l2)
    mat_1.append(m1l3)
    new_l=[]
    index_cnt=0

    for i in range(len(mat_1)):
        for j in range(len(mat_1[i])):
                tmp=(int(mat_1[j][i],16))^(int(str(add_k[i_msg][index_cnt]),16))
                new_l.append(check_x(hex(tmp)))
                index_cnt+=1

    cipher_text=' '.join(map(str,new_l))
    print('Cipher Text=',cipher_text)

    file=open("aes_values.txt",'w')
    file.write(cipher_text)
    file.write("\n")
    for i in range(len(add_k)):
        for j in range(len(add_k[i])):
            file.write(add_k[i][j])
            file.write(' ')
        file.write('\n')
    file.write(str(append_length))
    file.close()




encryption_main()
