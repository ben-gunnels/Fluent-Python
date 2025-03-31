
"""
    The __missing__ method can be added to a subclass of dict and will be called on dict.__getitem__.
    The __missing__ method will define what is to be done when a key is missing from the dict.
    This can allow you to check for alternate datatype key inputs by default.
"""

class StringKeyDict(dict):
    def __missing__(self, key):
        if isinstance(key, str): # If the key has been converted to a string, then it is indeed missing from the dictionary at this point
            raise KeyError(key)
        return self[str(key)]
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
        
    def __contains__(self, key):
        # Allows for the key to be of the original type of key, or string type
        return key in self.keys() or str(key) in self.keys()
    

board_pins = [("1", "A01"), ("4", "A04"), (6, "P06"), (7, "P07")]

bpskd = StringKeyDict(board_pins)

queries = [1, 4, 6, 7, 2]

# What happens here? Is the behavior as expected?
for query in queries:
    print(bpskd[query])