import subprocess, datetime
time_start = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

# speedtest-cli -f csv
csv_line = subprocess.run(["./speedtest", "-f", "csv"], stdout=subprocess.PIPE).stdout
csv_line = csv_line.decode('utf-8', 'ignore')

time_stop = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')

modified = "\"" + time_start + "\",\"" + time_stop + "\"," + csv_line
print(modified, end='')