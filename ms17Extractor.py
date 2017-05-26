import shodan
import subprocess
from termcolor import colored
import argparse
import shlex

parser = argparse.ArgumentParser()
parser.add_argument("-a", dest ="api_key", ,type=str ,help="Shodan API key")
parser.add_argument("-s", dest = "search_query", help="Search query")
parser.add_argument("-l", dest = "limit", default = 100, help="Search results' limit")

args = parser.parse_args()

api_key = args.api_key
SEARCH = args.search_query
LIMIT = args.limit

api = shodan.Shodan(api_key)
results = api.search(SEARCH, limit=LIMIT)['matches']
target_ips = []
victems_ips = []

for result in results: 
    target_ips.append(result['ip_str'])

for ip in target_ips:
    print(colored(' [*] %s '%ip, 'white'))
    cmd = 'nmap -sC -p445 --open --max-hostgroup 2 --script /usr/share/nmap/scripts/smb-vuln-ms17-010.nse %s' % ip
    cmd_list = shlex.split(cmd)
    try:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out, err = process.communicate()
        out = out.decode('utf-8')
        if "VULNERABLE" in out:
            victems_ips.append(ip)
            print(colored(' [+] Try To Hack!', 'green'))
    except Exception:
        print(colored(' [-] ERROR!', 'red'))

victems = open('victems_ips', 'w')
for ip in victems_ips:
    victems.write(ip)
    victems.write('\n')
