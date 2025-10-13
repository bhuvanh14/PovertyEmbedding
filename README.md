
# PovertyEmbedding

## Project Overview
PovertyEmbedding is a machine learning mini-project focused on analyzing poverty and GDP data using various datasets. The project includes data preprocessing, exploratory analysis, and model development in Python.

## Directory Structure

```
PovertyEmbedding/
├── fix.py                      # Utility or data cleaning script
├── ml_mini_project_129_132.ipynb # Main Jupyter notebook for analysis and modeling
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── Datasets/                   # Data files used in the project
	 ├── API_NY.GDP.PCAP.CD_DS2_en_csv_v2_24794.csv
	 ├── API_SI.POV.NAHC_DS2_en_csv_v2_171.csv
	 └── MPI_national.csv
```

## Setup Instructions

1. **Clone the repository**
	```powershell
	git clone <repo-url>
	cd PovertyEmbedding
	```

2. **Create a Python environment (optional but recommended)**
	```powershell
	python -m venv venv
	.\venv\Scripts\activate
	```

3. **Install dependencies**
	```powershell
	pip install -r requirements.txt
	```

## Running the Project

### Jupyter Notebook
1. Launch Jupyter Notebook:
	```powershell
	jupyter notebook
	```
2. Open `ml_mini_project_129_132.ipynb` and run the cells to execute the analysis.

### Python Script
To run the utility script (if needed):
```powershell
python fix.py
```

## Datasets
All datasets are located in the `Datasets/` folder. These include:
- World Bank GDP per capita data
- World Bank poverty headcount ratio data
- Multidimensional Poverty Index (MPI) national data

## Notes
- Ensure all required packages are installed before running the notebook or scripts.
- For any issues, check the dependencies in `requirements.txt`.

## License
See repository for license information.
