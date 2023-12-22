class Admin():
    admin_number=0
    def __init__(self, login_name, password, name, id:int):
        Admin.admin_number+=1
        self.login_name = login_name
        self.password = password
        self.name = name
        self.id = id

    def toJson(self):
        return {
            'login_name' : self.login_name,
            'password' : self.password,
            'name' : self.name,
            'id' : self.id
        }
    
    @staticmethod
    def fromJson(jsonAdmin):
        newAdmin = Admin(
            jsonAdmin['login_name'],
            jsonAdmin['password'],
            jsonAdmin['name'],
            int(jsonAdmin['id'])
        )
        return newAdmin
