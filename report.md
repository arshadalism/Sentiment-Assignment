# Summary Report

# In the graph
O -> Positive
1-> Negative
2-> Neutral

## Approach
1. Loaded the dataset from the provided XLS file.
2. Cleaned the data by removing null values and unnecessary columns.
3. Preprocessed the text by converting it to lowercase and removing punctuation.
4. Performed sentiment analysis using the TextBlob library.
5. Generated a summary report showing the distribution of sentiments.

## Challenges
- Ensuring the text preprocessing steps correctly handled all edge cases (e.g., various punctuation marks).
- Deciding on the sentiment analysis library that would provide the most accurate results.

## Assumptions
- The 'review' column in the dataset contains the text of the reviews.
- Sentiment analysis results were accurate enough for the purpose of this assignment.

## Results
- Positive reviews: 32
- Neutral reviews: 8
- Negative reviews: 10
