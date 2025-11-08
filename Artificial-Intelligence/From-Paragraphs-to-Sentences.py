import re
import sys

text = sys.stdin.read().strip()

sentences = re.split(r'(?<=[.!?])\s+', text)

for s in sentences:
    s = s.strip()
    if s:  
        print(s)
