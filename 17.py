def check_password(func):
    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")
        if password == "Иван_Олегович":
            return func(*args, **kwargs)
        else:
            print("В доступе отказано.")
            return None
    return wrapper

# Пример использования декоратора
@check_password
def protected_function():
    print("Доступ к защищенной функции получен!")

# Вызов функции
protected_function()
