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
VALID_TEST_CASES = [
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


#Testing 3 Tautology Attacks, 3 union query attacks, 3 additional statement attacks, and 3 comment attacks.
# Each member should come up with at least one of each type of attack
def test_tautology_attacks():
    ...

def test_union_query_attacks():
    ...

def test_additional_statement_attacks():
    ... 

def test_comment_attacks():
    ...

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
    # ── Valid Input ──────────────────────────────────────────
    test_create_query_validation(VALID_TEST_CASES)

    # ── Vulnerability Demonstrations ─────────────────────────
    test_tautology_attacks()
    test_union_query_attacks()
    test_additional_statement_attacks()
    test_comment_attacks()

    # ── Weak Mitigation ──────────────────────────────────────


    # ── Strong Mitigation ────────────────────────────────────


if __name__ == "__main__":
    main()