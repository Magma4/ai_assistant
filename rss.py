import feedparser as fp

feed_url = "https://www.worldbank.org/en/search?q=grants+fundings"
feed = fp.parse(feed_url)
feed_title = feed.feed.title
feed_description = feed.feed.description

grants = []

for entry in feed.entries:
    item_title = entry.title
    item_description = entry.description
    item_published = entry.published

    # Check if the item is a grant
    if 'grant' in item_title.lower() or 'grant' in item_description.lower():
        grant = {
            'title': item_title,
            'description': item_description,
            'published': item_published
        }
        grants.append(grant)

# Print the identified grants
for grant in grants:
    print("Grant Title:", grant['title'])
    print("Grant Description:", grant['description'])
    print("Published:", grant['published'])
    print()