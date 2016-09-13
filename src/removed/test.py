from bracketMatching import matchBrackets

inputString = "[AA[BB]CC[DD[EE[FF]GG]HH]II]"
lis = matchBrackets(inputString)

print(lis)
print(lis.pop())
print(lis)
