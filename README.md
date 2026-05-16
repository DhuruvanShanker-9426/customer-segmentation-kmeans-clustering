# 🛒 Customer Segmentation using RFM Analysis and K-Means Clustering

## 📌 Project Overview

This project focuses on **Customer Segmentation** using **RFM Analysis** and **K-Means Clustering**.

Customer segmentation is a business technique used to divide customers into different groups based on their purchasing behavior. In this project, customers are grouped based on how recently they purchased, how frequently they purchased, and how much money they spent.

The main goal of this project is to identify meaningful customer segments and provide useful business recommendations for each segment.

---

## 🔗 Project Links

- **Live Streamlit App:** [View Deployed App](https://customer-segmentation-kmeans-clustering-hgpcyrnpxj7mw8jmm7ybu6.streamlit.app/)
- **Dataset Source:** [Online Retail II UCI Dataset on Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci/data)

---

## 🎯 Objective

The objective of this project is to:

- Analyze customer purchase behavior
- Create RFM features from transaction data
- Apply preprocessing techniques
- Use K-Means Clustering for customer segmentation
- Identify meaningful customer groups
- Build an interactive Streamlit web app
- Provide business insights and recommendations

---

## 📊 Dataset

The dataset used in this project is the **Online Retail II UCI Dataset** from Kaggle.

This dataset contains online retail transaction records. It includes customer purchases, invoice details, product information, quantity, price, customer ID, and country details.

You can access the dataset here: [Online Retail II UCI Dataset on Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci/data)

---

## 📊 About RFM Analysis

RFM Analysis is a customer behavior analysis technique based on three important metrics:

| Metric | Meaning |
|---|---|
| **Recency** | How recently a customer made a purchase |
| **Frequency** | How often a customer made purchases |
| **Monetary** | How much money a customer spent |

These three features help businesses understand customer activity, loyalty, and value.

---

## 🧠 Machine Learning Technique Used

This project uses **K-Means Clustering**, which is an **unsupervised machine learning algorithm**.

K-Means Clustering is used to group similar customers together based on their behavior. Since this is an unsupervised learning problem, there is no target column. The model finds hidden customer groups using the RFM features.

---

## 📂 Project Workflow

1. Data Loading
2. Data Understanding
3. Data Cleaning
4. RFM Feature Creation
5. Exploratory Data Analysis
6. Log Transformation
7. Feature Scaling using RobustScaler
8. Finding the Best K Value
9. Model Building using K-Means Clustering
10. Customer Segment Creation
11. Segment-wise Analysis
12. Data Visualization
13. Streamlit App Development
14. Business Insights and Recommendations

---

## 🧹 Data Preprocessing

The dataset was cleaned and prepared before applying clustering.

The main preprocessing steps include:

- Handling missing values
- Removing invalid customer records
- Creating customer-level purchase details
- Creating RFM features
- Applying log transformation to reduce skewness
- Scaling the features using RobustScaler

Log transformation was applied because RFM data usually contains outliers, especially in frequency and monetary values.

Feature scaling was applied because K-Means is a distance-based algorithm. If the features are not scaled properly, large-value columns like monetary can dominate the clustering result.

---

## 🔍 Feature Selection

The following features were used for clustering:

| Feature | Description |
|---|---|
| `recency` | Number of days since the customer’s last purchase |
| `frequency` | Number of purchases made by the customer |
| `monetary` | Total amount spent by the customer |

The `Customer_ID` column was not used for clustering because it is only an identifier and does not represent customer behavior.

---

## 📈 Finding the Best Number of Clusters

To find the best number of clusters, different K values were tested.

The following methods were used:

- **Elbow Method**
- **Silhouette Score**

After applying log transformation and RobustScaler, **K = 4** was selected because it provided meaningful and useful customer segments for business analysis.

Although K = 2 gave a higher silhouette score, K = 4 was selected because it created more detailed and business-friendly customer groups.

---

## 🤖 Model Used

The final model used in this project is **K-Means Clustering**.

    KMeans(
        n_clusters=4,
        init='k-means++',
        n_init='auto',
        max_iter=300,
        tol=0.0001,
        random_state=94
    )

The model grouped customers into four different segments based on their RFM behavior.

---

## 👥 Customer Segments

The customers were divided into the following four segments:

| Segment | Description |
|---|---|
| **Inactive / Low-Value Customers** | Customers with low purchase frequency, low spending, and high recency |
| **At-Risk Customers** | Customers who purchased in the past but have not purchased recently |
| **Recent Regular Customers** | Customers who purchased recently and show moderate buying behavior |
| **High-Value Loyal Customers** | Customers who purchase frequently, spend more, and are recently active |

---

## 📊 Segment Summary

| Segment | Avg Recency | Avg Frequency | Avg Monetary | Total Customers |
|---|---:|---:|---:|---:|
| At-Risk Customers | 253.56 | 4.51 | 1712.35 | 1512 |
| High-Value Loyal Customers | 33.50 | 19.07 | 10976.55 | 1226 |
| Inactive / Low-Value Customers | 383.59 | 1.34 | 278.06 | 1896 |
| Recent Regular Customers | 27.99 | 3.40 | 940.44 | 1244 |

---

## 📌 Key Insights

### 1. Inactive / Low-Value Customers

Inactive / Low-Value Customers form the largest customer segment.

These customers have the lowest average frequency and monetary value, and the highest average recency. This means they purchased rarely, spent less, and have not purchased for a long time.

### 2. High-Value Loyal Customers

High-Value Loyal Customers have the highest average frequency and monetary value with low recency.

This means they purchase often, spend more, and are still active customers.

### 3. At-Risk Customers

At-Risk Customers have moderate frequency and monetary value, but high recency.

This means they were valuable in the past, but they have not purchased recently.

### 4. Recent Regular Customers

Recent Regular Customers have low recency and moderate purchase behavior.

This means they purchased recently and have the potential to become loyal customers if properly engaged.

---

## 💡 Business Recommendations

| Segment | Recommendation |
|---|---|
| **Inactive / Low-Value Customers** | Send reactivation offers, discount coupons, and reminder campaigns |
| **At-Risk Customers** | Use win-back campaigns and personalized offers to bring them back |
| **Recent Regular Customers** | Encourage repeat purchases using product recommendations and small loyalty offers |
| **High-Value Loyal Customers** | Provide premium offers, loyalty rewards, early access deals, and personalized service |

---

## 📊 Visualizations

The following visualizations were created to analyze customer segments:

- Segment-wise customer count
- Segment-wise average recency
- Segment-wise average frequency
- Segment-wise average monetary value

These visualizations helped in understanding the size, value, and behavior of each customer group.

---

## 🌐 Streamlit Web App

An interactive Streamlit application was developed and deployed for this project.

The app helps users explore the customer segmentation results and understand customer groups in a simple and visual way.

You can view the deployed application here: [View Deployed App](https://customer-segmentation-kmeans-clustering-hgpcyrnpxj7mw8jmm7ybu6.streamlit.app/)

---

## 🛠️ Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

---

## ✅ Project Conclusion

In this project, customer segmentation was performed using **RFM Analysis** and **K-Means Clustering**.

The customers were grouped into four meaningful segments:

- Inactive / Low-Value Customers
- At-Risk Customers
- Recent Regular Customers
- High-Value Loyal Customers

The project shows how unsupervised machine learning can be used to understand customer behavior and support business decision-making.

By identifying different customer groups, businesses can create targeted marketing strategies, improve customer retention, and increase sales performance.

---

## 🚀 Final Outcome

This project helped convert raw customer purchase data into meaningful customer segments.

The results can be used by businesses to:

- Understand customer behavior
- Identify valuable customers
- Re-engage inactive customers
- Improve marketing strategies
- Increase customer retention
- Support data-driven business decisions.

The project also includes a deployed Streamlit application, making the results easy to explore and present.