import re
N = input()
pattern = '^[987]\d{9}'
result = re.match(pattern,N)
if result:
	print("VALID")
else:
	print("NOT VALID")