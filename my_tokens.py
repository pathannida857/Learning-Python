# Keywords

import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))
print(keyword.softkwlist)
print(len(keyword.softkwlist))

print(f'total keywords in python is {len(keyword.softkwlist)+len(keyword.kwlist)}')