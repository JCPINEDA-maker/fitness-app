import streamlit as st

# 1. Page Setup
st.set_page_config(page_title="Pro Fuel System", page_icon="🧪", layout="wide")

# 2. Language Database (The "Dictionary")
content = {
    "English": {
        "title": "🛡️ Pro Supplement Architect",
        "subtitle": "Professional Nutrition & Supplement Programming",
        "select_lang": "Choose Language",
        "gender_label": "Select Gender",
        "goal_label": "Select Your Goal",
        "weight_label": "Current Weight (lbs)",
        "button": "Generate Professional Program",
        "tips_title": "💡 Nutrition & Timing Tips",
        "muscle": "Build Muscle",
        "fat": "Burn Fat",
        "focus": "Mental Performance"
    },
    "Español": {
        "title": "🛡️ Arquitecto de Suplementos Pro",
        "subtitle": "Programación Profesional de Nutrición y Suplementos",
        "select_lang": "Seleccionar Idioma",
        "gender_label": "Seleccionar Género",
        "goal_label": "Seleccionar Objetivo",
        "weight_label": "Peso Actual (lbs)",
        "button": "Generar Programa Profesional",
        "tips_title": "💡 Consejos de Nutrición y Tiempos",
        "muscle": "Ganar Músculo",
        "fat": "Quemar Grasa",
        "focus": "Rendimiento Mental"
    }
}

# 3. Sidebar for Language Toggle
lang = st.sidebar.selectbox("Language / Idioma", ["English", "Español"])
t = content[lang]

# 4. Header Section
st.title(t["title"])
st.write(t["subtitle"])

# 5. Professional Inputs
col1, col2 = st.columns(2)

with col1:
    # GENDER SELECTION WITH ICONS
    gender = st.radio(t["gender_label"], ["👨 Man / Hombre", "👩 Woman / Mujer"], horizontal=True)
    weight = st.number_input(t["weight_label"], 100, 400, 180)

with col2:
    goal = st.selectbox(t["goal_label"], [t["muscle"], t["fat"], t["focus"]])

# 6. The Logic Engine
if st.button(t["button"]):
    st.divider()
    
    # Calculate Macros based on Gender & Weight
    # Men get slightly more protein for muscle synthesis in this logic
    if "👨" in gender:
        protein = weight * 1.2 if t["muscle"] in goal else weight * 1.0
    else:
        protein = weight * 1.0 if t["muscle"] in goal else weight * 0.8
        
    calories = weight * 16 if t["muscle"] in goal else weight * 12
    
    # Results Display
    res1, res2 = st.columns(2)
    
    with res1:
        st.header("📊 Macros")
        st.metric("Protein / Proteína", f"{int(protein)}g")
        st.metric("Daily Calories / Calorías", f"{int(calories)} kcal")
        
    with res2:
        st.header("💊 Supplement Program")
        # Logic for Supplement recommendations
        if t["muscle"] in goal:
            st.write("**1. Creatine Monohydrate:** 5g daily. \n*Timing: Post-workout.*")
            st.write("**2. Whey Protein:** 1-2 scoops. \n*Timing: Upon waking or post-training.*")
        elif t["fat"] in goal:
            st.write("**1. L-Carnitine:** 2g. \n*Timing: 30 mins before cardio.*")
            st.write("**2. Multivitamin:** 1 serving. \n*Timing: With breakfast.*")
        else:
            st.write("**1. Omega-3:** 2000mg. \n*Timing: With largest meal.*")
            st.write("**2. Magnesium:** 400mg. \n*Timing: 30 mins before sleep.*")

    # 7. Professional Tips
    st.subheader(t["tips_title"])
    if lang == "English":
        st.info("✅ **Hydration:** Drink 1oz of water per lb of body weight.\n\n"
                "✅ **Timing:** Eat your largest carbohydrate meal 2 hours before training.")
    else:
        st.info("✅ **Hidratación:** Bebe 1oz de agua por cada libra de peso corporal.\n\n"
                "✅ **Tiempos:** Consume tu comida más alta en carbohidratos 2 horas antes de entrenar.")
    
    st.balloons()
