# ${1:ms17-010 Shodan Extractor}
Simple script to extract machines which are infected with ms17-010 vulnerability. However there are many alarms asking to patch machines, you will find alot of infected ones.

# Pre-requests:
You should have an upgrade shodan API_KYE. You can get one from their web site.

# Usage: 
```python
python3 shodanExtractor.py -a <you_api_key> -s "port:445 os:'7'" -l 100
```

# Disclaimer:
This is for Educational purposes ONLY. First of all, this code aims to alarm people about security issues infected unpatched machines.

