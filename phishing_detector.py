
import re

SUSPICIOUS_WORDS = [
    "urgent",
    "verify your account",
    "click here",
    "password",
    "account suspended",
    "prize",
    "claim now",
    "confirm your details",
    "login immediately"
]

def analyze_email(email_text):
    findings = []

    text = email_text.lower()

    # Check for suspicious phrases
    for word in SUSPICIOUS_WORDS:
        if word in text:
            findings.append(f"Suspicious phrase found: {word}")

    # Check for URLs in the email
    urls = re.findall(r"https?://\S+|www\.\S+", email_text)

    if urls:
        findings.append(f"Contains {len(urls)} link(s). Verify them carefully.")

    # Display results
    print("\n--- Phishing Email Analysis ---")

    if findings:
        print("Warning: Suspicious indicators detected!\n")
        for finding in findings:
            print("-", finding)
    else:
        print("No common phishing indicators detected.")

    print("\nNote: This basic tool cannot confirm whether an email")
    print("is safe or malicious. Verify suspicious emails independently.")


def main():
    print("=== Phishing Email Detection Tool ===")
    print("Paste the email text below.")
    email_text = input("\nEmail text: ")

    if not email_text.strip():
        print("Please enter some email text.")
        return

    analyze_email(email_text)


if __name__ == "__main__":
    main()
