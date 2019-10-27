from collections import  deque

# declare contants
CACHE_SIZE = 0
CACHE_TRIGGER = 0
PUSHED_CACHE_OBJ = 0
DUMPED_LRU = 0
class ExpiringCache:

    def __init__(self):
        self.CACHE_SIZE = CACHE_SIZE
        self.cache_storage = deque()
        self.req_count = 0

    def push_cache(self, arg_item):
        if arg_item in self.cache_storage:
            self.cache_storage.remove(arg_item)
            self.cache_storage.appendleft(arg_item)
            self.req_count = self.req_count + 1
            return CACHE_TRIGGER
        
        if (len(self.cache_storage) + 1) > self.CACHE_SIZE:
            self.cache_storage.pop()
            self.cache_storage.appendleft(arg_item)
            return DUMPED_LRU

        else:
            self.cache_storage.appendleft(arg_item)
            return PUSHED_CACHE_OBJ

        def req_count(self):
            return self.req_count

        def storage_content(self):
            format(self.cache_converter())


        def cache_converter(self):
            return list(self.cache_storage)

        def result_request(self):
            return self.req_count

if __name__ == "__main__":
    pass




