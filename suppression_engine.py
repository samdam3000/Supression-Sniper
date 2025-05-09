from scraper import scrape_fox_sports
import time

def evaluate_trigger():
    data = scrape_fox_sports()
    # Placeholder logic: always fire for demo
    trigger_fired = True
    confidence = 36.2
    reason = "Suppression lifted: ineffective tackle + fast PTB"
    in_game_time = time.strftime('%M:%S', time.gmtime(time.time() % 3600))
    return {
        'trigger': trigger_fired,
        'confidence': f"{confidence:.1f}%",
        'time': in_game_time,
        'reason': reason
    }
