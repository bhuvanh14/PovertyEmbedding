
# PovertyEmbedding: End-to-End Country Poverty Analysis with Wikipedia Embeddings, GDP, and MPI

## Project Overview
This project builds a comprehensive pipeline to analyze and predict country-level poverty rates by combining:
- Wikipedia country summaries (textual context)
- Semantic text embeddings
- GDP per capita data
- Multidimensional Poverty Index (MPI) metrics

The goal is to create a rich dataset that merges qualitative and quantitative features, then apply machine learning models to predict poverty rates and interpret global poverty patterns.

## Pipeline Steps
1. **Wikipedia Country Summary Collection**
	- Uses Python (`wikipedia`, `pycountry`, `pandas`) to fetch short summaries for all countries.
	- Output: `wikipedia_countries.csv` (country, summary)

2. **Embedding Generation**
	- Loads `wikipedia_countries.csv` and uses SentenceTransformers (`all-MiniLM-L6-v2`) to generate semantic embeddings for each summary.
	- Output: `wikipedia_country_embeddings.csv` (country, summary, embedding dims)

3. **Poverty Data Integration**
	- Loads World Bank poverty data from `API_SI.POV.NAHC_DS2_en_csv_v2_171.csv`.
	- Extracts poverty rates for a target year (e.g., 2018), aligns country names, and merges with Wikipedia embeddings.

4. **GDP per Capita Integration**
	- Loads GDP data from `API_NY.GDP.PCAP.CD_DS2_en_csv_v2_24794.csv`.
	- Merges GDP per capita with the combined Wikipedia-poverty dataset.

5. **MPI Data Integration**
	- Loads MPI data from `MPI_national.csv`.
	- Calculates average poverty rate from urban/rural MPI, merges with Wikipedia embeddings and other features.

6. **Exploratory Data Analysis (EDA)**
	- Visualizes distributions, correlations, and relationships between GDP, poverty, and embedding features.
	- Plots global poverty rates on a world map using Plotly.

7. **Feature Engineering & Selection**
	- Scales features, selects top features based on correlation with poverty rate.
	- Prepares data for machine learning.

8. **Model Training & Evaluation**
	- Trains regression models (Linear, Ridge, Lasso, ElasticNet, SVR, RandomForest, LightGBM) to predict poverty rates.
	- Uses Randomized and Grid Search for hyperparameter tuning.
	- Evaluates models on test set and interprets results.

9. **Error Analysis**
	- Analyzes model residuals to identify patterns and outliers in predictions.

## Datasets & Their Roles
- **API_SI.POV.NAHC_DS2_en_csv_v2_171.csv**: World Bank poverty rates by country and year. Used as the main target variable for prediction and analysis.
- **API_NY.GDP.PCAP.CD_DS2_en_csv_v2_24794.csv**: GDP per capita by country and year. Used as a key economic feature to improve model accuracy and interpretability.
- **MPI_national.csv**: Multidimensional Poverty Index data, including urban/rural headcounts and deprivation intensity. Used for alternative poverty metrics and deeper analysis.
- **wikipedia_countries.csv**: Raw Wikipedia summaries for each country. Used for generating semantic embeddings.
- **wikipedia_country_embeddings.csv**: Final dataset with country, summary, and embedding vectors. Used as input features for modeling and merging with other datasets.

## End-to-End Flow
1. **Data Collection**: Gather Wikipedia summaries, poverty rates, GDP, and MPI data for all countries.
2. **Feature Creation**: Generate text embeddings, align country names, and merge all datasets.
3. **EDA & Visualization**: Explore distributions, correlations, and visualize poverty rates globally.
4. **Feature Engineering**: Scale and select relevant features for modeling.
5. **Modeling**: Train and tune regression models to predict poverty rates using all available features.
6. **Evaluation & Interpretation**: Assess model performance, analyze errors, and interpret feature importance.

## How Each Dataset Contributes
- **Wikipedia summaries/embeddings**: Provide rich, contextual information about each country, capturing geography, economy, and social conditions.
- **GDP per capita**: Directly measures economic prosperity, strongly correlated with poverty rates.
- **Poverty rates (World Bank)**: Main target for prediction and analysis.
- **MPI data**: Offers alternative and multidimensional poverty metrics for robust analysis.

## Technologies Used
- Python (pandas, numpy, scikit-learn, sentence-transformers, matplotlib, seaborn, plotly, pycountry, wikipedia)
- Jupyter Notebook for pipeline development and visualization

## Project Outcomes
- Merged, enriched dataset combining text, economic, and poverty metrics
- Visualizations and insights into global poverty patterns
- Predictive models for country-level poverty rates
- Error analysis and interpretation of model results

## Folder Structure
- `Datasets/`: Contains all raw data files (poverty, GDP, MPI)
- `ml_mini_project_129_132 .ipynb`: Main notebook with code, analysis, and results
- `README.md`: Project overview and pipeline description

---
This README provides a complete overview of the project pipeline, datasets, and end-to-end flow. For details, see the notebook and data files in the repository.