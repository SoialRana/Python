from collections import deque

bank= deque(["Rahim","karim","shuvo"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
if not bank:
    print("no person left")