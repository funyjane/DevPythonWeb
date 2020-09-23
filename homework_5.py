creds = {'dan' : 'test321', 'misha' : 'test123'}

def enter_creds(func):
    

    def wrapper(*args):
        user_name = input("Please enter your username: ")
        user_pwd = input("Please enter your password: ")
        if creds.get(user_name) == user_pwd:
            print('correct')
        else:
            print('user name or password incorrect')
    # если не сработает
        try:
            if creds[user_name] == user_pwd:
                print('correct')
            else:
                print('wrong password')
        except:
            print('wrong user name')
    return wrapper


@enter_creds
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
