def validate_user(user):
    if "id" in user and "name" in user and "email" in user:
        if (
            isinstance(user["id"], int)
            and isinstance(user["name"], str)
            and isinstance(user["email"], str)
            and "@" in user["email"]
        ):
            return True
    
    return False
    
    