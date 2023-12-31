# Motivation
In 2021, the global music industry experienced its fastest growth rate in over two decades, with a total revenue of $25.9 billion, representing an impressive 18.5% increase. Pop music played a significant role in driving this revenue, thanks to artists such as Taylor Swift, Ed Sheeran, and Justin Bieber. The surge in music sales was primarily fueled by the streaming segment, which witnessed a considerable rise in the number of paying subscribers. Notably, the number of paid subscribers reached 523 million in 2021, a substantial increase from the 443 million recorded in 2020.<br />

These remarkable trends have caught my attention, leading me to conduct data analysis using the valuable data provided by the Spotify API. Through this analysis, I aim to explore intriguing questions such as:<br />

1. Who are the most influential artists within the pop music genre?<br />
2. How has the pop music market evolved in terms of its market size and audio features?<br />
3. Is there a correlation between the development of audio features and the state of the US economy?<br />

# Folders and Files
* **genre_artist**: The folder is created to store information about the pertinent artists within a specific music genre.
* **artist_album**: The folder is created to store information about the albums by artists.
* **artist_track**: The folder is created to store information about the tracks by artists.
* **track_analysis**: The folder is created to store information about the analysis conducted on the tracks.
* **spotifyapp.py**: This file includes the relevant class and functions required to download and manage all the aforementioned data.
* **evaluation.ipynb**: Data analysis and visualization based on the provided data.

# Data Analysis and Viasualization
In general, the data analysis is conducted on a dataset that includes 970 artists, 33,200 albums, and 167,203 tracks.
## Most Influential Artists

Two measures of prevalence in Spotify:

* **Followers**: The number of people following the artist.
* **Popularity**: The Spotify popularity index is a number from 0-100 and comes directly from Spotify. 100 meaning the highest possible level of popularity attainable on Spotify.

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/3e9642cf-62c7-494a-b494-325c06185861)

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/f62e20c5-4a18-4385-868f-300e7a95f05c)

Taking into account the follower count and popularity data provided by Spotify, the following artists are deemed to be highly influential within the pop music genre. They have secured a position in both the "Top 20 Artists with the Most Popularity" and the "Top 20 Artists with the Most Followers" lists:

1. Taylor Swift
2. The Weeknd
3. Drake
4. BTS
5. Ed Sheeran
6. Justin Bieber
7. Rihanna
8. Bruno Mars
9. Post Malone
10. Coldplay
11. Ariana Grande
12. Dua Lipa
13. Imagine Dragons

These artists have proven their significance and impact on the music industry, consistently garnering a vast number of followers and maintaining high levels of popularity.

## Evolution of Market Size
The evolution of market size is analyzed in terms of the number of albums and tracks released, both on a yearly and monthly basis. It is important to clarify that this analysis encompasses both albums and singles, which are collectively considered within the 'album' category for the purpose of this study.

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/8196be97-9087-4c84-b1b0-7c9fc2fd62b9)

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/5e97d2db-7b09-494e-82e1-82407322cdba)

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/8b99cd9a-e4cf-4b94-a809-3f252b60f31b)

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/abb26c99-43a7-4581-8dc8-16721ad62415)

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/92648306-06e5-4bcc-8241-53616ad47baf)

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/0b0e0cc4-162d-45ed-bf4f-728087701e82)

Upon observation, it is evident that there is a noteworthy parallel between the trends in the number of released albums and tracks. Both exhibit an upward trajectory over the years, with artists displaying particularly heightened levels of activity during the month of January. Analyzing the distribution of releases by year and month, the pronounced surge during the month of January persists until approximately 2013 or 2014, after which the activity becomes more evenly spread across different months.

## Evolution of Audio Features

Audio Features
This project examines 11 music attributes provided by Spotify. Here is the explanation from Spotify's document.

* **Acousticness**: a confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
* **Danceability**: it describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* **Energy**: it is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
* **Instrumentalness**: it predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
* **Liveness**: it detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
* **Loudness**: the overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
* **Speechiness**: it detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
* **Valence**: a measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
* **Tempo**: the overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
* **Duration_ms**: the duration of the track in milliseconds.
* **Key**: the key the track is in. Integers map to pitches using standard Pitch Class notation.

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/135afeaa-2003-4026-a983-5b596b8a03aa)

It is clear that certain audio features, including danceability, loudness, and tempo, have exhibited an upward trend in recent years. Conversely, features such as instrumentalness, valence, and duration_ms have demonstrated a downward trend. This suggests that there is a growing preference among listeners for music that offers heightened sensory stimulation. This trend aligns with the increasing popularity of short videos, which also emphasize quick and impactful content experiences.

## Correlation between Audio Features and the State of the US Economy.
Considering the variations in the audio features over the years, it would be intriguing to explore their correlation with the economy. To investigate this, we will utilize the Nasdaq Composite Index (^IXIC), the S&P 500 Index (^SPX), and the Dow Jones Index (^DJI) as proxies for tracking the US economy.

![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/c04a4b25-65c5-4e63-a967-2a0608e433c8)


![image](https://github.com/jjjjjooooo/music-analyzer/assets/50882720/2a985935-aba3-4e36-8629-0bc5e3aa6ad4)

It can be observed that the audio feature danceability exhibits a positive correlation with the stock market, to some extent. Conversely, duration_ms demonstrates a negative correlation with the stock market. This implies that during periods of economic growth, there is a higher preference for music with a greater danceability factor. Simultaneously, listeners may show less patience for songs with longer durations.








