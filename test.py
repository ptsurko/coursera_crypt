
import collections

class Iterator(object):
#     def __getitem__(self, index):
#         if index > 10:
#             raise IndexError()
#         yield index * 10
    def __init__(self):
        self.index = 0
        
    def __iter__(self):
        return self
    
    def next(self):
        if self.index > 10:
            raise StopIteration()
        
        self.index += 1
        return self.index * 10
            
            
class LoggingDict(dict):
    print 'class'
    pass

class LoggingOD(LoggingDict, collections.OrderedDict):
    pass

def main():
    pass
#     print LoggingOD.__mro__
#     for i in Iterator():
#         print i
    

if __name__ == '__main__':
    main()