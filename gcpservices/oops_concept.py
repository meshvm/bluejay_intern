# from django.shortcuts import render
# from django.http import HttpResponse
import rsa
import random


# Create your views here.
# To Encrypt
class Encryption:
    # generate public and private keys with
    # rsa.newkeys method,this method accepts
    # key length as its parameter
    # key length should be atleast 16
    def __init__(self):
        self.publicKey, self.privateKey = rsa.newkeys(512)

    def compress_str(self, message):
        # this is the string that we will be encrypting
        # rsa.encrypt method is used to encrypt
        # string with public key string should be
        # encode to byte string before encryption
        # with encode method
        encMessage = rsa.encrypt(message.encode(), self.publicKey)

        print("original string: ", message)
        print("encrypted string: ", encMessage)
        return encMessage

    def decompress(self, encMessage):
        # the encrypted message can be decrypted
        # with ras.decrypt method and private key
        # decrypt method returns encoded byte string,
        # use decode method to convert it to string
        # public key cannot be used for decryption
        decMessage = rsa.decrypt(encMessage, self.privateKey).decode()

        print("decrypted string: ", decMessage)
        return decMessage


    def get_me_newurl(self,org_url):
        origin_dict = dict()
        origin_dict["org_url"]=org_url
        ecrypted_data = (Encryption.compress_str(self,org_url))
        origin_dict.update( encryption= str(ecrypted_data))

        # origin_decrypt = Encryption.decompress(origin_dict["encryption"])
        shorted_url = generate_keys()
        origin_dict.update(shorted_url=str(shorted_url))
        final_result = str("https://www.example.com/") + shorted_url
        return final_result

def generate_keys():
    randomword = ''
    choose_chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
    randomword += str(''.join(random.sample(choose_chars, 8)))
    return randomword


# def shorturlhome(request):
#     return render(request, 'shorturl/homeURL.html')


# def newurl(request):
#     # org_url = request.GET.get('inputurl')
#     org_url="www.google.com"
#     link= Encryption()
#     new_url = link.get_me_newurl(org_url)
#     print(new_url)
#     # return render(request, 'shorturl/newurl.html', {'org_url': new_url})
if __name__=='__main__':
    org_url = "www.google.com"
    link = Encryption()
    new_url = link.get_me_newurl(org_url)
    print(new_url)