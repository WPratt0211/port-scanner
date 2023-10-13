# Port Scanner

**Port Scanner** is a lightweight, simple port scanner built for educational and practice purposes in the field of network penetration testing. It is implemented in Python and is designed to help display and reinforce newly acquired skills in network security.

## Usage

### Prerequisites

Before using the Port Scanner, make sure you have Python 3.x installed on your system.

### Scanning Ports

- Line 45 of the code specifies the ports to be scanned. Please note that this scanner is relatively simplistic and may not be suitable for high-speed or extensive port scanning.

- The default setting scans ports 50 to 85. If you wish to scan a different port range, you can modify the numbers in the code to match your requirements. Keep in mind that the scanner is intentionally slow, with each port being scanned for approximately 1 second, as specified in line 47.

### Running a Scan

To run a scan, use the following syntax:

```
python3 scanner.py <ip_address>
```

Replace `<ip_address>` with the target IP address you want to scan.

## Acknowledgments

- The ASCII art banner used in this project was generated with [ManyTools](https://manytools.org/hacker-tools/ascii-banner/).

---

**Please note that this port scanner should be used responsibly and only on systems and networks where you have explicit permission to scan. Unauthorized scanning can violate legal and ethical standards.**
