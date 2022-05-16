url = input("What is the URL of your twitter profile: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")