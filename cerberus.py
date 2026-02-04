import sys
import platform
import socket

def check_identity():
    # 1. Check the CPU Architecture
    # On your Mac VM, this should be 'aarch64'
    arch = platform.machine()
    print(f"[INFO] CPU Architecture: {arch}")
    
    if "aarch64" not in arch and "arm64" not in arch:
        print("[WARN] Architecture mismatch! Expected ARM64.")
        return False
    return True

def check_internet():
    # 2. Check Connectivity
    # Try to connect to Google DNS (8.8.8.8) on port 53
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        print("[PASS] Internet Connection: ACTIVE")
        return True
    except OSError:
        print("[FAIL] Internet Connection: DOWN")
        return False

def check_sandbox():
    # 3. Check if we are inside the Virtual Environment
    # Sys.prefix tells us where Python is running from. 
    # If we are in venv, it should not equal the base system prefix.
    if sys.prefix == sys.base_prefix:
        print("[FAIL] SANDBOX NOT ACTIVE! Run 'source venv/bin/activate' first.")
        return check_sandbox
    
    print(f"[PASS] Sandbox Active: {sys.prefix}")
    return True

def main():
    print("--- CERBERUS PRE-FLIGHT CHECK ---")
    
    # We run the checks. If ANY fail, we stop.
    if not check_identity():
        print("Identity Check Failed.")
    elif not check_internet():
        print("Network Check Failed.")
    elif not check_sandbox():
        print("Environment Check Failed.")
    else:
        print("--- ALL SYSTEMS GO. READY FOR LAUNCH. ---")

if __name__ == "__main__":
    main()