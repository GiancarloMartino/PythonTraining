username = input('Please insert your username: ')
password = input('Please enter your password: ')
password_length = len(password)
crypted_password = '*' * password_length
print(f'Dear {username}, your password {crypted_password} is {password_length} letters long')
