# Income-Disparities-Food-Deserts-in-the-U.S.

**Introduction:**
Food deserts can be found all across the United States. Food deserts are geographical locations where low-income communities do not have access to a     store with affordable fresh foods. "Food desert" communitites tend to have worse health issues like higher obesity levels so it is important to provide access to fresh foods where possible. When trying to find food deserts, you will likely see lower (average) family incomes and higher average poverty rates. The idea behind this streamlit app is to be able to see which states and even which ethnicities experience more food deserts, or have high poverty rates which could lead to more food deserts. As a Health Informatics and Analytics masters student, this topic is important as it can show us where changes are needed, what health issues are being seen from these areas, and which populations experience food deserts the most. 

**Data/operation abstraction design:**
The Food Access Research Atlas Data (2019) was provided by the United States Department of Agriculture (USDA ERS). The data set is very large which means I had to turn it into a zip file for GitHub to be able to access it. Since the dataset is so large, I did add in st.cache_data so that the app would not have to re-read the dataset everytime a filter is applied. While the dataset was robust, it would be have been interesting to see this dataset include multiple years to show how the poverty rates or grocery store access has changed overtime. 

**Future work:**
The Food Access Research Atlas Data (2019) had data around age groups, ethncities, distances from stores, access to vehicles, etc. Future work on this app would pull in additional attributes to further identify where and who are experiencing food deserts. As a student with a focus in healthcare, it would be interesting to see another dataset of the same year but on health issues in these states and counties as well. Does a community experience higher type 2 diabetes rates or high cholesterol because they are 10-miles from a fresh grocery store? If years were included in this dataset, or if this dataset was joined with others from previous years, the app could be made to analyze the years and predict what states, ages, or ethnicities would experience food deserts and income disparaties in the future.
