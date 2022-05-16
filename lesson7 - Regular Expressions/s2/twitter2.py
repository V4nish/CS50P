url = input("What is the URL of your twitter profile: ").strip()

username = url.removeprefix("https://twitter.com/", "")   # What about http:// or just twitter.com/ or other parameters... Or even www.twitter.com/
print(f"Username: {username}")