string = "asdvcvcwqewgbgfdasdasdazzczx"  # Sample string
dict_counter = {}  # Empty dict for holding characters
                   # as keys and count as values
for char in string:  # Traversing the whole string
                # character by character
    if not dict_counter or char not in dict_counter.keys(): # Checking whether the dict is
                                                            # empty or contains the character
        dict_counter.update({char: 1}) # If not then adding the
                                       # character to dict with count = 1
    elif char in dict_counter.keys(): # If the character is already
                                      # in the dict then update count
        dict_counter[char] += 1
for key, val in dict_counter.items(): # Looping over each key and
                                      # value pair for printing
    print(key, val)