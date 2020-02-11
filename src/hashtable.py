# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        #Overwrite keys when same key entered
        if self.retrieve(key):
            self.remove(key)
        #Acquire index
        index = self._hash_mod(key)
        #Acqure the given Node
        node = self.storage[index]

        #If the node is empty at given index, add it and exit function
        if node is None:
            self.storage[index] = LinkedPair(key,value)
            return
        #Otherwise collision is dectected at given index
        #Iterate through the LL
        prev = node
        while node is not None:
            prev = node
            node = node.next
        #When the last node is found, add to it .next
        prev.next = LinkedPair(key,value)


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        #Acquire the index and node
        index = self._hash_mod(key)
        node = self.storage[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        #if nothing is found, return warning
        if node is None:
            return f"The given {key} is not in the hashtable"
        else:
            #The possible node has been found
            removed = node.value
            #Now delete the node appropriately
            if prev is None:
                #Either none or next possible match
                self.storage[index] = node.next
            else:
                #Point the subsequent node and delete
                prev.next = prev.next.next
            return removed

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        #Acquire the index
        index = self._hash_mod(key)
        #acquire the node at given index
        node = self.storage[index]

        #Loop through find the key or end of the list
        while node is not None and node.key != key:
            node = node.next
        
        #Once node is found, return if exists
        if node is None:
            return None
        else:
            return node.value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        #Create new Hashtable
        ht = HashTable(self.capacity*2)

        #Copy via loop
        for node in self.storage:
            current_node = node
            while current_node is not None:
                ht.insert(current_node.key, current_node.value)
                current_node = current_node.next
        
        #Update existing Hashtable

        self.capacity = self.capacity*2
        self.storage = ht.storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")