# Open the file in read mode
with open('add-link.txt', 'r') as file:
    # Read each line and strip any leading/trailing whitespace
    urls = [line.strip() for line in file]
print(urls)
# Print the list of URLs (optional)
# for url in urls:
#     print(url)
