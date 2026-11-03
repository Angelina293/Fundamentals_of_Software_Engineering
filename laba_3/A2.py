import string

password = input("Введите пароль: ")
errors = []
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + "*-#"
if len(password) != 8:
    errors.append("Длина пароля не равна 8")
if password.lower() == password:
    errors.append("В пароле отсутствуют заглавные буквы")
if password.upper() == password:
    errors.append("В пароле отсутствуют строчные буквы")
if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отстутсвуют цифры")
if not any(symbol in "*-#" for symbol in password):
    errors.append("В пароле отсутсвуют специальные символы")
if not all(symbol in allowed for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")

if errors:
    for error in errors:
        print(error)
else:
    print("Надёжный пароль")
    