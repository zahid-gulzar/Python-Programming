# => You can combine strings with (+)

first_name = 'Zahid'
last_name = 'Gulzar'

print(first_name + last_name)                # Output: ZahidGulzar (no space)
print('Hello ' + first_name + ' ' + last_name)  # Output: Hello Zahid Gulzar

# -------------------------------------------------------------------

# => Custom string formatting methods

# 1. String concatenation (less readable)
output1 = 'Hello, ' + first_name + ' ' + last_name

# 2. Using .format() with placeholders {}
output2 = 'Hello, {} {}'.format(first_name, last_name)

# 3. Using .format() with index numbers
output3 = 'Hello, {0} {1}'.format(first_name, last_name)

# 4. Using f-strings (Python 3.6+; cleanest and fastest)
output4 = f'Hello, {first_name} {last_name}'

print(output1)
print(output2)
print(output3)
print(output4)