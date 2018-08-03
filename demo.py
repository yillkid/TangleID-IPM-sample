import M2Crypto
import M2Crypto.BN as BN
import os
import json
from tangleid import new_claim, get_claim_info, get_all_claims_in_channel
import time
from random import SystemRandom

host_url = "http://localhost:8000"

msg_claim = {"extension":"tangleid", "command":"new_claim","uuid": \
"V9TCFLAOGGTAQATTJBLABAG9WY","channel":"","next_channel":"", "msg":"TestingMessage", "sign":""}
msg_get_all_claims_in_channel = {"extension":"tangleid", "command":"get_all_claims_in_channel","channel": ""}
msg_get_claim_info = {"command":"get_claim_info","hash_txn":""}

def addr_generate(length):
    alphabet = u'9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    generator = SystemRandom()

    return str(u''.join(generator.choice(alphabet) for _ in range(length)))

def generate_keypair_as_pem(key_len, exponent):
    def empty_callback():
        pass

    rsa = M2Crypto.RSA.gen_key(key_len, exponent, empty_callback)
    # Get RSA Public Key in PEM format
    buf = M2Crypto.BIO.MemoryBuffer('')
    rsa.save_pub_key_bio(buf)
    public_key = buf.getvalue()

    # Get Private Key in PEM format
    buf = M2Crypto.BIO.MemoryBuffer('')
    rsa.save_key_bio(buf, None)
    private_key = buf.getvalue() # RSA Private Key
    
    return (public_key, private_key)

def get_data_digest(data):
    msg_digest = M2Crypto.EVP.MessageDigest('sha256')
    msg_digest.update (data)
    digest =  msg_digest.digest()
    return digest

def generate_secure_msg(A_private_key, B_public_key, message):
    padding = M2Crypto.RSA.pkcs1_oaep_padding
    buf = M2Crypto.BIO.MemoryBuffer('')
    buf.write(B_public_key)
    rsa1 = M2Crypto.RSA.load_pub_key_bio(buf)
    cipher_message = rsa1.public_encrypt(message, padding)
    # Use A's private key to sign the 'cipher_message'
    digest1 = get_data_digest(cipher_message)
    rsa2 = M2Crypto.RSA.load_key_string(A_private_key)
    signature = rsa2.sign(digest1, 'sha256')
    return cipher_message, signature

def read_secure_msg(A_public_key, B_private_key, cipher_message, signature):
    try:
        # Use A's public key to verify 'signature'
        buf = M2Crypto.BIO.MemoryBuffer('')
        buf.write(A_public_key)
        rsa3 = M2Crypto.RSA.load_pub_key_bio(buf)                
        # Verify
        digest2 = get_data_digest(cipher_message)
        rsa3.verify(digest2, signature, 'sha256')
        # Use B's private key to decrypt 'cipher_message'
        rsa4 = M2Crypto.RSA.load_key_string(B_private_key)        
        padding = M2Crypto.RSA.pkcs1_oaep_padding
        plaintext_message = rsa4.private_decrypt(cipher_message, padding)
        return plaintext_message
    except Exception as err:        
        print 'Verify Fail:%r'% err
        raise 

if __name__ == '__main__':
    keylen = 1024         # 1024 bits
    exponent = 65537
    padding = M2Crypto.RSA.pkcs1_oaep_padding
    
    # Generate RSA key-pair in PEM files for public key and private key

    os.system('clear') 
    print "A plane issue a claim to B ..."
    raw_input("Press Enter to continue...")
 
    A_pub_key, A_priv_key = generate_keypair_as_pem(keylen, exponent)

    # Generate RSA key-pair in PEM files for public key and private key 
    B_pub_key, B_priv_key = generate_keypair_as_pem(keylen, exponent)

    print "A ans B generate RSA key pairs ..."
    raw_input("Press Enter to continue...")

    # A is sender, B is receiver
    msg_claim['addr'] = addr_generate(26)
    msg_claim['next_addr'] = addr_generate(26)

    print "A plan to issue B a claim : " + str(msg_claim)
    raw_input("Press Enter to continue...")

    # Sender's behavior
    cipher_msg, signature = generate_secure_msg(A_priv_key, B_pub_key, str(msg_claim['msg']))
    msg_claim['msg'] = cipher_msg.encode('base64')
    msg_claim['sign'] = signature.encode('base64')

    print "After encrypt the message, the claim : " + str(msg_claim)
    raw_input("Press Enter to continue...")

    print "Claim issue starting ..."
    txn_hash = new_claim(host_url, msg_claim)
    print "Done! The transaction hash is : " + str(txn_hash)
    raw_input("Press Enter to continue...")

    # Receiver's behavior
    print "B search txn hash in channel (IOTA ADDRESS) ... " + str(msg_claim['addr'])
    msg_get_all_claims_in_channel['channel'] = msg_claim['addr']

    str_claims = get_all_claims_in_channel(host_url, msg_get_all_claims_in_channel)

    # FIXME: String type list should not have square brackets and apostrophe
    str_claims = str(str_claims).replace("[","").replace("]","").replace("'", "")

    list_claims = str_claims.split()
    msg_get_claim_info['hash_txn'] = str(list_claims[0])
    claim_info = get_claim_info(host_url, msg_get_claim_info)

    claim_json = json.loads(claim_info)

    plain_text = read_secure_msg(A_pub_key, B_priv_key, claim_json['msg'].decode('base64'), claim_json['sign'].decode('base64'))
    print "B verify signature OK and got claim: " + str(plain_text)

