enter_user_name = input('Enter username: ')
enter_password = input('Enter password: ')

password_length = len(enter_password)
hidden_password = '*' * password_length

print(f'{enter_user_name}, your password, {hidden_password}, is {len(enter_password)}, letters long')