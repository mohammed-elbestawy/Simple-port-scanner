# Simple Port Scanner

> A lightweight multithreaded TCP port scanner written in Python. Built as a learning project to understand how tools like Nmap work under the hood — raw socket connections, not a wrapper around another scanner.

---

## Features

- Resolves hostnames to IP addresses automatically
- Configurable port range (defaults to 1–1024 if not specified)
- Multithreaded scanning (up to 100 concurrent threads) for fast results
- Clean error handling — invalid input, unresolvable hosts, and `Ctrl+C` are all handled gracefully

---

## Usage

```bash
# Scan the default range (ports 1-1024)
python3 scanner.py <target>

# Scan a custom port range
python3 scanner.py <target> <start_port> <end_port>
```

### Examples

```bash
python3 scanner.py 192.168.1.10
python3 scanner.py scanme.nmap.org 1 1000
```

### Sample Output

```
--------------------------------------------------
Scanning target: 192.168.1.10 (192.168.1.10)
Port range: 1-1000
Time started: 2026-07-03 22:10:04.123456
--------------------------------------------------
[+] Port 22 is open
[+] Port 80 is open
[+] Port 443 is open
--------------------------------------------------
Scan completed at: 2026-07-03 22:10:06.789012
Open ports found: [22, 80, 443]
--------------------------------------------------
```

---

## How It Works

The scanner attempts a TCP connection to each port in the specified range using Python's `socket` module. A successful connection (`connect_ex()` returning `0`) means the port is open. Ports are scanned concurrently using `ThreadPoolExecutor`, which is significantly faster than scanning sequentially — especially over larger port ranges.

---

## Requirements

- Python 3.6+
- No external dependencies — uses only the Python standard library

---

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Only scan systems you own or have explicit written permission to test. Unauthorized port scanning may be illegal depending on your jurisdiction.
