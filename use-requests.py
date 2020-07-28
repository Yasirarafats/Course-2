import requests

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'get success! Response = {response.status_code}')
        print(f'Content {response.text}')
    else:
        print(f'Ada kesalahan requests{response.status_code}')
except Exception as e:
    print(f'there is an error {e}')
print ('program ended')