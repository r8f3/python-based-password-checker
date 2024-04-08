def is_password_in_file(password, filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if password.strip() == line.strip():
                    return True
    except FileNotFoundError:
        print("File not found.")
    return False


def is_password_weak(password):
    upper_chars = sum(1 for char in password if char.isupper())
    lower_chars = sum(1 for char in password if char.islower())
    digits = sum(1 for char in password if char.isdigit())
    special_chars = sum(1 for char in password if not char.isalnum() and not char.isspace())

    print("Upper chars:", upper_chars)
    print("Lower chars:", lower_chars)
    print("Digits:", digits)
    print("Special chars:", special_chars)

    if upper_chars != 0 and lower_chars != 0 and digits != 0 and special_chars != 0:
        if len(password) >= 10:
            print("The strength of password is strong.\n")
            return False, "Password is strong"
        else:
            print("The strength of password is medium.\n")
            return False, "Password is medium"
    else:
        reasons = []
        if upper_chars == 0:
            reasons.append("Password must contain at least one uppercase character")
        if lower_chars == 0:
            reasons.append("Password must contain at least one lowercase character")
        if digits == 0:
            reasons.append("Password must contain at least one digit")
        if special_chars == 0:
            reasons.append("Password must contain at least one special character")
        return True, ", ".join(reasons)


  
def is_password_strong(password, filename=None):
    weak, weak_reason = is_password_weak(password)
    if weak:
        return False, weak_reason
    if filename and is_password_in_file(password, filename):
        return False, "Password is present in the list"
    return True, "Password is strong"



def main():
    passwords = input("Enter your passwords separated by commas: ").split(',')
    filename = input("Enter the directory of your wordlist (leave blank if none): ")
    
    for password in passwords:
        password = password.strip()
        is_strong, message = is_password_strong(password, filename)
        if is_strong:
            print(f"{password}: Password is strong")
        else:
            print(f"{password}: {message}")


if __name__ == "__main__":
    main()
