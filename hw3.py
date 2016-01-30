import hashlib


def read_chunks(file_obj, chunk_size=1024):
    while True:
        chunk = file_obj.read(chunk_size)
        if not chunk:
            return
        yield chunk 

def calculate_hash(file_name):
    with open(file_name, 'r') as file_obj:
        chunks = list(read_chunks(file_obj))
        print 'Number of chunks: %d' % len(chunks)
                
        file_hash = reduce(lambda h, chunk: hashlib.sha256(chunk + h).digest(), reversed(chunks), '')
        return file_hash.encode('hex')
    

def main():
    assert calculate_hash('Video2.mp4') == '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8', 'SHA256 for Video2'
    print 'Answer: %s' % calculate_hash('Video1.mp4')
    
if __name__ == '__main__':
    main()