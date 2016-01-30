import urllib2

CIPHERTEXT = 'f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4'.decode('hex')

TARGET = 'http://crypto-class.appspot.com/po?er='

# TODO: implement using MapReduce

def strxor(a, b):
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

class PaddingOracle(object):
    
    def encrypt(self, ciphertext, encrypted=''):
        encrypted = encrypted.decode('hex')
        message_byte_len =  len(ciphertext) - 16
        ciphertext_end = ciphertext[message_byte_len:]

        for i in range(len(encrypted), message_byte_len):
            start_search = message_byte_len - 1 - i
            ciphertext_start = ciphertext[:start_search]
            
            padding = chr(i + 1)

            encrypted_ciphertext = ciphertext[start_search + 1:message_byte_len]
            encrypted_xor_padding = strxor(encrypted_ciphertext, strxor(encrypted, padding * i))
            
            current_symbol = ciphertext[start_search]
            current_symbol_xor_padding = strxor(current_symbol, padding)
            
            encrypted_with_cyphertext_end = encrypted_xor_padding + ciphertext_end
            
            for j in range(0, 256):
                message_symbol = chr(j)
    
                c = ciphertext_start + strxor(current_symbol_xor_padding, message_symbol) + encrypted_with_cyphertext_end
                if self._query(c.encode('hex')):
                    encrypted = message_symbol + encrypted
                    print 'symbol: %s' % message_symbol.encode('hex')
                    break
        
    
        return encrypted
            
    def _query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            urllib2.urlopen(req)          # Wait for response
            print "Ok"
        except urllib2.HTTPError, e:          
#             print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding

def main():
    print CIPHERTEXT.encode('hex')
    po = PaddingOracle()
    encrypted = po.encrypt(CIPHERTEXT, '')
    print 'result: %s' % encrypted

if __name__ == "__main__":
    main()