# port-scanner
A lightweight, not great port scanner built primarily to display/practice newly acquired skills in network pentesting and Python.


Line 45 specifies which ports to scan. Since this scanner is very simplistic, it is also slow, so I've defaulted it to ports 50-85 just to scan my home network. If you want ot use it to scan larger port ranges, just changes those numbers to the desired port range and it should do the job, albeit very slowly as each port will be scanned for about 1 second as specified on line 47.

Banner was created with https://manytools.org/hacker-tools/ascii-banner/

Syntax to run a scan:

```python3 scanner.py <ip>```
