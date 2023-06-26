import os
import asyncio
import googleapiclient.discovery
from google.oauth2 import service_account
import aiohttp
from bs4 import BeautifulSoup

# Set up YouTube Data API credentials
API_KEY = 'YOUR_API_KEY'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# Function to scrape subscriber count using SocialBlade asynchronously
async def scrape_subscriber_count(session, channel_url):
    socialblade_url = f"https://socialblade.com/youtube/channel/{channel_url}"
    async with session.get(socialblade_url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        subscriber_count = soup.select_one('#youtube-stats-header-sb > span').text.strip()
        return subscriber_count

# Function to determine niche using ChatGPT
def determine_niche(prompt):
    # Implement your ChatGPT code here or call an external API/service to generate niche based on prompt
    niche = 'Example Niche'  # Replace with your actual niche generation logic
    return niche

# Initialize YouTube Data API client
credentials = service_account.Credentials.from_service_account_file(
    'PATH_TO_YOUR_SERVICE_ACCOUNT_JSON_FILE',
    scopes=['https://www.googleapis.com/auth/youtube.readonly']
)
youtube = googleapiclient.discovery.build(
    API_SERVICE_NAME, API_VERSION, credentials=credentials, cache_discovery=False
)

# Retrieve YouTube channels with 1 million or more subscribers
channels_list = []
next_page_token = None

while True:
    channels = youtube.search().list(
        part='snippet',
        type='channel',
        order='subscriberCount',
        maxResults=50,
        q='',
        pageToken=next_page_token
    ).execute()

    channels_list.extend(channels['items'])
    next_page_token = channels.get('nextPageToken')

    if not next_page_token:
        break

# Scrape subscriber count and determine niche for each channel asynchronously
async def process_channel(session, channel):
    channel_id = channel['id']['channelId']
    channel_url = f'https://www.youtube.com/channel/{channel_id}'
    subscriber_count = await scrape_subscriber_count(session, channel_url)
    niche = determine_niche(channel['snippet']['title'])

    return {
        'channel_id': channel_id,
        'subscriber_count': subscriber_count,
        'niche': niche
    }

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for channel in channels_list:
            tasks.append(process_channel(session, channel))
        
        results = await asyncio.gather(*tasks)

    # Print the results
    for result in results:
        print(f"Channel ID: {result['channel_id']}")
        print(f"Subscriber Count: {result['subscriber_count']}")
        print(f"Niche: {result['niche']}")
        print('-' * 50)

# Run the main function asynchronously
asyncio.run(main())
