import re

name = 'Torvalds'

print(re.sub('[aeiouAEIOU]', '', name))