default_username = "admin"
default_password = "python123"
def validate_login(username, password):
    if username == "" or password == "":
        return "Fields cannot be empty"
    
    if username == default_username and password == default_password:
        return "Login successful!"

    if username == default_username and password != default_password:
        return "Invalid password"
    
    if username != default_username:
        return "User not found"
    
    