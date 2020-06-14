# Queue + set
from collections import deque
class Logger(object):
    def __init__(self):
        self._msg_set = set()
        self._msg_queue = deque()
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, 
        otherwise returns false.
        """
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:        # determine the time difference of incoming
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
            else:
                break
        
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp))
            return True
        else:
            return False
        
# Time: O(N) where N is the size of the queue. In the worst case, all the messages in the queue become obsolete. As a result, we need clean them up.
# Space: O(N) where N is the size of the queue. We keep the incoming messages in both the queue and set. The upper bound of the required space would be 2N, if we have no duplicate at all.
        


# Method 2: Hashtable / Dictionary
class Logger(object):
    def __init__(self):
        self.msg_dict = {}         # Initialize your data structure here.
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, 
        otherwise returns false.
        """
        # only two case, we return True
        if message not in self.msg_dict:              # case 1: add the message and print
            self.msg_dict[message] = timestamp
            return True

        if timestamp - self.msg_dict[message] >= 10:  # case 2: update timestamp of message
            self.msg_dict[message] = timestamp
            return True
        
        return False
        
# Time: O(1). The lookup and update of the hashtable takes a constant time.
# Space: O(M) where M is the size of all incoming messages. Over the time, the hashtable would have an entry for each unique message that has appeared.