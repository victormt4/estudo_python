s1 = {1, 2, 3}

# {2,3,4}
s2 = {2, 2, 3, 4}

print(s1, s2)

# operações

print('\nunião:')
print(s1 | s2)

print('\nintersecção:')
print(s1 & s2)

print('\nleft join:')
print(1 in (s1 - s2))

print('\n"ou" exclusivo:')
print(s1 ^ s2)

print('\nadicionando valor ao conjunto:')
s1.add(5)
print(s1)

# conjunto imutável
frozenset(s1)
