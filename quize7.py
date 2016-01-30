

def main():
  cipher1 = 0x09e1c5f70a65ac519458e7e53f36  
  print '{:028X}'.format(cipher1)
  
  message1 = ''.join(["{:02X}".format(ord(ch)) for ch in "attack at dawn"])
  print message1
  
  message2 = ''.join(["{:02X}".format(ord(ch)) for ch in "attack at dusk"])
  print message2
  
  cipher2 = int(message2, base=16) ^ (int(message1, base=16) ^ cipher1)
  print 'result:'
  print '{:028X}'.format(cipher2)
  

if __name__ == "__main__":
  main()