# Map Reducing Google Play Store Applications and Analysis

## Developers

Naresh Vunnam, Jesse Alford II, Luke Carlson, and Hitesh Kolla

## Background

The Google Play Store is an app store for mobile applications available on mobile devices such as phones and tablets running Android. Android device owners are able to access the Google Play Store and download thousands of apps. Each app store page includes its own attributes such as ratings, reviews, app type, and updates. 

## Data Source

https://www.kaggle.com/lava18/google-play-store-apps


## Big Data Qualifications

This is a big data problem due to the “Volume” and “Variety” big V’s. This file contains over 70,000 records of varying information, making this a key candidate for a map reduce problem. Each record has 12 different attributes, most in different formats. These attributes include app category, name, review count, version, android version, dates, and more. 


## Big Data Questions

For each category find the average ratings.
For all categorys find category with the highest number of ratings.
For each category find the lowest size.
For each year find the total number of apps that are updated.


## Setup

Tools Needed: 

Python 3

Excel

Data source mentioned above

1. Pull the repository.

2. Choose a big data solution to follow below.

3. Run the mapper, sort, and reducer python file with the input directory set to your dataset.

4. Use a bar graph to graph the reduced data file. Default settings were used in this repository.

5. Complete!

## Big Data Solutions

### Hitesh Kolla
For each category find the average ratings.

	Mapper input:  	
		-App: Photo Editor & Candy Camera & Grid & ScrapBook
		-Category: ART_AND_DESIGN
		-Rating: 4.1
		-Reviews: 159
		-Size: 19MB
		-Installs: 10,000+

	Mapper output / Reducer input:  key: ART_AND_DESIGN, value: 4.9 (example:ART_AND_DESIGN, 4.9 )
	Reducer output:   key: ART_AND_DESIGN, value: 4.9 (average: 3.5 )
	Language:  We will be using Python for our MR project.
### Execution
	python mapper.py
![screenshot 206](https://user-images.githubusercontent.com/31717045/49252464-be462e00-f3e9-11e8-8880-06f298dd85d2.png)

	python sort.py
	python reducer.py
![screenshot 208](https://user-images.githubusercontent.com/31717045/49252435-ab335e00-f3e9-11e8-9009-b814bbd92e73.png)
	
	What kind of chart will you use to display your results?  Bar Graph
	Story: The following graph describes the average rating for each category where "Education" category has the highest average
	rating with 4.36 and "Business" category has the lowest average rating with 2.71.  

![story_average_rating 1](https://user-images.githubusercontent.com/31717045/49251004-04998e00-f3e6-11e8-8446-91f67407059d.JPG)
	
	Problems faced: While doing the average ratings in our data we had some rows of data as NaN due to which the reducer 
	output does not result in the complete values. So, in this scenario I have decided to make the data with NaN to '0'.
	After doing this change	in the data the program worked well and gave me exact results that matches with the excel outputs. 
	Comparing the outputs of reducer with excel gives you perfection.
	
### Jesse Alford II
For all categorys find category with the highest number of ratings.

	Mapper input:  
		-App: Coloring Book Moana
		-Category: ART_AND_DESIGN
		-Rating: 3.9
		-Reviews: 967
		-Size: 14MB
		-Installs: 500,000+

	Mapper output / Reducer input:  key: ART_AND_DESIGN, value: 967 (example:ART_AND_DESIGN, 967 )
	Reducer output:   key: ART_AND_DESIGN, value: sumOfAllRatings (sum: 1451598)
	Language:  We will be using Python for our MR project.
	
	
## Execution
	Python Mapper.py
![mapperPNG](Max_reviews/mapperPNGFix.png?raw=true)

	Python Sort.py
	Python Reducer.py
![reducerPNG](Max_reviews/reducerPNGFix.png?raw=true)

	What kind of chart will you use to display your results?  Bar Graph
	Story: In the graph below it is apparent that game, communication, and social have the highest amount of reviews. It cannot be
		guaranteed from this graph alone, but it is likely that the high review count is directly related to the popularity of each category. First of the three, Beauty likely uses large files to allow huge high resolution camera changes. And large data logs of color. Communication likely has to keep map resources for offline. Events surprised me, creators likely keep the entire app available for use offline, requiring a much greater file size.
	Problems: Opening the CSV using the default method did not work, and Latin-1 encoding had to be used. Using a CSV(comma-seperated-values) introduced the problem of having to first eliminate non CSV commas from the file. E.G.(The comma in 5,000).

	
![Category Review Count](Max_reviews/maxReviewsBarChart.png?raw=true)

### Luke Carlson
For each category find the lowest size.

	Mapper input:  
		-App: Draw & Paint
		-Category: ART_AND_DESIGN
		-Rating: 4.5
		-Reviews: 215,644
		-Size: 25MB
		-Installs: 50,000,000+

	Mapper output / Reducer input:  key: ART_AND_DESIGN, value: 25 (example:ART_AND_DESIGN, 25 )
	Reducer output:   key: ART_AND_DESIGN, value: 25 (minimum: 25 )
	Language:  We will be using Python for our MR project.
	Python Mapper.py
![mapperPNG](LowestSizeResources/check1.png?raw=true)
	Python Sort.py
	Python Reducer.py
![mapperPNG](LowestSizeResources/check2.png?raw=true)
	
	What kind of chart will you use to display your results?  Bar Graph
	Story: Most apps are designed to be as small in size as possible, but how small can some apps be? This graph shows that almost 	every app category has at least one app that is nearly one megabyte. However there are three exceptions, beauty, communication and events.



	
![mapperPNG](LowestSizeResources/MinAppChartgg.png?raw=true)

### Naresh Vunnam
For each year find the total number of apps that are updated for the year 2018.

	Mapper input:  
		-App: Infinte Painter
		-Category: ART_AND_DESIGN
		-Size: 29MB
		-Installs: 1,000,000+
		-Content Rating: Everyone
		-Last Updated: 14-Jun-18

	Mapper output / Reducer input:  key: year, value: 10 (example:year, 10 )
	Reducer output:   key: year, value: 10 (2018: 10 )
	Language:  We will be using Python for our MR project.
### Execution
	python mapper.py
![screenshot 217](https://user-images.githubusercontent.com/31740220/49252000-82f72f80-f3e8-11e8-95a5-8a905fbaf2dd.png)

	python sort.py
	python reducer.py
![screenshot 218](https://user-images.githubusercontent.com/31740220/49252059-a4f0b200-f3e8-11e8-9bf4-045e65e06f8c.png)
	
	What kind of chart will you use to display your results?  Bar Graph
	Story: The bar graph below clearly demonstrates that the apps under the categories "Family" and "Games" are the ones with
	morethan 600 and 400 apps updated in the year 2018 respectively. Whereas categories like "LIBRARIES_AND_DEMO", "BEAUTY" and
	"WEATHER" are the ones with less than 30 apps updated in 2018.
	
![story_lastupdate](https://user-images.githubusercontent.com/31740220/49609905-8e0b0c00-f962-11e8-965e-e2dca9a96d8b.JPG)

	Problems faced: As my question is "For each year find the total number of apps that are updated for the year 2018".
	I have faced a problem with comparing the date. Because the dates are of different format in the data. So, I have 
	changed all the dates to single format and in the reducer I have compared for the dates having the year 2018 which 
	made it easy for me to get the expected results.
