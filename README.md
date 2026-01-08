# Portfolio Tracker — Data Science Project

My project builds a data analysis and visualization tool to consolidate investment portfolios. It is useful to see the user's current portfolio return and historical risk. 
The project also uses ML to predict and estimate future risk of the same porfolio.

### Features
- Import holdings manually.
- Fetch or simulate market prices via Yahoo Finance
- Prices are automatically saved in data/
- Compute daily returns, portfolio performance, and KPIs
- Automatic generation of financial plots saved in results/
- Volatility forecasting dataset builder 
- ML forecasting module using 3 models
    1) Naive (baseline)
    2) Linear Regression
    3) Random Forest
- Automatic model selection based on lowest MAE
- Next week volatility prediction
- Portfolio value impact estimate based on next 5 days volatility
### Structure 
```text
FutureVolatility_project_LB/
├── main.py                    # Main entry point
├── src/                       # Source code
│   ├── io.py                  # Data loading / preprocessing
│   ├── kpis.py                # KPIs calculation
│   ├── manual_input.py        # Data input / collection
│   ├── model_training.py      # Model training
│   ├── risk_models.py         # Feature builder
│   └── transform.py           # Evaluation metrics
├── data/                      # Data from base portfolio
├── results/                   # Output plots and metrics
├── requirements.txt           # Requirements
├── PROPOSAL.md                # Proposal
├── Final_report.pdf           # Final report
└── environment.yml            # Dependencies
```

## How to run the project

## 1) Clone the repository, install requirment and run main()
```bash
git clone <https://github.com/LorisBe/FutureVolatility_project_LB.git>
cd FutureVolatility_project_LB
conda env create -f environment.yml
conda activate capstone_portfolio
python main.py
```
### 2) Enter Loris' base portfolio for same result (adjusted for recent move  in price)

Full brake down of my portfolio for you to enter in the code to run and get the result of my personal portfolio : 

**1)**  
Ticker: XRP-USD  
Quantity: 61.722937  
Average cost per unit: 2.2  
Asset type: Crypto  
Currency: USD  

**2)**  
Ticker: BTC-USD  
Quantity: 0.000681  
Average cost per unit: 83682  
Asset type: Crypto  
Currency: USD  

**3)**  
Ticker: NVDA  
Quantity: 2.619475  
Average cost per unit: 175  
Asset type: Equity  
Currency: USD  

**4)**  
Ticker: SPY  
Quantity: 17.481  
Average cost per unit: 523  
Asset type: Equity  
Currency: USD  

**5)**  
Press Enter on an empty ticker to end the input.

## Results

Result are dynamic in this project, meaning you'll get different result each time you run the program as the entries will be different and the prices will be updated daily. However, for the sake of this project, a base case portfolio was created and ran on the 26th of december 2025. The result were : 
```text
| Model            | Average Absolute Error | Average Squared Error | RMSE     |
| ---------------- | ---------------------- | --------------------- | -------- |
| **Naive**        | 0.225177               | 0.106795              | 0.326796 |
| **LinearReg**    | 0.189103               | 0.074172              | 0.272346 |
| **RandomForest** | 0.180084               | 0.074678              | 0.273273 |


Predicted next-week annualized volatility: 0.4353

Approximate 5-day volatility (1σ): 6.13%

Based on this estimate, over the next 5 trading days the portfolio value could typically fluctuate by ±6.13%.

Current portfolio value: 12629.97

Expected range (1σ): [11855.56 , 13404.37]
```
# Enjoy!


