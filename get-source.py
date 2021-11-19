import requests

for id in range(799931, 799932):
    url = 'https://zinro.net/m/log.php?id='+str(id)
    filename = 'log-'+str(id)+".txt"

    urlData = requests.get(url).content

    with open(filename, mode='wb') as f:  # wb でバイト型を書き込める
        f.write(urlData)
