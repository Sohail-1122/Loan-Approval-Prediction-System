import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dotenv import load_dotenv
import os

from prediction import predict_loan
from src.logger import logger

# =====================================================
# LOGGING
# =====================================================

logger.info("=" * 60)
logger.info("LOAN APPROVAL APPLICATION STARTED")
logger.info("=" * 60)

# =====================================================
# CONFIG
# =====================================================

load_dotenv()

st.set_page_config(
    page_title="Loan Approval Intelligence System",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 100%
    );
}

.main-title {
    text-align:center;
    color:#38bdf8;
    font-size:42px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
}

.metric-box {
    background-color:#1e293b;
    padding:20px;
    border-radius:15px;
    border:1px solid #334155;
}

div[data-testid="stMetric"] {
    background-color:#1e293b;
    border:1px solid #334155;
    padding:15px;
    border-radius:15px;
}

.block-container {
    padding-top: 2rem;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
    <div class="main-title">
        🏦 Loan Approval Intelligence System
    </div>

    <div class="subtitle">
        AI Powered Loan Eligibility Assessment Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("# 🏦 Loan Approval AI")

    st.markdown("---")

    st.markdown("""
    ### 📌 About Project

    This Loan Approval Intelligence System uses
    Machine Learning to predict whether a loan
    application will be approved or rejected
    based on applicant financial information,
    credit score, income, liabilities and assets.
    """)

    st.markdown("---")

    st.markdown("""
    ### 🎯 Objective

    • Predict loan approval status

    • Analyze applicant risk profile

    • Evaluate credit worthiness

    • Provide approval probability

    • Assist banking decisions
    """)

    st.markdown("---")

    st.markdown("""
    ### 🤖 Machine Learning Model

    **Algorithm Used**

    • Support Vector Machine (SVM)

    **Type**

    • Supervised Learning

    • Classification Model

    **Output**

    • Approved

    • Rejected
    """)

    st.markdown("---")

    st.markdown("""
    ### 📊 Dataset Features

    • Number of Dependents

    • Education

    • Self Employed

    • Annual Income

    • Loan Amount

    • Loan Term

    • CIBIL Score

    • Residential Assets

    • Commercial Assets

    • Luxury Assets

    • Bank Assets
    """)

    st.markdown("---")

    st.markdown("""
    ### 🛠 Technology Stack

    **Language**

    • Python

    **Libraries**

    • Pandas

    • NumPy

    • Scikit-Learn

    • Streamlit

    • Plotly

    • Joblib
    """)

    st.markdown("---")

    st.markdown("""
    ### 📈 Business Rules

    Higher chance of approval when:

    ✅ High CIBIL Score

    ✅ Higher Income

    ✅ Strong Asset Value

    ✅ Lower Loan Burden

    ✅ Stable Employment
    """)

    st.markdown("---")

    st.success("🟢 Model Status : Active")

    st.info("Version : 1.0.0")

    st.metric("Accuracy", "93.75%")

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("📋 Applicant Information")

col1, col2 = st.columns(2)

with col1:

    no_of_dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=10,
        value=0
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["Yes", "No"]
    )

    income_annum = st.number_input(
        "Annual Income (₹)",
        min_value=50000,
        max_value=10000000,
        value=500000,
        step=10000
    )

    loan_amount = st.number_input(
        "Loan Amount (₹)",
        min_value=10000,
        max_value=50000000,
        value=1000000,
        step=10000
    )

with col2:

    loan_term = st.number_input(
        "Loan Term (Years)",
        min_value=1,
        max_value=20,
        value=2
    )

    cibil_score = st.number_input(
        "CIBIL Score",
        min_value=300,
        max_value=900,
        value=750
    )

    residential_assets_value = st.number_input(
        "Residential Assets Value (₹)",
        min_value=0,
        max_value=100000000,
        value=500000,
        step=10000
    )

    commercial_assets_value = st.number_input(
        "Commercial Assets Value (₹)",
        min_value=0,
        max_value=100000000,
        value=250000,
        step=10000
    )

    luxury_assets_value = st.number_input(
        "Luxury Assets Value (₹)",
        min_value=0,
        max_value=50000000,
        value=100000,
        step=10000
    )

    bank_assets_value = st.number_input(
        "Bank Assets Value (₹)",
        min_value=0,
        max_value=50000000,
        value=200000,
        step=10000
    )

