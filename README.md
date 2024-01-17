# PowerBI-Spotify-user-report-dashboard
## Dashboard Snapshot
![image](https://github.com/SaroashDS/PowerBI-Spotify-user-report-dashboard/assets/144798692/a0cd348d-9bca-43da-a0cb-0cb5983295a4)

### Dashboard Link : https://studentuetedupk-my.sharepoint.com/:u:/g/personal/2018me140_student_uet_edu_pk/ESHECpwa8vlIqeI_VK-ANKgB9Ji7AzSpl-TteZh5-pDNBA?e=BCIaa9

## Problem Statement

This dashboard aims to provide comprehensive insights into music streaming data, enabling users to analyze track popularity, artist performance, and user preferences in a visually appealing manner. This can be really user for people who listen to music all the time.


### Steps followed 
1. Objective Definition:
   - Develop a detailed music streaming dashboard for data-driven decision-making in the music industry.
2. Data Collection:
   - Gathered data on track names, artists, release dates, and stream counts from a latest kaggle dataset.
3. Data Preparation:
   - Cleaned and formatted the data for analysis, addressing any missing or inconsistent values. Renamed the columns.
   - Used spotify API to fetch the song cover photos utilizing python script (song_fetch.py). The urls were then added to the dataset
4. Dashboard Design:
   - Key Metrics:
       = Total Streams: Represents the overall stream count.
       = Top Song vs. Average: Compares the streams of the top song against the average streams.
   - Visualizations:
        1. Bar Chart (Top Tracks by # of streams):
        
              - X-Axis: Track names
              - Y-Axis: Stream counts
              - Insight: Visual representation of top tracks and their popularity w.r.t the number of streams.
           
                ![image](https://github.com/SaroashDS/PowerBI-Spotify-user-report-dashboard/assets/144798692/8312eeb9-17c3-4187-b739-dc5227b43915)
    
        2. Line Chart (Track by release date):
        
              - X-Axis: Release dates
              - Y-Axis: Stream counts
              - Insight: Depicts the trend in streaming over time.
  
                ![image](https://github.com/SaroashDS/PowerBI-Spotify-user-report-dashboard/assets/144798692/80dfc9b8-f408-45a5-a0bd-7526b3ee8ac3)

        3. Heat Map (Energy Distribution):
        
              - X-Axis: Energy levels
              - Y-Axis: Stream counts
              - Insight: Highlights the distribution of energy levels across tracks.
  
                ![image](https://github.com/SaroashDS/PowerBI-Spotify-user-report-dashboard/assets/144798692/0f1a4671-447c-4b26-8bf2-7cb022b7d116)

        4. KPI Cards:
        
              - Average Streams: Displays the average stream count.
                
                ![image](https://github.com/SaroashDS/PowerBI-Spotify-user-report-dashboard/assets/144798692/a39ef360-4106-4db7-bcae-4526c0a7a22b)
                
              - Top Song Streams Vs Average: Displays stream count for the top song.
                
                ![image](https://github.com/SaroashDS/PowerBI-Spotify-user-report-dashboard/assets/144798692/98609639-54ee-47b2-ba40-f2094522d39d)
                
              - Top Artist Streams: Displays stream count for the top artist.
                
                ![image](https://github.com/SaroashDS/PowerBI-Spotify-user-report-dashboard/assets/144798692/5c578dd1-5e6f-4d0b-aa8f-188ab25a5e7a)
                
5. DAX Measures:
   1.  Top Song Streams:
       - Calculates the stream count for the top song.
        ```DAX
        Top Song Streams = CALCULATE(SUM('MusicData'[StreamCount]), TOPN(1, 'MusicData', 'MusicData'[StreamCount], DESC))
        ```
   2.  Average Streams:
       - Computes the average stream count.
        ```DAX
        Average Streams = AVERAGE('MusicData'[StreamCount])
        ```
   3.  Top Artist Streams:
       - Determines the stream count for the top artist.
        ```DAX
        Top Artist Streams = CALCULATE(SUM('MusicData'[StreamCount]), TOPN(1, VALUES('MusicData'[Artist]), 'MusicData'[StreamCount], DESC))
        ```
   4.  Energy Range:
       - Groups tracks into energy ranges for the heat map.
        ```DAX
        Energy Range = SWITCH(TRUE(), 'MusicData'[Energy] < 0.25, "Low", 'MusicData'[Energy] >= 0.25 && 'MusicData'[Energy] < 0.75, "Medium", 'MusicData'[Energy] >= 0.75, "High")
        ```
   5.  Max Streams:
       - Finds the maximum stream count.
        ```DAX
        Max Streams = CALCULATE(MAX('MusicData'[StreamCount]))
        ```  
6.Visual Enhancements:
 - Adjusted chart sizes, colors, and labels for improved readability.
 - Customized themes to match the aesthetics of the music streaming industry.
 - The hex codes for spotify theme were grabbed from https://www.color-hex.com/color-palette/53188
 - Created a custom structure on powerpoint and used it on power BI
   

![image](https://github.com/SaroashDS/PowerBI-Spotify-user-report-dashboard/assets/144798692/de1047d6-af88-4750-a020-471dc86440a3)

7. Finalization:
 - Conducted user testing to ensure the dashboard's effectiveness.
 - Published the dashboard for broader use.

## Major Insights

- Top Tracks:

Identified the most-streamed tracks, aiding in playlist curation.

- Stream Trends:

Analyzed trends over time, identifying periods of increased or decreased streaming activity.

- Energy Distribution:

Explored the distribution of energy levels across tracks, helping in genre-specific analysis.

- Top Artist Performance:

Evaluated the stream counts for the top artist, indicating their popularity.

- Average Stream Count:

Provided a benchmark for evaluating the success of tracks and artists.

## Use Case
Music streaming platforms can leverage this dashboard to understand user preferences, optimize playlists, and make informed decisions about artist collaborations and promotions.

## Conclusion
This dashboard serves as a powerful tool for extracting actionable insights from music streaming data, empowering stakeholders in the music industry to make strategic decisions.
