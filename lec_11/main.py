import requests

# to make GET, POST, PUT, DELETE calls
get_response = requests.get("https://jsonplaceholder.typicode.com/posts")
post_response = requests.post("https://jsonplaceholder.typicode.com/posts")
put_response = requests.put("https://jsonplaceholder.typicode.com/posts/1")
delete_response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

filteredByTitle = []
filteredByBody = []

# filter out GET calls results
for data in get_response.json():
    # filter out titles that contains more than 6 words
    # split() breaks a string into a list of substrings on a whitespace seperator
    if len(data['title'].split()) > 6:
        filteredByTitle.append(data)
    # filter out body that contains more than 3 lines of description
    # splitlines() seperates a string into list of lines based on linebreaks
    if len(data['body'].splitlines()) > 3:
        filteredByBody.append(data)