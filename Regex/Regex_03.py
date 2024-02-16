import re

text = "Toyota Supra, Ram 1500"

res = re.sub(r" ","-", text)
res = re.sub(r",", ".", res)

print(res)
