import re
from collections import Counter
from datetime import datetime

def analyze_log(file_name):
  ip_pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
  time_pattern = r'\[(.*?\]'
  status_pattern = r'"\s(\d{3})\s'

  ip_counter = Counter()
  hourly_counter = Counter()
  status_counter = Counter()

  with open(file_name, 'r') as file:
    for line in file:
      ip_match = re.search(ip_pattern, line)
      time_match = re.search(time_pattern, line)
      status_match = re.search(status_pattern, line)

      if ip_match:
        ip = ip_match.group(1)
        ip_counter[ip] += 1

      if time_match:
        time_str = time_match.group(0)[1:-1]
        time_obj = datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S %z')
        hour_key = time_obj.strftime('%Y-%m-%d %H')
        hourly_counter[hour_key] += 1

      if status_match:
        status_code = status_match.group(1)
        status_counter[status_code] += 1

## ip 별 접속 횟수 Top 10
  print("Top 10 IPs:")

  for ip, count in ip_counter.most_common(10):
    print(f"{ip}: {count} 회")

  for hour, count in hourly_counter.items():
    print(f"{hour}: {count} 회")

  for status_code, count in status_counter.items():
    print(f"Status {status_code}: {count} 회")