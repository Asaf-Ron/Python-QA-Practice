def validate_password(password):
    if len(password) < 8:
        return False
    for character in password:
        if character.isdigit():
            return True

    return False