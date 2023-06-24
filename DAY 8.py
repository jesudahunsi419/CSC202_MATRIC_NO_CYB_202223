# Prime number checker


# numbe = int(input("Check this number"))
# def primenum_ch(numbe):
#     ti_prime= True
#     for n in range(2, numbe -1) :
    
#      numbe % n
#      if numbe % n == 0 :
#         ti_prime = False
#        # print(f"This is not a prime number")
#     if ti_prime :
#         print(f"This is a prime number")
#     else :
#        print(f"This is not a prime number")

# primenum_ch(numbe)

# Ceasar Cipher

alphabet = [ "a","b","c" ,"d" ,"e","f","g" ,"h" ,"i","j","k" ,"l" ,"m","n", "o","p" ,"q" ,"r","s","t" ,"u" ,"v","w", "x", "y" ,"z","a","b","c" ,"d" ,"e","f","g" ,"h" ,"i","j","k" ,"l" ,"m","n", "o",
 "p" ,"q" ,"r","s","t" ,"u" ,"v","w","x","y","z"]
direct = input(f"Type 'encode' to encrypt , Type 'decode' to decrypt\n").lower()
tec = input("Type your Message\n").lower()
shIft =int(input("Type your Shift number\n"))
# Encrypt Function
# if direct== "encode" :
#      encrypt( text = tec, sh_num= shIft)

# def caesar ():
  
#  if direct== "encode" :
#      encrypt( text = tec, sh_num= shIft)
#  elif direct == "decode" :
#      decrypt(ted= tec, shif= shIft)
def Caesar(start_txt, sh_num, cipher_direct) :
     end_txt= ""
     for letter in start_txt :
          position = alphabet.index(letter)

          
          if cipher_direct == "decode" :
            sh_num *= -1
            new_pos = position + sh_num
            end_txt += alphabet[new_pos]

          elif cipher_direct == "encode" :
          # new_pos = position + sh_num
           sh_num *= 1
           new_pos = position + sh_num
           end_txt += alphabet[new_pos]
          
     print(f" The {cipher_direct}d text is {end_txt}")

Caesar( start_txt= tec, sh_num= shIft, cipher_direct=direct)
# def encrypt(text , sh_num):
#     ciphe_txt =""
#     for letr in text :
#         position =alphabet.index(letr)
#         new_pos = position + sh_num
#         new_letr= alphabet[new_pos]
#         ciphe_txt += new_letr
#         #print(new_pos)
#     print(f" The encoded text is {ciphe_txt}")

# #encrypt( text = tec, sh_num= shIft) 

# # Decrypt function
# def decrypt( ted, shif):
#       ciphe_txt =""
#       for lert in ted :
#             position =alphabet.index(lert)
#             new_pos = position - shif
#             new_letr= alphabet[new_pos]
#             ciphe_txt += new_letr
#       print(f" The encoded text is {ciphe_txt}")
# # #decrypt(ted= tec, shif= shIft)    
# # if direct== "encode" :
# #      encrypt( text = tec, sh_num= shIft)
# # elif direct == "decode" :
# #      decrypt(ted= tec, shif= shIft)
# # else :
# #      print(f" Check the options again")
# caesar()