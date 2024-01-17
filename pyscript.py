import requests
import pandas as pd
from multiprocessing import Pool
from tqdm import tqdm

def get_spotify_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_data = auth_response.json()
    return auth_data['access_token']

def search_track(track_name, artist_name, token):
    query = f"{track_name} artist:{artist_name}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track"
    response = requests.get(url, headers={
        'Authorization': f'Bearer {token}'
    })
    json_data = response.json()
    try:
        first_result = json_data['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except (KeyError, IndexError):
        return None

def get_track_details(track_id, token):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    response = requests.get(url, headers={
        'Authorization': f'Bearer {token}'
    })
    json_data = response.json()
    try:
        album_data = json_data['album']
        images = album_data.get('images', [])
        if images:
            image_url = images[0]['url']
            return image_url
        else:
            print(f"No images found for track_id {track_id}")
            return None
    except KeyError:
        print(f"Unexpected JSON structure for track_id {track_id}: {json_data}")
        return None

def process_chunk(args):
    chunk, access_token = args
    processed_rows = []
    for i, row in tqdm(chunk.iterrows(), total=len(chunk), desc="Processing chunk"):
        track_id = search_track(row['track_name'], row['artist_name'], access_token)
        if track_id:
            image_url = get_track_details(track_id, access_token)
            processed_rows.append((i, image_url))
        else:
            print(f"No track found for {row['track_name']} - {row['artist_name']}")
    return processed_rows

if __name__ == '__main__':
    # Define client_id and client_secret before calling get_spotify_token
    client_id = '31971df0ef2c46eaa222c0313b838445'
    client_secret = '0c221685a9e64352b24762606cdec4bf'

    access_token = get_spotify_token(client_id, client_secret)

    # Assuming you have a CSV file named 'spotify-2023.csv'
    df_spotify = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

    # Print column names
    print(df_spotify.columns)

    # Define the number of processes (adjust as needed)
    num_processes = 4

    # Split DataFrame into chunks
    chunks = [(df_spotify.iloc[i:i + len(df_spotify)//num_processes], access_token) for i in range(0, len(df_spotify), len(df_spotify)//num_processes)]

    # Process chunks in parallel
    with Pool(processes=num_processes) as pool:
        results = list(tqdm(pool.imap_unordered(process_chunk, chunks), total=num_processes, desc="Processing chunks"))

    # Flatten the results list
    processed_rows = [item for sublist in results for item in sublist]

    # Update DataFrame with results
    for idx, result in processed_rows:
        df_spotify.at[idx, 'image_url'] = result

    # Save the updated DataFrame to a new CSV file
    df_spotify.to_csv('updated_file.csv', index=False)
