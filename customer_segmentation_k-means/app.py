import numpy as np
import joblib
import time
import streamlit as st

st.set_page_config(
    page_title="Customer Segmentation App",
    page_icon="👥",
    layout="centered"
)

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/robust_scaler.pkl")

segment_map = {
    0: "Inactive / Low-Value Customers",
    1: "Recent Regular Customers",
    2: "At-Risk Customers",
    3: "High-Value Loyal Customers"
}

st.title("👥 Customer Segmentation App")

st.markdown(
    """
    This application predicts the **customer segment** based on RFM values.

    **RFM means:**
    - **Recency**: Number of days since the customer's last purchase
    - **Frequency**: Number of purchases made by the customer
    - **Monetary**: Total amount spent by the customer
    """
)

st.markdown("---")

st.subheader("📌 Enter Customer RFM Details")

col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input(
        "Recency",
        min_value=1,
        value=18,
        help="Number of days since the customer's last purchase"
    )

with col2:
    frequency = st.number_input(
        "Frequency",
        min_value=1,
        value=4,
        help="Total number of purchases made by the customer"
    )

with col3:
    monetary = st.number_input(
        "Monetary Value",
        min_value=1.0,
        value=1320.0,
        step=100.0,
        help="Total amount spent by the customer"
    )

if st.button("🔍 Predict Customer Segment"):

    with st.spinner("Predicting customer segment..."):

        time.sleep(3)
        
        user_input = np.array([[recency, frequency, monetary]])

        user_input_log = np.log1p(user_input)

        user_input_scaled = scaler.transform(user_input_log)

        cluster = model.predict(user_input_scaled)[0]

        segment = segment_map[cluster]

    st.markdown("---")
    st.subheader("✅ Prediction Result")

    st.info(f"**Customer Segment:** {segment}")

    st.markdown("### 📊 Entered Customer Details")

    st.info(f"**Recency:** {recency} days")
    st.info(f"**Frequency:** {frequency} purchases")
    st.info(f"**Monetary Value:** ₹{monetary:.2f}")

    st.markdown("### 💡 Business Interpretation")

    if segment == "Inactive / Low-Value Customers":
        st.error("This customer has low purchase activity and has not purchased recently.")
        st.info("**Recommendation:** Send reactivation offers, discounts, or reminder campaigns.")

    elif segment == "Recent Regular Customers":
        st.info("This customer has purchased recently and shows regular buying behavior.")
        st.info("**Recommendation:** Encourage repeat purchases with personalized product recommendations.")

    elif segment == "At-Risk Customers":
        st.warning("This customer had good purchase behavior in the past but has not purchased recently.")
        st.info("**Recommendation:** Use win-back campaigns and special offers to re-engage the customer.")

    else:
        st.success("This customer is highly valuable, purchases frequently, and spends more.")
        st.info("**Recommendation:** Provide loyalty rewards, premium offers, and early access deals.")

st.markdown("---")

with st.expander("ℹ️ Model Information"):
    st.info(
        """
        **Model Used:** K-Means Clustering  
        **Number of Clusters:** 4  
        **Features Used:** Recency, Frequency, Monetary  
        **Preprocessing:** Log Transformation + RobustScaler  
        **Purpose:** Customer Segmentation based on purchasing behavior
        """
    )

st.caption("This project is created for educational and portfolio purposes.")