s = 'udacity'
t = 'city'
i = 3

# find always retruns -1 when it cant find character

print s[i:].find(t)      # 0
# print s.find(t)[:i]      # fail, there is no way to select a subsequnce of characters form a number
print s[i:].find(t) + i
print s[i:].find(t[i:])
