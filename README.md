# Map Reducing Google Play Store Applications and Analysis

## Developers:

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

## Big Data Solutions

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
	What kind of chart will you use to display your results?  Bar Graph
	Story: The following graph describes the average rating for each category where "Education" category has the highest average
	rating with 4.36 and "Business" category has the lowest average rating with 2.71.  

![story_average_rating 1](https://user-images.githubusercontent.com/31717045/49251004-04998e00-f3e6-11e8-8446-91f67407059d.JPG)

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
	What kind of chart will you use to display your results?  Bar Graph
	Story: In the graph below it is apparent that game, communication, and social have the highest amount of reviews. It cannot be
		guaranteed from this graph alone, but it is likely that the high review count is directly related to the popularity of each category. 
	
![Category Review Count](Max_reviews/maxReviewsBarChart.png?raw=true)

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
	What kind of chart will you use to display your results?  Bar Graph

For each year find the total number of apps that are updated.

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
	What kind of chart will you use to display your results?  Bar Graph
	Story: The bar graph below clearly demonstrates that the apps under the categories "Family" and "Games" are the ones with
	morethan 1000 and 700 apps updated in the year 2018 respectively. Whereas categories like "LIBRARIES_AND_DEMO", "BEAUTY" and
	"EVENTS" are the ones with less than 50 apps updated in 2018.
	
![story_lastupdate](https://user-images.githubusercontent.com/31740220/49110669-bbb1d000-f253-11e8-924a-b20f31e5ddd6.JPG)

