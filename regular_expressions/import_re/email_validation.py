import re

def is_valid_email(email):
    """
    Checks if an email address is potentially valid using a basic regex and
    optionally a verification service (recommended).

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email seems valid (basic check), False otherwise.
    """

    # Basic check (optional, can be removed)
    if re.search(r"^\w+@(\w+\.)?\w+\.(net|com|org)$", email.lower()):
        # Optional: Further validation using email verification service here
        return True  # Replace with your verification service call
    else:
        return False

def main():
    """
    Prompts the user for an email address and displays the validation result.
    """

    email = input("Enter an email address: ")

    if is_valid_email(email):
        print(f"{email} seems to be a valid email address (basic check).")
        print("For more reliable validation, consider using an email verification service.")
    else:
        print(f"{email} does not seem to be a valid email address (basic check).")

if __name__ == "__main__":
    main()
