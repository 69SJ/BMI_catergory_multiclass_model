# BMI_catergory_multiclass_model

A machine learning project for processing SAS XPT files, visualizing data, and training/testing predictive models using Jupyter Notebooks.

## Folder Structure

- **dataset/**  
  Contains the raw dataset files.  
  **Note:** The dataset was obtained from the [CDC NHANES 2021-2023](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023) website.

- **feature_plotting/**  
  Contains Jupyter Notebooks and scripts for data visualization and feature analysis (e.g., `feature_plotting.ipynb`).

- **models/**  
  Contains Jupyter Notebooks for training and evaluating various machine learning models such as XGBoost, multinomial logistic regression, and random forest (e.g., `xgboost.ipynb`, `multinomial_logreg.ipynb`, `random_forest.ipynb`).

- **xpt_converter.py**  
  A Python script to convert SAS XPT files into CSV format.

## Environment Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/69SJ/BMI_catergory_multiclass_model
   cd BMI_catergory_multiclass_model

2. **Install Dependencies**

   This project uses Python and pip. Install the required packages by running:

   ```bash
   pip install -r requirements.txt
   ```

   If you do not have a `requirements.txt` file, install at least the following packages:

   - pandas
   - numpy
   - scikit-learn
   - xgboost
   - matplotlib

## Data Processing

The repository includes a script (`xpt_converter.py`) to convert SAS XPT files into CSV format.

**How to Use:**

1. **Update the Script:**  
   Open `xpt_converter.py` and update the directory path to point to the folder where your `.xpt` files are located.

2. **Run the Script:**

   ```bash
   python xpt_converter.py
   ```

   The script will:
   - Search for all `.xpt` files in the specified directory.
   - Convert each file into a CSV file.
   - Save the CSV files in the same directory as the original files.

## Training and Testing

All training and testing procedures are implemented within Jupyter Notebooks.

**Notebooks Include:**

- **Feature Analysis:**  
  `feature_plotting/feature_plotting.ipynb` – For data visualization and feature analysis.

- **Model Training and Evaluation:**  
  - `models/xgboost.ipynb` – For training and evaluating an XGBoost model.
  - `models/multinomial_logreg.ipynb` – For training and evaluating a multinomial logistic regression model.
  - `models/random_forest.ipynb` – For training and evaluating a random forest model.

**How to Run:**

1. Launch Jupyter Notebook or JupyterLab in your terminal:

   ```bash
   jupyter notebook
   ```

2. Navigate to the desired folder (`feature_plotting` or `models`) and open the corresponding notebook.

3. Execute the cells sequentially to reproduce the data processing, model training, and testing steps.

## Reproducibility

- Follow the instructions in each notebook from start to finish to ensure reproducibility of the results.
- Ensure your dataset is placed in the `dataset/` folder as expected by the notebooks and scripts.
- The notebooks include inline comments and documentation to help you understand each step.

## Troubleshooting

- Verify that all required packages are installed.
- Double-check file paths in `xpt_converter.py` and in the notebooks.
- If issues arise, refer to the inline comments within the notebooks or open an issue in the repository for further assistance.

## License

Include your license information here (e.g., MIT License).
```
``` 
