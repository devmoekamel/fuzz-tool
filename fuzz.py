import requests
import argparse

from concurrent.futures import ThreadPoolExecutor

def check_url(word):
    global counter  # Use global counter variable

    try:
        req = requests.head(url + "/" + word[:-1])
        if req.status_code not in filter_list:
            print(f"/{word[:-1]}            Status Code: {req.status_code}")
    except Exception as e:
        print(f"Error: {e}")

    # Print progress after each request
    print(f":: Progress: [{counter}/{len(lines)}] ::", end="\r")
    counter += 1




parser = argparse.ArgumentParser(description="FUZZing Tool")

parser.add_argument("-u", "--url", help="Specify the URL", required=True)
parser.add_argument("-fc", "--filter_code", help="Filter output with your list of status code", required=False)
parser.add_argument("-mc", "--matching_code", help="match output with list of status code", required=False)
parser.add_argument("-w", "--wordlist", help="Specify the Wordlist File", required=True)

args = parser.parse_args()

url = args.url
file_path = args.wordlist
filter= args.filter_code

file = open(file_path, 'r')
lines = file.readlines()
filter_list= [404]
matching_list=[]
counter = 1

with ThreadPoolExecutor() as executor:
    executor.map(check_url, lines)



