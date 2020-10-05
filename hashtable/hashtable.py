class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.hash_table = [None] * capacity
        self.num_elements = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # number of items / num_slots
        return self.num_elements / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381

        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # hash the key and get an index
        i = self.hash_index(key)

        # Check if something already exists at that index
        if self.hash_table[i] != None:
            # print(f"Collision! Overwriting {repr(self.hash_table[i])}!")

            current_node = self.hash_table[i]

            while current_node is not None:

                # Check if it is a duplicate key and overwrite if nececessary
                if current_node.key == key :

                    current_node.value = value

                # otherwise check if next node is empty and place new value there
                elif current_node.next is None:

                    new_node = HashTableEntry(key, value)

                    current_node.next = new_node

                    # increment number of elements
                    self.num_elements += 1

                    print(f"Taken Node: {new_node.key, new_node.value}!")

                    print(f"Num elements: {self.num_elements}")

                # otherwise, go to the next node
                current_node = current_node.next
        
        else: 
            
            self.hash_table[i] = HashTableEntry(key, value)

             # increment number of elements
            self.num_elements += 1

            print(f"New Node: {key, value}!")

            print(f"Num elements: {self.num_elements}")

                
            

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # hash the key and get an index
        i = self.hash_index(key)
        # Check if Key is missing at that index
        if self.hash_table[i] is None:
            print(f"Key Not Found!")
        else:
            self.hash_table[i] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # hash the key and get an index
        i = self.hash_index(key)
        
        # Return the value from the array at the index
        # return self.hash_table[i]

        current_node = self.hash_table[i]
    
        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.key == key:
                return current_node.value
    
            # otherwise, go to the next node
            current_node = current_node.next

        return None 


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_ht = HashTable(new_capacity)

        # Rehashing
        for i in range(1, self.num_elements):
            
            new_ht.put("line_{i}", ht.get(f"line_{i}"))

        return new_ht



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"), f" - Line{i}")

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"), f" - what the")

    print("")
