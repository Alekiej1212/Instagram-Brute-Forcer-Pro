import time
import random
from tqdm import tqdm
from colorama import Fore, Style

# Dummy list of target accounts (for demonstration)
targets = ["demo_user1", "demo_user2"]

# Dummy wordlist
passwords = ["123456", "password", "qwerty123", "letmein", "instagram1"]

print(Fore.CYAN + "Ultimate Instagram BruteForcer Lite v3.5.2" + Style.RESET_ALL)
print("Starting brute-force on demo accounts...")

for target in targets:
    print(f"\nTarget: {target}")
    for pwd in tqdm(passwords):
        time.sleep(0.5)
        success = random.choice([False, False, False, True])  # Simulated success rate
        if success:
            print(Fore.GREEN + f"[+] Password found for {target}: {pwd}" + Style.RESET_ALL)
            break
    else:
        print(Fore.RED + f"[-] No valid password found for {target}" + Style.RESET_ALL)

print("\nDemo completed. For full version, contact: @EliasK_SecTools")
