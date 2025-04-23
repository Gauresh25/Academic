import requests
from bs4 import BeautifulSoup
import time
import urllib.parse
import random
from datetime import datetime

# Rotate between different user agents
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
]


def get_random_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.google.com/',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }


def get_safety_news(location):
    try:
        encoded_location = urllib.parse.quote(location)

        search_queries = [
            f"{encoded_location} crime incident",
            f"{encoded_location} safety warning",
            f"{encoded_location} emergency alert",
            f"{encoded_location} weather warning",
            f"{encoded_location} security alert"
        ]

        all_articles = []

        print(f"\nFetching safety news for {location}...")
        print("-" * 80)

        for query in search_queries:
            print(f"\nSearching for: {query}")

            time.sleep(1)

            url = f"https://news.google.com/search?q={query}&hl=en-US&gl=US&ceid=US:en"

            response = requests.get(url, headers=get_random_headers(), timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Find articles using the correct class structure
            articles = soup.find_all('article', {'class': 'IFHyqb DeXSAc'})

            for article in articles:
                try:
                    # Find title link (class JtKRv contains the article title)
                    title_link = article.find('a', {'class': 'JtKRv'})
                    if not title_link:
                        continue

                    title = title_link.get_text(strip=True)

                    # Get the article URL
                    article_url = title_link.get('href', '')
                    if article_url.startswith('./'):
                        article_url = f"https://news.google.com{article_url[1:]}"

                    # Get source (class vr1PYe contains the source name)
                    source_elem = article.find('div', {'class': 'vr1PYe'})
                    source = source_elem.get_text(strip=True) if source_elem else 'Unknown'

                    # Get time (class hvbAAd contains the timestamp)
                    time_elem = article.find('time', {'class': 'hvbAAd'})
                    pub_time = time_elem.get('datetime') if time_elem else 'Recent'

                    # Get authors if available (class bInasb contains author information)
                    author_elem = article.find('div', {'class': 'bInasb'})
                    author = author_elem.get_text(strip=True) if author_elem else ''

                    article_data = {
                        'title': title,
                        'link': article_url,
                        'source': source,
                        'time': pub_time,
                        'author': author,
                        'query_category': query.split()[1]
                    }

                    # Only add if we haven't seen this title before
                    if not any(existing['title'] == title for existing in all_articles):
                        all_articles.append(article_data)

                        # Print article details immediately
                        print("\nArticle found:")
                        print(f"Title: {title}")
                        print(f"Source: {source}")
                        print(f"Time: {pub_time}")
                        if author:
                            print(f"Author: {author}")
                        print(f"Category: {article_data['query_category']}")
                        print(f"Link: {article_url}")
                        print("-" * 40)

                except Exception as e:
                    print(f"Error processing article: {str(e)}")
                    continue

        print(f"\nTotal articles found: {len(all_articles)}")
        return all_articles

    except requests.RequestException as e:
        print(f"Request error: {str(e)}")
        return []

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return []


if __name__ == '__main__':
    location = input("Enter location to search for safety news: ")
    get_safety_news(location)