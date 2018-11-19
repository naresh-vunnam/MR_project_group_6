# Map Reducing Google Play Store Applications and Analysis

## Developers:

Jesse Alford II, Luke Carlson, Hitesh Kolla, and Naresh Vunnam

## Background

The Google Play Store is an app store for mobile applications available on mobile devices such as phones and tablets running Android. Android device owners are able to access the Google Play Store and download thousands of apps. Each app store page includes its own attributes such as ratings, reviews, app type, and updates. 

## Data Source

https://www.kaggle.com/lava18/google-play-store-apps


## Big Data Qualifications

This is a big data problem due to the “Volume” and “Variety” big V’s. This file contains over 70,000 records of varying information, making this a key candidate for a map reduce problem.


## Big Data Questions

For each category find the average ratings.
For each category find the maximum number of reviews.
For each category find the lowest size.
For each year find the total number of apps that are updated.

## Big Data Solutions

For each category find the average ratings.

	Mapper input:  	
		-App
		-Category
		-Rating
		-Reviews
		-Size
		-Installs
		-Photo Editor & Candy Camera & Grid & ScrapBook
		-ART_AND_DESIGN
		-4.1
		-159
		-19M
		-10,000+

	Mapper output / Reducer input:  key: ART_AND_DESIGN, value: 4.9 (example:ART_AND_DESIGN, 4.9 )
	Reducer output:   key: ART_AND_DESIGN, value: 4.9 (average: 3.5 )
	Language:  We will be using Python for our MR project.
	What kind of chart will you use to display your results?  Bar Graph

For each category find the maximum number of reviews

	Mapper input:  
		-App
		-Category
		-Rating
		-Reviews
		-Size
		-Installs
		-Coloring book moana
		-ART_AND_DESIGN
		-3.9
		-967
		-14M
		-500,000+

	Mapper output / Reducer input:  key: ART_AND_DESIGN, value: 967 (example:ART_AND_DESIGN, 967 )
	Reducer output:   key: ART_AND_DESIGN, value: 967 (maximum: 967)
	Language:  We will be using Python for our MR project.
	What kind of chart will you use to display your results?  Bar Graph

For each category find the lowest size

	Mapper input:  
		-App
		-Category
		-Rating
		-Reviews
		-Size
		-Installs
		-Sketch - Draw & Paint
		-ART_AND_DESIGN
		-4.5
		-215644
		-25M
		-50,000,000+

	Mapper output / Reducer input:  key: ART_AND_DESIGN, value: 25 (example:ART_AND_DESIGN, 25 )
	Reducer output:   key: ART_AND_DESIGN, value: 25 (minimum: 25 )
	Language:  We will be using Python for our MR project.
	What kind of chart will you use to display your results?  Bar Graph

For each year find the total number of apps that are updated

	Mapper input:  
		-App
		-Size
		-Installs
		-Content Rating
		-Genres
		-Last Updated
		-Infinite Painter
		-29M
		-1,000,000+
		-Everyone
		-Art & Design
		-14-Jun-18

	Mapper output / Reducer input:  key: year, value: 10 (example:year, 10 )
	Reducer output:   key: year, value: 10 (2018: 10 )
	Language:  We will be using Python for our MR project.
	What kind of chart will you use to display your results?  Bar Graph
