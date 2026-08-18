# Scanner Automation Tool 🛠️
A simple automation tool built with Python for Termux to run Nmap and Whois scans easily with a nice UI.

## Features ✨
- Nmap scanner integration.
- Whois lookup integration.
- Automated requirements installer (`pkg`).
- Beautiful terminal UI with custom colors and progress bars.

## How to Install and Run on Termux 📱
```bash
pkg update && pkg upgrade
pkg install git python
git clone [https://github.com/belal-the-eagle/scanner-automation.git](https://github.com/belal-the-eagle/scanner-automation.git)
cd scanner-automation
pip install pyfiglet
pip install colorama
pip install alive_progress
python scanner.py
