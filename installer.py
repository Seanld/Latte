import requests

print("Downloading...")

request = requests.get("https://raw.githubusercontent.com/Seanld/Latte/dev/latte.py")
data = request.text

print("Installing...")

opened = open("stash_extensions/bin/latte.py", "w")
opened.write(data)
opened.close()

request.close()

print("Latte has been successfully installed!")
