import pandas as pd
import sys

def convert_csv_to_tls(csv_filename, output_filename):
    df = pd.read_csv(csv_filename, encoding='utf-8')
    ips = df.iloc[:, 0]
    download_speeds = df.iloc[:, 5]

    with open(output_filename, 'w', encoding='utf-8') as f:
        for i, (ip, speed) in enumerate(zip(ips, download_speeds)):
            f.write(f"{ip}#香港优选IP {i+1}  ↓ {speed}MB/s\n")

csv_filename = 'result.csv'
output_filename = 'HK.txt'
convert_csv_to_tls(csv_filename, output_filename)