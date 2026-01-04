import streamlit as st

st.set_page_config(page_title="Fitness Fuel Finder", page_icon="💪")

# DESIGN: Custom CSS to make it look professional
# CHANGE THIS LINE (Line 6 or 7):
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    h1 { color: #ff4b4b; text-align: center; }
    </style>
    """, unsafe_allow_html=True) # I fixed 'index' to 'html' here

st.title("🛡️ Fitness Fuel Finder")
st.subheader("Get your custom supplement & macro plan")

# INPUTS
name = st.text_input("First Name")
goal = st.selectbox("What is your main goal?", ["Build Muscle", "Burn Fat", "Mental Focus"])
weight = st.number_input("Weight (lbs)", min_value=100, max_value=400, value=180)

if st.button("Generate My Plan"):
    # LOGIC (This is the 'Work' the code does)
    protein = weight * 1.0
    
    st.success(f"Okay {name}, here is your strategy:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 🥩 Daily Macros")
        st.write(f"- **Protein:** {protein}g")
        st.write(f"- **Calories:** {weight * 15} kcal")
    
    with col2:
        st.write("### 💊 Recommended Stack")
        if goal == "Build Muscle":
            st.write("- Creatine Monohydrate (5g)")
            st.write("- Whey Protein Isolate")
        elif goal == "Burn Fat":
            st.write("- L-Carnitine")
            st.write("- Green Tea Extract")
        else:
            st.write("- Ashwagandha")
            st.write("- Magnesium Glycinate")

    st.info("💡 **Marketing Tip:** You can link these products directly to your Shopify store!")
