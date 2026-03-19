import requests

def fetch_market_news(sector: str):
    try:
        url = f"https://duckduckgo.com/?q={sector}+india+market+news&format=json"
        response = requests.get(url)
        return response.text[:1000]  # simple extraction
    except Exception as e:
        return f"Error fetching data: {str(e)}"