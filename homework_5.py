creds = {'dan' : 'test321', 'misha' : 'test123'}

def decorator(func):
  def wrapper(*args, **kwargs):
        login = input('Enter login: ')
        password = input('Enter password: ')
        if login not in creds.keys() or creds[login] != password:
            return 'Autorization required'
        a = func(*args, **kwargs)
        return a
  return wrapper


@decorator
def sum_numbers(a, b):
    return a+b

print(sum_numbers(2, 3))