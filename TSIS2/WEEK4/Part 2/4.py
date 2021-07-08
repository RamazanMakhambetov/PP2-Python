import re

sub = re.findall(r'[^aeiouAEIOU]([aeiouAEIOU]{2,})(?=[^aiueoAEIOU])', input())

print('\n'.join([sub[i] for i in range(len(sub))]) if sub else -1)