# =====================================================
# PREPROCESSING
# =====================================================

education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

st.markdown("")

predict_btn = st.button(
    "🔍 Predict Loan Status",
    use_container_width=True
)

# =====================================================
# PREDICTION
# =====================================================

if predict_btn:

    sample = [
        no_of_dependents,
        education,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_assets_value
    ]

    prediction, probability = predict_loan(sample)

    st.markdown("---")

    # ==========================================
    # METRICS
    # ==========================================

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            "Approval Probability",
            f"{probability*100:.2f}%"
        )

    with metric2:
        st.metric(
            "CIBIL Score",
            f"{cibil_score}"
        )

    with metric3:
        st.metric(
            "Annual Income",
            f"₹{income_annum:,.0f}"
        )

    st.markdown("---")

    # ==========================================
    # CHARTS
    # ==========================================

    chart_col1, chart_col2 = st.columns([1, 1])

    with chart_col1:

        gauge_color = "#22c55e"

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=probability * 100,

                title={
                    "text": "Approval Probability"
                },

                number={
                    "suffix": "%"
                },

                gauge={
                    "axis": {
                        "range": [0, 100]
                    },

                    "bar": {
                        "color": gauge_color
                    },

                    "steps": [
                        {
                            "range": [0, 50],
                            "color": "#7f1d1d"
                        },
                        {
                            "range": [50, 75],
                            "color": "#f59e0b"
                        },
                        {
                            "range": [75, 100],
                            "color": "#16a34a"
                        }
                    ]
                }
            )
        )

        fig.update_layout(
            height=450,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with chart_col2:

        asset_fig = go.Figure()

        asset_fig.add_bar(
            x=[
                "Residential",
                "Commercial",
                "Luxury",
                "Bank"
            ],
            y=[
                residential_assets_value,
                commercial_assets_value,
                luxury_assets_value,
                bank_assets_value
            ]
        )

        asset_fig.update_layout(
            title="Asset Distribution",
            height=450,
            paper_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            asset_fig,
            use_container_width=True
        )

# ==========================================
# RESULT
# ==========================================

    st.markdown("---")

    
    approval_probability = probability
    rejection_probability = 1 - probability
    
    if prediction == 0:
    
        st.markdown(
            f"""
            <div style="
            background: linear-gradient(135deg,#16a34a,#22c55e);
            padding:25px;
            border-radius:15px;
            color:white;
            text-align:center;
            box-shadow:0px 4px 15px rgba(0,0,0,0.3);
            ">
    
            <h2>✅ LOAN APPROVED</h2>
    
            <h3>Approval Probability: {approval_probability:.2%}</h3>
    
            <p>
            Congratulations! The applicant meets the eligibility criteria
            for loan approval.
            </p>
    
            </div>
            """,
            unsafe_allow_html=True
        )
    
    else:
    
        st.markdown(
            f"""
            <div style="
            background: linear-gradient(135deg,#dc2626,#ef4444);
            padding:25px;
            border-radius:15px;
            color:white;
            text-align:center;
            box-shadow:0px 4px 15px rgba(0,0,0,0.3);
            ">
    
            <h2>❌ LOAN REJECTED</h2>
    
            <h3>Rejection Probability: {rejection_probability:.2%}</h3>
    
            <p>
            The applicant does not currently satisfy the
            required approval criteria.
            </p>
    
            </div>
            """,
            unsafe_allow_html=True
        )
    
    logger.info(
        f"Prediction={prediction}, "
        f"Approval={approval_probability:.2%}, "
        f"Rejection={rejection_probability:.2%}"
    )