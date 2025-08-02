import re

common_passwords = [
    "123456", "password", "12345678", "qwerty", "abc123", "letmein",
    "admin", "welcome", "monkey", "login"
]

def check_password_strength(password):
    score = 0
    feedback = []
    if len(password) >= 12:
        score += 1
        feedback.append("[+] Length: OK")
    else:
        feedback.append("[!] Length too short (min 12 characters)")
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("[+] Contains uppercase: OK")
    else:
        feedback.append("[!] Missing uppercase letters")
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("[+] Contains lowercase: OK")
    else:
        feedback.append("[!] Missing lowercase letters")
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("[+] Contains digits: OK")
    else:
        feedback.append("[!] Missing digits")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("[+] Contains symbols: OK")
    else:
        feedback.append("[!] Missing symbols")
    if password.lower() in common_passwords:
        feedback.append("[!] This password is commonly used!")
        score -= 1
    if score >= 5:
        strength = "STRONG"
    elif score >= 3:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return feedback, strength
if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    user_input = input("Enter your password: ")
    results, final_strength = check_password_strength(user_input)

    print("\n--- Analysis ---")
    for line in results:
        print(line)
    print(f"\n🔎 Password strength: {final_strength}")
