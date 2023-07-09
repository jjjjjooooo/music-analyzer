# Analysis of pop music

## Introduction
In 2021, the global music industry experienced its fastest growth rate in over two decades, with a total revenue of $25.9 billion, representing an impressive 18.5% increase. Pop music played a significant role in driving this revenue, thanks to artists such as Taylor Swift, Ed Sheeran, and Justin Bieber. The surge in music sales was primarily fueled by the streaming segment, which witnessed a considerable rise in the number of paying subscribers. Notably, the number of paid subscribers reached 523 million in 2021, a substantial increase from the 443 million recorded in 2020.<br />

These remarkable trends have caught my attention, leading me to conduct data analysis using the valuable data provided by the Spotify API. Through this analysis, I aim to explore intriguing questions such as:<br />

1. Who are the most influential artists within the pop music genre?<br />
2. How has the pop music market evolved in terms of its market size and audio features?<br />
3. Is there a correlation between the development of audio features and the state of the US economy?<br />

## Data
* **genre_artist**: The folder is created to store information about the pertinent artists within a specific music genre.
* **artist_album**: The folder is created to store information about the albums by artists.
* **artist_track**: The folder is created to store information about the tracks by artists.
* **track_analysis**: The folder is created to store information about the analysis conducted on the tracks.
* **spotifyapp.py**: This file includes the relevant class and functions required to download and manage all the aforementioned data.
* **EDA.ipynb**: An exploratory data analysis notebook based on the provided data.

## Data Viasualization
In general, the data analysis is conducted on a dataset that includes 970 artists, 33,200 albums, and 167,203 tracks.
### Most Influential Artists

![image](https://github.com/jjjjjooooo/Spotify/assets/50882720/474a93d5-d6ad-4536-a212-a81d5cb0b63e)

![image](https://github.com/jjjjjooooo/Spotify/assets/50882720/b114ac8e-5e8c-452c-99d1-82ce202c16d8)

### Evolution of Market Size

![image](https://github.com/jjjjjooooo/Spotify/assets/50882720/0e8710ba-281d-43aa-9599-c0273844af06)

![image](https://github.com/jjjjjooooo/Spotify/assets/50882720/53a40a05-51fd-41a4-8d8c-12340b7b027f)

### Evolution of Audio Features

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

![image](https://github.com/jjjjjooooo/Spotify/assets/50882720/6d828a81-c52e-405a-9107-4fa2fd2b4f3a)


# Correlation between Audio Features and the State of the US Economy.
Considering the variations in the audio features over the years, it would be intriguing to explore their relationship with the economy. To investigate this, we will utilize the Nasdaq Composite Index (^IXIC), the S&P 500 Index (^SPX), and the Dow Jones Index (^DJI) as proxies for the economy.

![image](https://github.com/jjjjjooooo/Spotify/assets/50882720/646be5f1-17a4-49bb-af3f-e91e7f2d694c)












