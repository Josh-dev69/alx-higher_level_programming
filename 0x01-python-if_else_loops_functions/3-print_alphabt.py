#!/usr/bin/python3
for alpha in range(97, 123):
    if chr(alpha) == 'e' or chr(alpha) == "q":
        continue
    print(f"{chr(alpha)}", end='')
