# Comprehensive Social Networking Platform

### About
This project processes and analyzes content data from popular streaming platforms: Netflix, Hulu, and Amazon Prime Video. The scripts aim to clean the raw data, combine it for comprehensive analysis, identify content overlaps, and prepare it for further insights, such as trends in release years, ratings, and content additions.

### Installation 

### Prerequisites
- Java Development Kit (JDK) 8 or higher.
- Basic command-line interface knowledge.

### Server Setup
```bash
- # Clone the repository
- git clone https://github.com/pate2389/data_wrangling.git

- # Run in order...
- CleaningData
- FilteringData
- MergingData
- Sorting Data

- # View graphical visualizations in any order by running...
- bargraph
- boxplot
- histogram
- linechart
- scatterplot

```

---

## Features

### Data Manipulation
- Cleaning and filtering data
- Merging and sorting data 

### Data Presentation
- Data displayed in various graphical forms (boxplot, bar-graph...)

---

## System Components

### Data Wrangling
**CleaningData:** Data Ingestion and Initial Cleaning
+ Forward filling missing values. Eliminating redundant rows to maintain data integrity and accuracy.

**FilteringData:** Data Integration and Filtering
+ Adding a dedicated 'Platform' column to each dataset (e.g., 'Netflix', 'Hulu', 'Amazon Prime') to easily distinguish content origin after combining. Merging the individual platform datasets into a single, comprehensive DataFrame to enable cross-platform analysis. Converting relevant columns, such as 'release_year', to appropriate numeric types for accurate filtering and calculations. Isolating content released within specific timeframes (e.g., 2000-2010) to focus on particular historical periods. Separating content into distinct DataFrames for "Movies" and "TV Shows" for focused analysis of each category.

**MergingData:** Content Overlap and Relationship Analysis
+ Performing inner merges across platforms based on the 'title' column to pinpoint movies and TV shows available on multiple services. This helps understand content exclusivity and overlap. Utilizing outer merges on 'release_year', 'type', and 'Platform' columns. While the current implementation overwrites release_years_df in successive steps, this functionality is intended to identify commonalities or differences in content characteristics across platforms.

**SortingData:** Data Sorting and Ordering
+ Ordering content chronologically to observe historical trends in content additions. Arranging content based on its age rating to understand content demographics. Ordering content by the date it was added to the platform, highlighting recent additions. Organizing content by its country of origin to analyze geographical distribution.


---


### Contributors
- **Priya Patel**
- **Shrawani Datar**
- **Raga Pulli**

