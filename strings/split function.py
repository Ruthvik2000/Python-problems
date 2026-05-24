text = 'hello world'
# Splits at space 
print(text.split()) 

text = 'hello, world'
# Splits at ',' 
print(text.split(', ')) 

text = 'hello:world'
# Splitting at 'l' 
print(text.split('l'))


"""
output:
['hello', 'world']
['hello', 'world']
['he', '', 'o:wor', 'd']


"""
