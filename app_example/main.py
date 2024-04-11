"""
This program connects to Quotable API and uses setitem, getitem, and iter function.

1. Fetch quotes from the API
2. Allow accessing individual quotes by index
3. Permit modification of quotes at a specific index (only for local cache)
4. Enable iteration over all fetched quotes.
"""

import requests

class QuotableCollection:
    def __init__(self, tag=None):
        self.quotes = self.fetch_quotes(tag)

    def fetch_quotes(self, tag):
        """Fetch quotes from the Quotable API by tag"""
        url = "https://api.quotable.io/quotes"

        if tag:
            url += f"?tags={tag}"

        response = requests.get(url)
        
        return response.json()['results']
    
    def __getitem__(self, index):
        """Allows accessing a quote by index"""
        return f'"{self.quotes[index]["content"]}" ~{self.quotes[index]["author"]}'
    
    def __setitem__(self, index, value):
        """Allows setting a quote at a specific index."""
        # obj[index] = value
        self.quotes[index]['content'] = value

    def __iter__(self):
        return (quote['content'] for quote in self.quotes)



quotable_collection = QuotableCollection(tag="technology")

# for quote in quotable_collection.quotes:
#     print(quote)

print(quotable_collection[0])

print("Old quote:\n" + quotable_collection[3])
quotable_collection[3] = "AI WILL REPLACE US"

print("New quote:\n" + quotable_collection[3] )

for quote in quotable_collection:
    print(quote)