import requests
import re

url = input("Enter website URL (e.g., example.com): ")
if not url.startswith('http'):
    url = 'https://' + url

try:
    response = requests.get(url, timeout=5)
    content = response.text
    print(f"\n[+] Scanning {url}\n")
except:
    print("[-] Failed to connect")
    exit()

# Extract emails
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
emails = list(set(emails))

# Extract phone numbers
phones = re.findall(r'(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})', content)
phones = list(set(phones))

print(f"[*] Emails found: {len(emails)}")
for email in emails:
    print(f"    {email}")

print(f"\n[*] Phone numbers found: {len(phones)}")
for phone in phones:
    print(f"    {phone}")

print("\n[+] Scan complete!")