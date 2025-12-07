users_db = {}  # fake in-memory database

def register(username: str, password: str):
    """Simple user registration logic for testing."""
    
    # basic validation
    if not username or not password:
        return {"success": False, "message": "Username and password required."}

    if username in users_db:
        return {"success": False, "message": "User already exists."}

    if len(password) < 6:
        return {"success": False, "message": "Password must be at least 6 characters."}

    # store user
    users_db[username] = {
        "password": password
    }

    return {"success": True, "message": f"User '{username}' registered successfully."}


# Example tests
if __name__ == "__main__":
    print(register("mux", "123456"))
    print(register("mux", "anotherpass"))
    print(register("", "123"))
    print(register("newuser", "short"))
