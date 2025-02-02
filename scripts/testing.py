import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

# API Key for Google Places API
API_KEY = os.getenv("PLACES_API")

# Coventry city center coordinates and radius
LOCATION = "52.406822,-1.519693"
RADIUS = 10000  # 10 km radius

# List of major UK retailers
RETAILERS = [
    "Tesco",
    "Asda",
    "Sainsbury's",
    "Morrisons",
    "Aldi",
    "Lidl",
    "Iceland",
    "Co-op Food",
    "M&S Simply Food"
]

PLACES_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

def fetch_stores(search_query):
    """Fetch stores for a specific retailer"""
    stores = []
    next_page_token = None
    
    while True:
        params = {
            "query": f"{search_query} Coventry",
            "location": LOCATION,
            "radius": RADIUS,
            "key": API_KEY,
        }
        
        if next_page_token:
            params["pagetoken"] = next_page_token
            time.sleep(2)  # Google requires delay between page token requests

        response = requests.get(PLACES_URL, params=params)
        if response.status_code != 200:
            print(f"Error fetching {search_query}: HTTP {response.status_code}")
            break

        data = response.json()
        if data["status"] != "OK":
            print(f"API Error for {search_query}: {data['status']}")
            break

        stores.extend(data.get("results", []))
        next_page_token = data.get("next_page_token")

        if not next_page_token:
            break

    return stores

# Collect data for all retailers
all_stores = []
for retailer in RETAILERS:
    print(f"Fetching {retailer}...")
    results = fetch_stores(retailer)
    all_stores.extend(results)
    time.sleep(1)  # Be kind to API rate limits

# Process and deduplicate results
store_data = []
seen_ids = set()  # To avoid duplicates

for store in all_stores:
    place_id = store.get("place_id")
    if place_id in seen_ids:
        continue
        
    seen_ids.add(place_id)
    
    store_data.append({
        "Name": store.get("name"),
        "Address": store.get("formatted_address"),
        "Latitude": store["geometry"]["location"]["lat"],
        "Longitude": store["geometry"]["location"]["lng"],
        "Rating": store.get("rating"),
        "User_Ratings_Total": store.get("user_ratings_total"),
        "Business_Status": store.get("business_status"),
        "Types": ", ".join(store.get("types", [])),
        "Place_ID": place_id,
        "Price_Level": store.get("price_level"),
    })

# DataFrame for next steps
df = pd.DataFrame(store_data)

print(df.head(5))
