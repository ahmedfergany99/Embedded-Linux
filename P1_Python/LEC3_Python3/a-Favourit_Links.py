import webbrowser

favorite_websites = {
    "Facebook": "https://www.facebook.com/profile.php?id=100003665116036",
    "GitHub_repo": "https://github.com/ahmedfergany99/Embedded-Linux",
    "Linkedin": "https://www.linkedin.com/in/ahmed-fergany-7bb9291a1",
    "moatasem_elsayed_channel": "https://www.youtube.com/@moatasemelsayed6226",
}

print("Choose your favorite link by typing its name.")
print("Available links are:")
print(list(favorite_websites.keys()))

site_name = input("Enter the site name: ")

# Get the URL associated with the entered site name
site_url = favorite_websites.get(site_name)

if site_url:
    webbrowser.open(site_url)
    print(f"Opening {site_name}...")
else:
    print("Invalid site name. Please choose from the available links.")