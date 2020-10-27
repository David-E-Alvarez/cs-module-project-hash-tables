class HashTableEntry:#"node" class equivalent
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # def __repr__(self):
    #     return f'HashTableEntry(key: {repr(self.key)}, value: {repr(self.value)})'


class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        """print entire linked list"""
        if self.head is None:
            return "[Empty List]"
        cur = self.head
        s = ""

        while cur != None:
            s += f'({cur.value})'
            #print("s: ", s)
            if cur.next is not None:
                s += '-->'
            cur = cur.next

        return s

    def insert_at_head(self,node):
        node.next = self.head
        self.head = node

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
        self.buckets = [None] * self.capacity
        self.num_of_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = self.num_of_items / len(self.buckets)
        return load_factor


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
        adapted from https://gist.github.com/mengzhuo/180cd6be8ba9e2743753 (typed out; not copied and pasted)
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def hash_index(self, key):#only takes in strings; no numbers
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    #get, put, and delete using hashtableentry
    def put(self, key, value):
        #ll = LinkedList()
        #1.)get index
        index = self.hash_index(key)
        cur = self.buckets[index] 
        #2.) check to see if place you want to put value at in hash table is taken
        if cur is not None and cur.key != key:
            cur = cur.next
        if cur is not None:
            cur.value = value
        else:
            hte = HashTableEntry(key,value)#like node
            hte.next = self.buckets[index]
            self.buckets[index] = hte 
            self.num_of_items += 1

    def get(self, key):
        index = self.hash_index(key)
        cur = self.buckets[index]
        while cur != None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None

    def delete(self, key):
        index = self.hash_index(key)
        self.buckets[index].value = None
        self.num_of_items -= 1




    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        note: common to double size of hash table
        # when resizing items need to be re-inserted rather than just copied because items have to be re-run through
        # hashing function because hashing function takes into account the size of hash table when determining index it returns
        Implement this.
        """
        # Your code here
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("lambda", "school")

    print('---->',ht.get("lambda"))
    print(ht.buckets)
    #ht.delete("lambda")
    #print(ht.buckets)
    
    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_3", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    #print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")


# def put(self, key, value):
#         """
#         Store the value with the given key.

#         Hash collisions should be handled with Linked List Chaining.

#         Implement this.
#         """
#         # Your code here
#         index = self.hash_index(key)
#         #print("index in put: ", index)
#         self.buckets[index] = value
#         self.num_of_items += 1


#     def delete(self, key):
#         """
#         Remove the value stored with the given key.

#         Print a warning if the key is not found.

#         Implement this.
#         """
#         # Your code here
#         index = self.hash_index(key)
#         self.buckets[index] = None
#         self.num_of_items -= 1


#     def get(self, key):
#         """
#         Retrieve the value stored with the given key.

#         Returns None if the key is not found.

#         Implement this.
#         """
#         # Your code here
#         index = self.hash_index(key)
#         return self.buckets[index]