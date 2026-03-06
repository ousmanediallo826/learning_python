import re
pattern = re.compile("[a-z]")
string = "Ousmane Diallo is college student at City Tech."

result = pattern.search( string)
print(result.group())
