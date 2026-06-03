# 💻 Laptop Price Predictor
 
> An end-to-end machine learning web app that predicts laptop prices in **₹ (INR)** based on 17 hardware and software specifications — built with Scikit-learn and deployed live on Streamlit Cloud.

---
 
## 📌 Overview
 
This project builds a **regression-based ML pipeline** trained on real laptop market data to predict prices. The model uses **log-transformation** on the target variable to handle price skewness, and applies `np.exp()` at inference time to reverse it back to the actual INR price.
 
The trained `FullPipeline.pkl` is loaded into a clean **Streamlit** interface where users configure laptop specs and get an instant ₹ price estimate.

> NOTE that Laptop prices may vary according to the selling platforms and time as The Dataset was old 
 
---

## 🔬 Notebook Walkthrough (`laptop_price_pred.ipynb`)
 
The notebook covers the complete ML lifecycle:
 
1. **Data Loading** — `laptop_data.csv` with real market specs and prices
2. **EDA** — Distribution analysis, correlation, outlier detection
3. **Feature Engineering** — Extracting CPU brand/tier/speed, GPU brand, PPI, memory parsing (SSD/HDD/Flash/Hybrid), OS normalization
4. **Target Transformation** — `log(Price)` to reduce skewness
5. **Pipeline Building** — Combining preprocessor (OneHotEncoder + scaling) with regressor
6. **Model Training & Evaluation** — Regression model tuning and validation
7. **Serialization** — Exporting the **fitted** pipeline as `FullPipeline.pkl` using `pickle`
---
 
## 💡 Key Learnings
 
> Noted in `what_i_learned.txt`:
 
- Always **reverse the power transformation** at prediction time — `np.exp()` is applied to convert log-price back to actual ₹ price
- Always **export the fitted pipeline**, not the unfitted one — else the model will be untrained
- Basics of building and deploying Streamlit apps
---
 
## 🚀 Getting Started
 
```bash
# 1. Clone the repository
git clone https://github.com/RaviNamdeoo/LaptopPricePredictor.git
cd LaptopPricePredictor
 
# 2. Install dependencies
pip install -r requirements.txt
 
# 3. Run the app
streamlit run app.py
```
 
Open `http://localhost:8501` in your browser.
 
---
 
## 📦 Dependencies
 
```
numpy
pandas
streamlit
scikit-learn==1.8.0
```
 
---
 
## 🌐 Live Demo
 
👉 **[laptoppricepred-ravi.streamlit.app](https://laptoppricepred-ravi.streamlit.app/)**
 
---
 
## 🏷️ Topics
 
`machine-learning` · `regression` · `streamlit` · `python` · `scikit-learn` · `laptop-price-prediction` · `data-science` · `feature-engineering`
 
---
 
## 👤 Author
 
**Ravi Namdeo**
- GitHub: [@RaviNamdeoo](https://github.com/RaviNamdeoo)
- LinkedIn: [ravinamdeo](https://www.linkedin.com/in/ravinamdeo/)
 
