import sys
import requests
from bs4 import BeautifulSoup


class RoadsToPhilosophy:
    def __init__(self) -> None:
        self.visited_titles = []

    def search_wikipedia(self, path: str) -> None:
        url = f'https://en.wikipedia.org{path}'
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.HTTPError as e:
            print(f"Error accessing {url}: {e}")
            if response.status_code == 404:
                print("It's a dead end!")
            return
        except requests.RequestException as e:
            print(f"Network error: {e}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find(id='firstHeading').text
        print(title)

        if title in self.visited_titles:
            print("It leads to an infinite loop!")
            return
        self.visited_titles.append(title)

        if title == 'Philosophy':
            print(f"{len(self.visited_titles)} roads from {self.visited_titles[0]} to Philosophy")
            return

        content = soup.find(id='mw-content-text')
        links = content.select('p > a[href^="/wiki/"]:not([href*=":"])')

        for link in links:
            return self.search_wikipedia(link['href'])

        print("It leads to a dead end!")

def main():
    if len(sys.argv) != 2:
        print('Usage: python roads_to_philosophy.py <title>')
        return

    wiki = RoadsToPhilosophy()
    wiki.search_wikipedia(f'/wiki/{sys.argv[1]}')


if __name__ == '__main__':
    main()

