# your improved User class goes here
class User():
    all_posts = {}
    all_users = []
    
    
    def __init__(self, name, email, drivers_license):
        self.name = name
        self.email = email
        self.drivers_license = drivers_license
        self.posts = []
    
    def __str__(self):
        return f"{self.name}" 
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_val:str):
        if name_val.isalpha():
            self._name = name_val.title()
        else:
            raise Exception("The name should be a `str` value")
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email_val):
        if ('@' in email_val) and (".com" == email_val[-4:]):
            self._email = email_val
        else:
            raise Exception("This isn't a valid email address") 
    
    
    def create_post(self):
        post = input("Please enter your post:\n")
        new_post = self.posts.append(post)
        
        print(new_post)
    
     
# calling on the class to create a user 
    @classmethod       
    def new_user(cls):
        user_info = {
            "name": input("Please enter your name:\n"),
            "email": input("Please enter your email:\n"),
            "drivers_license": input("Please enter your license number:\n")
        }   
        new_user = User(**user_info) 
        cls.all_users.append(new_user)   
        return f"{new_user} was created successfully"

print(User.new_user())
User.create_post()

