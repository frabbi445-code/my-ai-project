import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from predictor import predict_health, generate_mock_data

st.set_page_config(page_title="AI Machine Analyzer", layout="wide")
st.title("🤖 Interactive AI Machine Health Analyzer")
st.markdown("এই ড্যাশবোর্ডটি সিস্টেমের বিভিন্ন প্যারামিটার অ্যানালাইসিস করে ডিভাইসের সামগ্রিক হেলথ প্রেডিক্ট করতে পারে।")

st.sidebar.header("📥 রিয়েল-টাইম সিস্টেম ইনপুট")
cpu = st.sidebar.slider("CPU Usage (%)", 0.0, 100.0, 45.0)
ram = st.sidebar.slider("RAM Usage (%)", 0.0, 100.0, 60.0)
temp = st.sidebar.slider("Temperature (°C)", 30.0, 100.0, 55.0)

predicted_health = predict_health(cpu, ram, temp)

st.subheader("📊 AI Analytics Summary")
col1, col2, col3 = st.columns(3)
col1.metric(label="Current CPU Load", value=f"{cpu} %")
col2.metric(label="Current RAM Load", value=f"{ram} %")
col3.metric(label="System Temperature", value=f"{temp} °C")

st.markdown("---")
st.subheader("🔮 Predictive AI Status")
if predicted_health > 70:
    st.success(f"✅ Your System is Healthy! Predicted Health Score: {predicted_health}/100")
elif 40 <= predicted_health <= 70:
    st.warning(f"⚠️ Warning: System under stress. Predicted Health Score: {predicted_health}/100")
else:
    st.error(f"🚨 Critical Alert: High risk of performance failure! Predicted Health Score: {predicted_health}/100")

st.markdown("---")
st.subheader("📈 Historical Data Analysis (Trends)")
mock_df = generate_mock_data()
fig = px.scatter_3d(mock_df, x='cpu_usage', y='ram_usage', z='temperature',
                    color='health_score', title="3D View of System Variables vs Health Score",
                    labels={'cpu_usage': 'CPU %', 'ram_usage': 'RAM %', 'temperature': 'Temp °C'})
st.plotly_chart(fig, use_container_width=True)