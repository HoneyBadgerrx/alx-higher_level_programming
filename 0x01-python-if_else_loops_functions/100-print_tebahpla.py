#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    if i % 2 != ord('z') % 2:
        i = i - (ord('a') - ord('A'))
    print(f"{i:c}", end='')
