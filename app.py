import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Prime Supps Architect", page_icon="💪", layout="wide")

# 2. UPDATED Smart Link Database
# Note: I am using 'collections/all' as a safe backup so you don't get 404s.
PRODUCTS = {
    "Muscle": "https://primesuppsnation.com/collections/all", 
    "Fat": "https://primesuppsnation.com/collections/all",    
    "Focus": "https://primesuppsnation.com/collections/all"   
}

# 3. Bilingual Content Dictionary
content = {
    "English": {
        "title": "🛡️ Prime Supps Architect",
        "subtitle": "Professional Supplement & Nutrition Automation",
        "gender_label": "Select Gender",
        "goal_label": "Select Your Goal",
        "weight_label": "Current Weight (lbs)",
        "button": "Generate My Program",
        "buy_button": "🛒 Buy This Custom Stack Now",
        "muscle": "Build Muscle",
        "fat": "Burn Fat",
        "focus": "Mental Focus",
        "tips": "💡 Professional Timing & Tips",
        "macros": "📊 Your Macros",
        "supps": "💊 Supplement Program"
    },
    "Español": {
        "title": "🛡️ Arquitecto Prime Supps",
        "subtitle": "Automatización Profesional de Nutrición y Suplementos",
        "gender_label": "Seleccionar Género",
        "goal_label": "Seleccionar Objetivo",
        "weight_label": "Peso Actual (lbs)",
        "button": "Generar Mi Programa",
        "buy_button": "🛒 Comprar este Combo Ahora",
        "muscle": "Ganar Músculo",
        "fat": "Quemar Grasa",
        "focus": "Enfoque Mental",
        "tips": "💡 Tiempos y Consejos Profesionales",
        "macros": "📊 Tus Macros",
        "supps": "💊 Programa de Suplementos"
    }
}

# 4. Sidebar Language Selector
lang = st.sidebar.selectbox("Language / Idioma", ["English", "Español"])
t = content[lang]

# 5. UI Header
st.title(t["title"])
st.write(t["subtitle"])

# 6. User Inputs
col1, col2 = st.columns(2)
with col1:
    gender = st.radio(t["gender_label"], ["👨 Man / Hombre", "👩 Woman / Mujer"], horizontal=True)
    weight = st.number_input(t["weight_label"], 100, 400, 180)
with col2:
    goal = st.selectbox(t["goal_label"], [t["muscle"], t["fat"], t["focus"]])

# 7. Execution Engine
if st.button(t["button"]):
    st.divider()
    
    # Macro Logic
    prot_mult = 1.2 if "👨" in gender else 1.0
    protein = weight * prot_mult
    calories = weight * 17 if t["muscle"] in goal else weight * 13

    # Results Display
    res1, res2 = st.columns(2)
    with res1:
        st.header(t["macros"])
        st.metric("Protein / Proteína", f"{int(protein)}g")
        st.metric("Calories / Calorías", f"{int(calories)} kcal")
        
    with res2:
        st.header(t["supps"])
        
        if t["muscle"] in goal:
            st.write("**1. Creatine Monohydrate:** 5g daily. \n*Timing: Post-workout.*")
            st.write("**2. Whey Protein Isolate:** 1-2 scoops. \n*Timing: Post-training.*")
            target_url = PRODUCTS["Muscle"]
        elif t["fat"] in goal:
            st.write("**1. Advanced Fat Burner:** 1 cap. \n*Timing: 20 mins before cardio.*")
            st.write("**2. BCAA Recovery:** 1 scoop. \n*Timing: During training.*")
            target_url = PRODUCTS["Fat"]
        else:
            st.write("**1. Prime Focus Nootropic:** 2 caps. \n*Timing: 30 mins before work.*")
            st.write("**2. Omega-3 Fish Oil:** 2000mg. \n*Timing: With lunch.*")
            target_url = PRODUCTS["Focus"]

    # 8. THE SMART LINK BUTTON
    st.divider()
    st.markdown(f"""
        <a href="{target_url}" target="_blank" style="text-decoration: none;">
            <div style="
                background-color: #ff4b4b;
                color: white;
                padding: 22px;
                text-align: center;
                border-radius: 12px;
                font-size: 22px;
                font-weight: bold;
                box-shadow: 0px 6px 15px rgba(255, 75, 75, 0.3);">
                {t['buy_button']}
            </div>
        </a>
    """, unsafe_allow_html=True)
    
    st.subheader(t["tips"])
    if lang == "English":
        st.info("✅ **Hydration:** Aim for 3-4 liters of water daily.\n\n"
                "✅ **Recovery:** Ensure 7-8 hours of sleep for supplement efficiency.")
    else:
        st.info("✅ **Hidratación:** Bebe de 3 a 4 litros de agua al día.\n\n"
                "✅ **Recuperación:** Duerme de 7 a 8 horas para optimizar los suplementos.")
    
    st.balloons()
