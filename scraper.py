import requests
from bs4 import BeautifulSoup
from config import MATCH_URL
import time

def scrape_fox_sports():
    try:
        res = requests.get(MATCH_URL, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        score_element = soup.select_one('.scoreboard__score')
        team_names = [e.text.strip() for e in soup.select('.scoreboard__team-name')]

        return {
            'teams': team_names,
            'score': score_element.text.strip() if score_element else 'N/A',
            'timestamp': time.time()
        }
    except Exception as e:
        return {'error': str(e)}
