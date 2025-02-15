# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value, next_node = None):
        self.key = key
        self.value = value
        self.next = next_node

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        self.original_cap = self.capacity


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
        hashed = 5381
        for char in key:
            hashed = (hashed - 1) * 33 + ord(char)
        return hashed

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
        hashed_key = self._hash_djb2(key)
        hash_idx = hashed_key % self.capacity
        if self.retrieve(key):
            node = self.storage[hash_idx] 
            while node:
                if node.key == key:
                    node.value = value
                    break
                else:
                    node = node.next
        else:
            self.count += 1
            if self.count / self.capacity > 0.7:
                    self.resize(2)
                    hash_idx = hashed_key % self.capacity
            if self.storage[hash_idx]:
                node = LinkedPair(key, value, self.storage[hash_idx])
            else:
                node = LinkedPair(key, value)
            self.storage[hash_idx] = node
        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        if self.retrieve(key):
            hashed_key = self._hash_djb2(key)
            hash_idx = hashed_key % self.capacity
            node = self.storage[hash_idx]
            previous_node = None
            while node:
                if node.key == key:
                    self.count -= 1
                    if self.count / self.capacity < 0.2 and self.capacity > self.original_cap:
                        self.resize(0.5)
                        hash_idx = hashed_key % self.capacity
                    if previous_node:
                        previous_node.next = node.next
                        break
                    else:
                        self.storage[hash_idx] = None
                        break
                else:
                    previous_node = node
                    node = node.next
        else: 
            print('The key was not found')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashed_key = self._hash_djb2(key)
        hash_idx = hashed_key % self.capacity
        node = self.storage[hash_idx] 
        while node:
            if node.key == key:
                return node.value
            else:
                node = node.next
            


    def resize(self, mult):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        hash_table = HashTable(int(self.capacity * mult))
        for elem in self.storage:
            node = elem
            while node:
                hash_table.insert(node.key, node.value)
                node = node.next
        self.capacity = hash_table.capacity
        self.storage =  hash_table.storage
    
   



if __name__ == "__main__":
    ht = HashTable(2)
    ht.insert("line_1", "Tiny hash table")
    old_capacity = len(ht.storage)
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    new_capacity = len(ht.storage)
    print("")
    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    
    

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
