#!/usr/bin/env python3
"""
Simple TCP Port Scanner
Usage: python3 scanner.py <target> [start_port] [end_port]
Example: python3 scanner.py 192.168.1.10 1 1000
"""

import sys
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024
TIMEOUT = 1
MAX_THREADS = 100


def resolve_target(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        print(f"[!] Hostname could not be resolved: {hostname}")
        sys.exit(1)


def scan_port(target, port):
    """Attempt to connect to a single port. Returns the port number if open, else None."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(TIMEOUT)
            result = s.connect_ex((target, port))
            if result == 0:
                return port
    except socket.error:
        pass
    return None


def main():
    if len(sys.argv) < 2:
        print("[!] Invalid number of arguments")
        print("    Syntax: python3 scanner.py <target> [start_port] [end_port]")
        sys.exit(1)

    target_input = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_START_PORT
    end_port = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_END_PORT

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("[!] Invalid port range. Must be between 1 and 65535, start <= end.")
        sys.exit(1)

    target = resolve_target(target_input)

    print("-" * 50)
    print(f"Scanning target: {target_input} ({target})")
    print(f"Port range: {start_port}-{end_port}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)

    open_ports = []

    try:
        with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            futures = {
                executor.submit(scan_port, target, port): port
                for port in range(start_port, end_port + 1)
            }
            for future in as_completed(futures):
                port = future.result()
                if port is not None:
                    open_ports.append(port)
                    print(f"[+] Port {port} is open")

    except KeyboardInterrupt:
        print("\n[!] Exiting program")
        sys.exit(1)

    print("-" * 50)
    print(f"Scan completed at: {datetime.now()}")
    print(f"Open ports found: {sorted(open_ports) if open_ports else 'None'}")
    print("-" * 50)


if __name__ == "__main__":
    main()
