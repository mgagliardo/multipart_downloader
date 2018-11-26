import sys
from urllib.parse import urlparse

# Returns true/false if URL schema is valid, not checking if 2xx/3xx
def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False

print(is_url(sys.argv[1]))
