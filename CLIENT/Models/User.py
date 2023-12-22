class User():
    usernumber = 4
    def __init__(self, id:int, name, password, email) -> None:
        User.usernumber+=1
        self.id = id
        self.name = name
        self.password = password
        self.email = email

    def toJson(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'password' : self.password,
            'email' : self.email
        }
    
    @staticmethod
    def fromJson(jsonUser):
        newUser = User(
            int(jsonUser['id']),
            jsonUser['name'],
            jsonUser['password'],
            jsonUser['email']
        )
        return newUser