import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
import pandas as pd
import time
from dotenv import load_dotenv


class SpotifyClient(object):
    def __init__(self, genre='Pop'):
        self.genre = genre
        self.authenticate()
        self.get_genre_artist()
        self.create_artist_df()

    def authenticate(self):
        load_dotenv()
        client_id = os.getenv('client_id')
        client_secret = os.getenv('client_secret')
        client_credentials_manager = SpotifyClientCredentials(
            client_id=client_id, client_secret=client_secret)
        self.sp = spotipy.Spotify(
            client_credentials_manager=client_credentials_manager)

    def get_genre_artist(self):

        os.makedirs('genre_artist', exist_ok=True)
        genre_artist = []

        for i in range(0, 1000, 50):
            genre_artist_search = self.sp.search(q='genre:' + self.genre,
                                                 limit=50,
                                                 type='artist',
                                                 offset=i)['artists']['items']
            genre_artist.extend(genre_artist_search)

        with open('./genre_artist/{}_artists.json'.format(self.genre),
                  'w') as f:
            json.dump(genre_artist, f)

    def create_artist_df(self):
        with open('./genre_artist/{}_artists.json'.format(self.genre),
                  'r') as f:
            artists = json.load(f)

        artist_list = []
        for artist in artists:
            artist_list.append([
                artist['name'], artist['id'], artist['popularity'],
                artist['followers']['total']
            ])

        self.artist_df = pd.DataFrame(artist_list,
                                      columns=[
                                          'artist_name', 'artist_id',
                                          'artist_popularity',
                                          'artist_followers'
                                      ])
        self.artist_id_list = self.artist_df['artist_id'].to_list()

    def get_artist_album(self):
        os.makedirs('artist_album', exist_ok=True)

        for artist_id in self.artist_id_list:
            artist_album = []
            for i in range(0, 1000, 50):
                artist_album_search = self.sp.artist_albums(artist_id,
                                                            limit=50,
                                                            offset=i)['items']
                artist_album.extend(artist_album_search)
                time.sleep(3)
            with open('./artist_album/{}_albums.json'.format(artist_id),
                      'w') as f:
                json.dump(artist_album, f)

    def create_album_df(self):
        album_list = []
        for file in os.listdir('./artist_album/'):
            artist_id = file.split('_')[0]

            with open(f'./artist_album/{file}', 'r') as f:
                artist_album = json.load(f)

            for album in artist_album:
                if album['artists'][0]['id'] == artist_id and album[
                        'album_type'] != 'compilation':
                    album_list.append([
                        artist_id, album['id'], album['release_date'],
                        album['album_type']
                    ])
        self.album_df = pd.DataFrame(album_list,
                                     columns=[
                                         'artist_id', 'album_id',
                                         'album_release_date', 'album_type'
                                     ])
        self.album_id_list = self.album_df['album_id'].drop_duplicates(
        ).to_list()

    def get_album_track(self):
        os.makedirs('artist_track', exist_ok=True)

        for artist_id in self.artist_id_list:
            album_sublist = self.album_df[self.album_df['artist_id'] ==
                                          artist_id]['album_id'].to_list()
            album_number = len(album_sublist)
            album_track = []
            for i in range(0, album_number, 20):
                track_search = self.sp.albums(album_sublist[i:i + 20])
                album_track.extend(track_search['albums'])
                time.sleep(5)
            with open('./artist_track/{}_tracks.json'.format(artist_id),
                      'w') as f:
                json.dump(album_track, f)

    def create_track_df(self):
        track_list = []

        for file in os.listdir('./artist_track/'):
            artist_id = file.split('_')[0]
            with open(f'./artist_track/{file}', 'r') as f:
                album_track = json.load(f)

            for album in album_track:
                album_id = album['id']
                album_name = album['name']
                album_popularity = album['popularity']
                album_release_date = album['release_date']

                for track in album['tracks']['items']:
                    track_id = track['id']
                    track_name = track['name']
                    track_duration = track['duration_ms']
                    track_list.append([
                        artist_id, album_id, album_name, album_popularity,
                        album_release_date, track_id, track_name,
                        track_duration
                    ])

        track_df = pd.DataFrame(track_list,
                                columns=[
                                    'artist_id', 'album_id', 'album_name',
                                    'album_popularity', 'album_release_date',
                                    'track_id', 'track_name',
                                    'track_duration(ms)'
                                ])
        self.track_df = track_df[track_df['album_id'].isin(self.album_id_list)]

    def get_track_analysis(self):
        os.makedirs('track_analysis', exist_ok=True)
        for artist_id in self.artist_id_list:
            track_sublist = self.track_df[
                self.track_df['artist_id'] ==
                artist_id]['track_id'].drop_duplicates().to_list()
            track_number = len(track_sublist)
            track_analysis = []
            for i in range(0, track_number, 100):
                track_analysis_search = self.sp.audio_features(
                    track_sublist[i:i + 100])
                track_analysis.extend(track_analysis_search)
                time.sleep(5)
            with open(
                    './track_analysis/{}_track-analysis.json'.format(
                        artist_id), 'w') as f:
                json.dump(track_analysis, f)

    def create_analysis_df(self):
        analysis_list = []

        for file in os.listdir('./track_analysis/'):
            with open(f'./track_analysis/{file}', 'r') as f:
                track_analysis = json.load(f)
                analysis_list.extend(track_analysis)
        self.analysis_df = pd.DataFrame(
            [x for x in analysis_list if x is not None]).drop_duplicates('id')
