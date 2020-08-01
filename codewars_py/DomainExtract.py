"""
Extract the domain name from a URL
git
Write a function that when given a URL as a string, 
parses out just the domain name and returns it as a string. 

For example:
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""
import re


def domain_name(url):
    # Get second group of regex match
    result = re.sub(r'(.*://w{3}\.|w{3}\.|.*://)?([^/?]+).*', '\g<2>', url)

    # Get domain before dot
    dotSplit = result.split(".")
    return dotSplit[0]
    
# Example
m = re.search(r'.*://w{3}\.|w{3}\.|.*://', 'http://www.codewars.com')
print("Test Example:", m.group(0))
