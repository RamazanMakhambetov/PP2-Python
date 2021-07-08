import re

s = input()
print(re.search(r'([0-9a-zA-Z])\1+',
      s).group(1)) if re.search(r'([0-9a-zA-Z])\1+', s) else print(-1)