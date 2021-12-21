import base64
import time
import os
from termcolor import colored
from pyfiglet import Figlet

Banner = Figlet(font='standard')
def printF(text='', color='green'):
    print("\n\n"+colored(Banner.renderText(text), 'green')+"\n\n")


printF("ENCRYPTION")

def str_data(file_name):
    file=open(file_name,'rb')
    file_data=file.read()
    image64=base64.encodebytes(file_data)
    str_image=str(image64)
    str_image=str_image[2:-1]
    return str_image

def encrypt(file_delete):
    file_name=input("\nPlease enter the file name with address$ ")
    try:
        str_image=str_data(file_name)
    except Exception as e:
        print(e+"\n")
        print("I can't read the file")
        time.sleep(1)
        main()
    try:
        encrypteddata=''
        alphabets='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        enc_alphabets='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        for i in str_image:
            if i in alphabets:
                position=alphabets.find(i)
                encrypteddata+=enc_alphabets[position]
            else:
                encrypteddata+=i

        with open(file_name+".enc",'w+') as f:
            f.write(encrypteddata)
        if 'del' == file_delete:
            os.system(f'del {file_name}')
        elif 'no_del' == file_delete:
            pass
    except Exception as e:
        print(e)
        print("Oops! Can't decode the file.")
        time.sleep(1)
        main()

def decrypt():
    file_name=input("\nPlease enter the file name with address$ ")
    if '.enc' in file_name:
        try:
            with open(file_name,'r') as enc_file:
                enc_str=enc_file.read()
        except Exception as e:
            print(f"Error Occured {e}")
            # print(f"No file found named {file_name}")
            time.sleep(1)
            main()
    else:
        print(f"No file found named {file_name}")
        time.sleep(1)
        main()

    alphabets='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    enc_alphabets='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    decrypteddata=''
    try:
        for i in enc_str:
            if i in enc_alphabets:
                position=enc_alphabets.find(i)
                decrypteddata+=alphabets[position]
            else:
                decrypteddata+=i
        # print(decrypteddata)
        file_name=file_name.replace('.enc','')
        decrypteddata=decrypteddata.encode()
        decrypteddata_byte=decrypteddata.decode('unicode-escape').encode('ISO-8859-1')
        # print(decrypteddata_byte)
        file_name=file_name.replace('.enc','')
        myimage=open(file_name,'wb')
        decode=base64.decodebytes(decrypteddata_byte)
        myimage.write(decode)
    except Exception as e:
        print(f"Error occured: {e}")
        time.sleep(1)
        main()



def main():
    while True:
        print("What you want to do. Press")
        print("1. For Encryption of file with main file deletion")
        print("2. For Encryption of file without main file deletion")
        print("3. For decryption of an ecrypted file")
        print("Press ctrl+c to exit")
        operation = int(input("$ "))

        if 1 == operation:
            encrypt('del')
        elif 2 == operation:
            encrypt('no_del')
        elif 3 == operation:
            decrypt()
        else:
            print("\nPlease select an appropriate option\n")
            time.sleep(1)


if __name__ == "__main__":
    main()  