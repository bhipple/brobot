import spotipy
import spotipy.util as util
# import urlparse
import oauth2 as oauth
import json


# sp = spotipy.Spotify()

# results = sp.search(q='weezer', limit='20')
# for i, t in enumerate(results['tracks']['items']):
    # print(' ', i, t['name'])


username = 'Chris.Hipple'
scope = 'user-library-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth = token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
