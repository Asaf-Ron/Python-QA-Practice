def validatade_credentials(username, password):
    if username == "":
        return "Username is required"
    elif len(username) < 4:
        return "Username is too short"
    elif password == "":
        return "Password is required"
    elif len(password) < 8:
        return "Password is too short"
    elif not any(char.isdigit() for char in password):
        return "Password must contain at least one digit"
    else:
        return "Login valid!"