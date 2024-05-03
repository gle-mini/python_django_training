import requests
import sys

def fetch_wikipedia_content(search_term, lang='en'):
    """ Fetches plain text content from Wikipedia based on the search term. """
    endpoint = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': search_term,
        'utf8': 1,
        'srlimit': 1
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    if 'query' in data and 'search' in data['query'] and data['query']['search']:
        page_id = data['query']['search'][0]['pageid']
        params = {
            'action': 'query',
            'prop': 'extracts',
            'exintro': True,
            'explaintext': True,
            'pageids': page_id,
            'format': 'json'
        }
        response = requests.get(endpoint, params=params)
        data = response.json()

        return data['query']['pages'][str(page_id)]['extract']

    return None

def write_to_file(content, filename):
    """ Writes content to a file. """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    if len(sys.argv) < 2:
        print("Error: No search term provided.")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Error: You can search only one term.")
    search_term = sys.argv[1]
    filename = f"{search_term.replace(' ', '_')}.wiki"

    content = fetch_wikipedia_content(search_term)
    if content:
        write_to_file(content, filename)
    else:
        print("Error: No results found for the search term.")

if __name__ == "__main__":
    main()

