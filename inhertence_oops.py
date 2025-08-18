
class user:
  def __init__(self,username,password):
    self.username = username
    self.__password = password
  
  def get_password(self):
    return self.__password

class admin(user):
  def login(self,input_password):
    if input_password == self.get_password():
      print(f"{self.username} just logged in")
      return True
    else:
      print("invalid password")
      return False

a = admin("ram",456)

print(a.username)
print(a.get_password())

a.login(456)