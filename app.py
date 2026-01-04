import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Fitness Fuel Finder", page_icon="💪")

# 2. DESIGN: Fixed CSS Injection
# The error was caused by 'unsafe_allow_index'; 'unsafe_allow_html' is the correct term.
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    h1 { color: #ff4b4b; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Fitness Fuel Finder")
st.subheader("Get your custom supplement & macro plan")

# 3. INPUTS
name = st.text_input("First Name")
goal = st.selectbox("What is your main goal?", ["Build Muscle", "Burn Fat", "Mental Focus"])
weight = st.number_input("Weight (lbs)", min_value=100, max_value=400, value=180)

# 4. BUTTON & LOGIC
if st.button("Generate My Plan"):
    # Simple logic: 1g protein per lb of bodyweight
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
            st.write("- **Creatine Monohydrate** (5g)")
            st.write("- **Whey Protein Isolate**")
        elif goal == "Burn Fat":
            st.write("- **L-Carnitine**")
            st.write("- **Green Tea Extract**")
        else:
            st.write("- **Ashwagandha**")
            st.write("- **Magnesium Glycinate**")

    st.divider()
    st.info("💡 **Founder Note:** Link these recommendations to your supplement store to drive sales.")
