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
test_cases = [
    ("ryan_00001",   "pass_word1"), 
    ("Emily_m",  "Secure_99"),    
    ("raquel_22",   "myPass_2007"),    
]

def test_create_query_validation(test_cases):
    print("=" * 60)
    print("VALID INPUT TEST CASES")
    print("=" * 60)
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
    print("Tautology Attacks")
    print("=" * 60)
    print("ATTACK INPUT TEST CASES")
    print("=" * 60)
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
    ... 

# This will be the function that will mitigate the vulnerabilities in the create_query function
# But make it super strong!
# It goes against all 4 attacks Tautology Attacks, union query attacks, additional statement attacks, and comment attacks.
# We will test for the username and the password
def create_strong_sanitized_query(username, password):
    ...

# This is main function that will run everything
def main():
    test_create_query_validation(test_cases)   
 
    test_tautology_attacks()
    test_union_query_attacks()  
    test_additional_statement_attacks()
    test_comment_attacks()

if __name__ == "__main__":
    main()