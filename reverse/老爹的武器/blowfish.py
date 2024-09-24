from Crypto.Cipher import Blowfish
import codecs

class BlowfishCipher:
    def __init__(self):
        pass

    def encrypt(self, plaintext, key):
        key = key.encode("utf-8")
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        
        # 将明文填充到8字节的倍数
        plaintext = plaintext.ljust((len(plaintext) + 7) // 8 * 8)
        
        ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
        hex_encode = codecs.encode(ciphertext, 'hex_codec').decode('utf-8')
        return hex_encode

    def decrypt(self, ciphertext, key):
        key = key.encode("utf-8")
        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        
        ciphertext = codecs.decode(ciphertext, 'hex_codec')
        decrypted_text = cipher.decrypt(ciphertext).decode('utf-8').rstrip()
        return decrypted_text

if __name__ == '__main__':
    key = 'hetuno.O'
    blowfish_cipher = BlowfishCipher()
    encrypted_text='9d0ec04ba44e01aa19eaa0302a66a90f'
    decrypted_text = blowfish_cipher.decrypt(encrypted_text, key)
    print(f"加密: {encrypted_text}, 解密: {decrypted_text}")
    #zjnuctf{pAn9ba1}