import streamlit as st
import pandas as pd
import joblib
import time


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Churn.AI",
    page_icon="🤖",
    layout="wide"
)



# ==========================
# PREMIUM UI CSS
# ==========================

st.markdown(
"""
<style>

/* Background */

.stApp{

background:
radial-gradient(
circle at top left,
#1e293b,
#020617 50%
);

color:white;

}



/* Remove Streamlit Branding */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}



/* Hero */

.hero{

text-align:center;

padding:30px;

animation:fadeIn 1.5s;

}



.hero h1{

font-size:70px;

font-weight:900;


background:

linear-gradient(
90deg,
#22d3ee,
#8b5cf6,
#ec4899
);


-webkit-background-clip:text;

color:transparent;


animation:glow 3s infinite alternate;


}



.hero p{

font-size:22px;

color:#cbd5e1;

}



/* Glass Cards */


.card{


background:

linear-gradient(
145deg,
rgba(255,255,255,0.12),
rgba(255,255,255,0.04)
);


backdrop-filter:blur(15px);


padding:30px;


border-radius:25px;


border:

1px solid
rgba(255,255,255,0.18);



box-shadow:

0 20px 40px
rgba(0,0,0,0.4);



transition:

0.4s;



}



.card:hover{


transform:

translateY(-8px)
scale(1.02);



box-shadow:

0 30px 60px
rgba(56,189,248,0.3);



border:

1px solid #38bdf8;


}



/* Sidebar */


section[data-testid="stSidebar"]{


background:

linear-gradient(
180deg,
#111827,
#020617
);



}



/* Sidebar title */


section[data-testid="stSidebar"] h1{


color:#38bdf8;

}



/* Select Boxes */


div[data-baseweb="select"] > div{


background:

rgba(255,255,255,0.08);


border-radius:15px;


}



/* Button */


.stButton button{


width:100%;


height:60px;


border-radius:30px;


background:

linear-gradient(
90deg,
#06b6d4,
#8b5cf6
);



color:white;


font-size:22px;


font-weight:700;



border:none;



transition:

0.3s;


}



.stButton button:hover{


transform:

scale(1.05);



box-shadow:

0 0 35px #8b5cf6;


}



/* Result */


.result{


background:

linear-gradient(
135deg,
rgba(16,185,129,0.25),
rgba(59,130,246,0.2)
);



padding:45px;


border-radius:30px;


text-align:center;


animation:

slideUp 1s;


border:

1px solid rgba(255,255,255,0.2);


}



.result h1{


font-size:50px;



background:

linear-gradient(
90deg,
#22d3ee,
#a855f7
);



-webkit-background-clip:text;


color:transparent;


}



/* Progress */


div[data-testid="stProgressBar"] > div > div{


background:

linear-gradient(
90deg,
#22d3ee,
#8b5cf6
);


}



/* Animations */


@keyframes fadeIn{

from{

opacity:0;

transform:translateY(-30px);

}

to{

opacity:1;

transform:translateY(0);

}

}



@keyframes slideUp{

from{

opacity:0;

transform:translateY(50px);

}

to{

opacity:1;

transform:translateY(0);

}

}



@keyframes glow{


from{

text-shadow:

0 0 10px #22d3ee;

}


to{

text-shadow:

0 0 35px #a855f7;

}


}


</style>

""",
unsafe_allow_html=True
)




# ==========================
# LOAD MODELS
# ==========================


models={


"🚀 XG Boost":
joblib.load("models/xgb_model.pkl"),


"🌲 Random Forest":
joblib.load("models/rf_model.pkl"),


"📈 Gradient Boost":
joblib.load("models/gb_model.pkl"),


"⚡ Ada Boost":
joblib.load("models/ada_model.pkl"),


"🌳 Decision Tree":
joblib.load("models/dt_model.pkl"),


"🎯 Support Vector Machine":
joblib.load("models/svm_model.pkl"),


"👥 KNN":
joblib.load("models/knn_model.pkl"),


"📊 Naive Bayes":
joblib.load("models/nb_model.pkl")

}



