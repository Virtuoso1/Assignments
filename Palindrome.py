from queue import Queue

class palindromeChecker:
    def __init__(self):
        self.stack = []
        self.queue = Queue()

    def push(self, data):
        self.stack.append(data)

    def enqueue(self, data):
        self.queue.put(data)

    def pop(self):
        return self.stack.pop()

    def dequeue(self):
        return self.queue.get()

def is_pali(s):
    checker = palindromeChecker()

    cleaned = ''.join(c.lower() for c in s if c.isalnum())

    for data in cleaned:
        checker.push(data)
        checker.enqueue(data)
    is_palindrome = True
    for _ in range(len(cleaned) // 2):
        if checker.pop() != checker.dequeue():
            is_palindrome = False
            break

    return is_palindrome
    #if is_palindrome:
    #    print(f"The word {s} is a palindrome.")
    #else:
    #    print(f"The word {s} is not a palindrome.")

#if __name__ == "__main__":
#    test = palindromeChecker()
#   is_pali("racecar")
