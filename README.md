# PowerBI-Spotify-user-report-dashboard

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
        1. Bar Chart (Top Tracks):
        
              - X-Axis: Track names
              - Y-Axis: Stream counts
              - Insight: Visual representation of top tracks and their popularity.
         
        2. Line Chart (Stream Trend):
        
              - X-Axis: Release dates
              - Y-Axis: Stream counts
              - Insight: Depicts the trend in streaming over time.
        3. Heat Map (Energy Distribution):
        
              - X-Axis: Energy levels
              - Y-Axis: Stream counts
              - Insight: Highlights the distribution of energy levels across tracks.
        4. KPI Cards:
        
              - Average Streams: Displays the average stream count.
              - Top Song Streams: Displays stream count for the top song.
              - Top Artist Streams: Displays stream count for the top artist.
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

![Snap_Count](https://user-images.githubusercontent.com/102996550/174090154-424dc1a4-3ff7-41f8-9617-17a2fb205825.jpg)

        
 - Step 16 : New measure was created to find  % of customers,
 
 Following DAX expression was written to find % of customers,
 
         % Customers = (DIVIDE(airline_passenger_satisfaction[Count of Customers], 129880)*100)
 
 A card visual was used to represent this perecntage.
 
 Snap of % of customers who preferred business class
 
 ![Snap_Percentage](https://user-images.githubusercontent.com/102996550/174090653-da02feb4-4775-4a95-affb-a211ca985d07.jpg)

 
 - Step 17 : New measure was created to calculate total distance travelled by flights & a card visual was used to represent total distance.
 
 Following DAX expression was written to find total distance,
 
         Total Distance Travelled = SUM(airline_passenger_satisfaction[Flight Distance])
    
 A card visual was used to represent this total distance.
 
 
 ![Snap_3](https://user-images.githubusercontent.com/102996550/174091618-bf770d6c-34c6-44d4-9f5e-49583a6d5f68.jpg)
 
 - Step 18 : The report was then published to Power BI Service.
 
 
![Publish_Message](https://user-images.githubusercontent.com/102996550/174094520-3a845196-97e6-4d44-8760-34a64abc3e77.jpg)

# Snapshot of Dashboard (Power BI Service)

![dashboard_snapo](https://user-images.githubusercontent.com/102996550/174096257-11f1aae5-203d-44fc-bfca-25d37faf3237.jpg)

 
 # Report Snapshot (Power BI DESKTOP)

 
![Dashboard_upload](https://user-images.githubusercontent.com/102996550/174074051-4f08287a-0568-4fdf-8ac9-6762e0d8fa94.jpg)

# Insights

A single page report was created on Power BI Desktop & it was then published to Power BI Service.

Following inferences can be drawn from the dashboard;

### [1] Total Number of Customers = 129880

   Number of satisfied Customers (Male) = 28159 (21.68 %)

   Number of satisfied Customers (Female) = 28269 (21.76 %)

   Number of neutral/unsatisfied customers (Male) = 35822 (27.58 %)

   Number of neutral/unsatisfied customers (Female) = 37630 (28.97 %)


           thus, higher number of customers are neutral/unsatisfied.
           
### [2] Average Ratings

    a) Baggage Handling - 3.63/5
    b) Check-in Service - 3.31/5
    c) Cleanliness - 3.29/5
    d) Ease of online booking - 2.88/5
    e) Food & Drink - 3.21/5
    f) In-flight Entertainment - 3.36/5
    g) In-flight service - 3.64/5
    h) In-flight Wifi service - 2.81/5
    i) Leg room service - 3.37/5
    j) On-board service - 3.38/5
    k) Online boarding - 3.33/5
    l) Seat comfort - 3.44/5
    m) Departure & arrival convenience - 3.22/5
  
  while calculating average rating, null values have been ignored as they were not relevant for some customers. 
  
  These ratings will change if different visual filters will be applied.  
  
  ### [3] Average Delay 
  
      a) Average delay in arrival(minutes) - 15.09
      b) Average delay in departure(minutes) - 14.71
Average delay will change if different visual filters will be applied.

 ### [4] Some other insights
 
 ### Class
 
 1.1) 47.87 % customers travelled by Business class.
 
 1.2) 44.89 % customers travelled by Economy class.
 
 1.3) 7.25 % customers travelled by Economy plus class.
 
         thus, maximum customers travelled by Business class.
 
 ### Age Group
 
 2.1)  21.69 % customers belong to '0-25' age group.
 
 2.2)  52.44 % customers belong to '25-50' age group.
 
 2.3)  25.57 % customers belong to '50-75' age group.
 
 2.4)  0.31 % customers belong to '75-100' age group.
 
         thus, maximum customers belong to '25-50' age group.
         
### Customer Type

3.1) 18.31 % customers have customer type 'First time'.

3.2) 81.69 % customers have customer type 'returning'.
       
       thus, more customers have customer type 'returning'.

### Type of travel

4.1) 69.06 % customers have travel type 'Business'.

4.2) 30.94 % customers have travel type 'Personal'.

        thus, more customers have travel type 'Business'.