model_description={


"🚀 XG Boost":
"High performance boosting algorithm",


"🌲 Random Forest":
"Multiple decision trees combined",


"📈 Gradient Boost":
"Sequential boosting technique",


"⚡ Ada Boost":
"Adaptive weak learner boosting",


"🌳 Decision Tree":
"Rule based prediction model",


"🎯 Support Vector Machine":
"Boundary based classifier",


"👥 KNN":
"Similarity based classifier",


"📊 Naive Bayes":
"Probability based classifier"

}



# ==========================
# SIDEBAR
# ==========================


st.sidebar.title("🧠 AI Engine")


model_name = st.sidebar.selectbox(

"Select ML Model",

list(models.keys())

)



st.sidebar.info(

model_description[model_name]

)



st.sidebar.success(
"🟢 AI System Online"
)


st.sidebar.caption(
"8 Machine Learning Models Loaded"
)




# ==========================
# HEADER
# ==========================


st.markdown(

"""

<div class="hero">

<h1>🤖 Churn.AI</h1>

<p>
Intelligent Customer Retention Prediction System
</p>


</div>

""",

unsafe_allow_html=True

)



st.divider()



# ==========================
# INPUT SECTION
# ==========================


left,right = st.columns(2)



with left:


    st.markdown(

    "<div class='card'>",

    unsafe_allow_html=True

    )


    st.subheader("👤 Customer Profile")


    age=st.slider(
        "Age",
        18,
        100,
        30
    )


    gender=st.selectbox(
        "Gender",
        [
            "Male",
            "Female"
        ]
    )


    tenure=st.slider(
        "Tenure",
        0,
        100,
        12
    )


    monthly=st.number_input(
        "Monthly Charges",
        0.0,
        1000.0,
        50.0
    )


    total=st.number_input(
        "Total Charges",
        0.0,
        10000.0,
        500.0
    )


    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )





with right:


    st.markdown(

    "<div class='card'>",

    unsafe_allow_html=True

    )


    st.subheader("📡 Service Details")


    contract=st.selectbox(
        "Contract Type",
        [
        "Month-to-Month",
        "One-Year",
        "Two-Year"
        ]
    )


    internet=st.selectbox(
        "Internet Service",
        [
        "DSL",
        "Fiber Optic",
        "No Internet Service"
        ]
    )


    tech=st.selectbox(
        "Tech Support",
        [
        "Yes",
        "No"
        ]
    )


    st.markdown(
    "</div>",
    unsafe_allow_html=True
    )




st.write("")



# ==========================
# PREDICT
# ==========================


if st.button(
"🚀 Analyze Customer",
use_container_width=True
):


    input_data=pd.DataFrame({


    "Age":[age],


    "Tenure":[tenure],


    "MonthlyCharges":[monthly],


    "TotalCharges":[total],


    "TechSupport":[
    1 if tech=="Yes" else 0
    ],


    "Gender_Male":[
    1 if gender=="Male" else 0
    ],


    "ContractType_One-Year":[
    1 if contract=="One-Year" else 0
    ],


    "ContractType_Two-Year":[
    1 if contract=="Two-Year" else 0
    ],


    "InternetService_Fiber Optic":[
    1 if internet=="Fiber Optic" else 0
    ],


    "InternetService_No Internet Service":[
    1 if internet=="No Internet Service" else 0
    ]



    })



    model=models[model_name]



    with st.spinner(
        "🤖 AI analyzing customer behavior..."
    ):

        time.sleep(1)

        prediction=model.predict(input_data)



    st.divider()



    st.markdown(

    "<div class='result'>",

    unsafe_allow_html=True

    )


    st.subheader(
        "Prediction Result"
    )



    if prediction[0]==1:


        st.error(
        "⚠️ HIGH CHURN RISK"
        )


        st.markdown(

        "<h1>Customer may leave service</h1>",

        unsafe_allow_html=True

        )



    else:


        st.success(
        "✅ LOW CHURN RISK"
        )


        st.markdown(

        "<h1>Customer is likely to stay</h1>",

        unsafe_allow_html=True

        )



    if hasattr(model,"predict_proba"):


        probability=model.predict_proba(input_data)[0][1]


        st.subheader(
            "Churn Probability"
        )


        st.progress(
            float(probability)
        )


        st.write(

        f"Risk Score : {probability*100:.2f}%"

        )



    st.markdown(

    "</div>",

    unsafe_allow_html=True

    )