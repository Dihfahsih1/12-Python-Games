url1 = "https://gmail.com"
url2 = "http://google.com"

if url1[4] == "s":
  slice = slice(8,-4)
else:
  slice = slice(7,-4)

print(url1[slice])
print(url2[slice])