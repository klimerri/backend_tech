def validate_role(role: str):
    allowed = {"admin", "dispatcher", "engineer"}
    if role not in allowed:
        raise ValueError("Invalid role")
    return role