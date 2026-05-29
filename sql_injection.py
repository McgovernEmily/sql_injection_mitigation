"""
CSE 453 - Lab 06: SQL Injection Mitigation
======================================================
Team Members: Ryan, Emily, Raquel
"""

# This function will create a username and password and return a SQL query string
def create_query(username, password):
    return f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}';"


# All team members need to create test cases for the function (making sure it's 
# valid input) should have at least 3 test cases
def test_create_query_validation(test_cases):
    for username, password in test_cases:
        query = create_query(username, password)
        print(f"  user='{username}', pass='{password}'")
        print(f"  → {query}")
        print()



def print_query(label, username, password):
    ''' Print the SQL query with a label '''
    print(f"[{label}]: => {create_query(username, password)}\n")

#Testing 3 Tautology Attacks, 3 union query attacks, 3 additional statement attacks, and 3 comment attacks.
# Added a label parameter to print the type of attack being tested
def test_tautology_attacks():
    print("=" * 60)
    print("ATTACK INPUT TEST CASES")
    print("=" * 60)
    
    print("Tautology Attacks")
    print_query("Ryan", "admin", "nothing' OR 'x'='x")
    print_query("Emily", "emily_user", "abc' OR 1=1--")
    print_query("Raquel", "raquel_22", "x' OR 'a'='a")

def test_union_query_attacks():
    print("Union Query Attacks")
    print_query("Ryan", "x' UNION SELECT * FROM admin_accounts--", "irrelevant")
    print_query("Emily", "x' UNION SELECT username, password FROM users--", "pass")
    print_query("Raquel", "x' UNION SELECT card_number, NULL FROMcredit_cards--", "x")

def test_additional_statement_attacks():
    print("Additional Statement Attacks")
    print_query("Ryan", "ryan", "x'; DROP TABLE users;--")
    print_query("Emily", "emily",  "x'; INSERT INTO users VALUES ('hacker','pw123');--")
    print_query("Raquel", "raquel", "x'; DELETE FROM users WHERE '1'='1';--")

def test_comment_attacks():
    print("Comment Attacks")
    print_query("Ryan", "admin' --", "doesnt_matter")
    print_query("Emily", "emily'#", "anything_here")
    print_query("Raquel", "raquel_22' --", "ignored")

# This will be the function that will mitigate the vulnerabilities in the create_query function
# but keep it weak!
# It goes against all 4 attacks Tautology Attacks, union query attacks, additional statement attacks, and comment attacks.
# We will test for the username and the password
def create_weak_sanitized_query(username, password):
    # some bad characters
    bad_characters = ["'", "--", ";", "/*", "*/", " DROP ", " UNION ", '"']

    sanitized_username = username
    sanitized_password = password

    for bad_char in bad_characters:
        sanitized_username = sanitized_username.replace(bad_char, "")
        sanitized_password = sanitized_password.replace(bad_char, "")

    return f"SELECT * FROM users WHERE username = '{sanitized_username}' AND password = '{sanitized_password}';"

# This will be the function that will mitigate the vulnerabilities in the create_query function
# But make it super strong!
# It goes against all 4 attacks Tautology Attacks, union query attacks, additional statement attacks, and comment attacks.
# We will test for the username and the password
def create_strong_sanitized_query(username, password):
    # Getting rid of all the things
    def allowthings(user_input):
        result = ""

        # This only allows letters, numbers, underscores, and hyphens
        for char in user_input:
            if ("a" <= char <= "z" or 
                "A" <= char <= "Z" or 
                "0" <= char <= "9" or
                char == "_" or char == "-"):
                result += char  
        return result
    
    sanitized_username = allowthings(username)
    sanitized_password = allowthings(password)

    return f"SELECT * FROM users WHERE username = '{sanitized_username}' AND password = '{sanitized_password}';"



# This is main function that will run everything
def main():
    # ── Valid Input ──────────────────────────────────────────
    VALID_TEST_CASES = [
    ("ryan_00001",   "pass_word1"), 
    ("Emily_mcgov",  "Secure_people2"),    
    ("raquel_22",   "myPass_2007"),    
    ]
    print("=" * 60)
    print("VALID INPUT TEST CASES")
    print("=" * 60)
    test_create_query_validation(VALID_TEST_CASES)

    # ── Vulnerability Demonstrations ─────────────────────────
    test_tautology_attacks()
    test_union_query_attacks()
    test_additional_statement_attacks()
    test_comment_attacks()

    # ── Weak Mitigation and strong ──────────────────────────────────────
    print(" ============ THIS IS THE WEAK AND STRONG SANITIZED QUERY TESTS ============")
    for user, passw in [
        ("chillydog", "password123"),
        ("pineapple123", "pw' UNION SELECT 'a','b'"),
        ("admin", "password123' OR '1'='1"),
        ("test", "DROP TABLE users; --"),
        ("testing24", "pw' --")
    ]:
        print(f"Testing with username: '{user}' and password: '{passw}'")
        print("Weak Sanitized Query:")
        print(create_weak_sanitized_query(user, passw))
        print("Strong Sanitized Query:") 
        print(create_strong_sanitized_query(user, passw))
        print()






if __name__ == "__main__":
    main()