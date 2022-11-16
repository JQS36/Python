"""
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""

height = 9 
width = 9 * 3
"""top_lines = []
for i in range(clm):
    if i%2 != 0:
        top_lines.append(i)
for i in top_lines:
    print((".|."*i).center(row,"-"))
print("WELCOME".center(row,"-"))
for i in sorted(top_lines, reverse=True):
    print((".|."*i).center(row,"-"))"""

font = "WELCOME"
half = tuple(f"{'.|.'*i:-^{width}}" for i in range(1, height, 2))

print(*half, font.center(width, '-'), *half[::-1], sep='\n')