import streamlit as st

# --- MEDICAL DATABASE (22 Diseases) ---
DISEASES_DB = {
    "Hypertension": {
        "category": "Cardiovascular",
        "overview": "A chronic condition where blood force against artery walls is consistently too high.",
        "symptoms": ["Headaches", "Shortness of breath", "Nosebleeds", "Often asymptomatic ('Silent Killer')"],
        "causes": ["High salt intake", "Obesity", "Lack of exercise", "Genetics", "Stress"],
        "prevention": ["Reduce sodium intake (<2,300mg/day)", "Exercise 150 mins/week", "Maintain healthy BMI", "Limit alcohol"],
        "screening": "Blood pressure check every 1–2 years starting at age 18."
    },
    "Coronary Artery Disease": {
        "category": "Cardiovascular",
        "overview": "Plaque buildup in the coronary arteries that reduces blood flow to the heart.",
        "symptoms": ["Chest pain (angina)", "Shortness of breath", "Fatigue", "Heart attack"],
        "causes": ["High cholesterol", "Smoking", "Diabetes", "Sedentary lifestyle"],
        "prevention": ["Adopt a Mediterranean diet", "Quit smoking", "Manage cholesterol (LDL < 100 mg/dL)", "Regular cardio"],
        "screening": "Lipid panel every 4–6 years for adults; ECG or stress testing if symptomatic."
    },
    "Heart Failure": {
        "category": "Cardiovascular",
        "overview": "A condition where the heart muscle doesn't pump blood as efficiently as it should.",
        "symptoms": ["Shortness of breath during exertion/lying down", "Swelling in legs/ankles", "Rapid heartbeat"],
        "causes": ["Uncontrolled hypertension", "Past heart attack", "Cardiomyopathy", "Valve disorders"],
        "prevention": ["Strict control of blood pressure & diabetes", "Avoid excess alcohol", "Low-sodium diet"],
        "screening": "Echocardiogram and BNP blood test evaluated by a cardiologist."
    },
    "Ischemic Stroke": {
        "category": "Cardiovascular / Neurological",
        "overview": "Occurs when blood supply to part of the brain is interrupted or drastically reduced.",
        "symptoms": ["Facial drooping", "Arm weakness", "Slurred speech", "Sudden confusion"],
        "causes": ["Blood clots", "Atherosclerosis", "Atrial fibrillation", "Hypertension"],
        "prevention": ["Control blood pressure", "Manage blood sugar", "Treat arrhythmia/AFib", "Avoid smoking"],
        "screening": "Carotid ultrasound, brain CT/MRI, and routine vascular checkups."
    },
    "Type 2 Diabetes": {
        "category": "Metabolic",
        "overview": "A metabolic disorder characterized by high blood sugar due to insulin resistance.",
        "symptoms": ["Increased thirst", "Frequent urination", "Unexplained weight loss", "Blurred vision"],
        "causes": ["Insulin resistance", "Obesity", "Inactivity", "Genetic predisposition"],
        "prevention": ["Low-glycemic index diet", "30 minutes daily activity", "Weight loss (5-7% of body weight)"],
        "screening": "Fasting blood glucose or HbA1c test annually starting at age 35."
    },
    "Hypothyroidism": {
        "category": "Endocrine",
        "overview": "Underactive thyroid gland failing to produce sufficient thyroid hormone.",
        "symptoms": ["Fatigue", "Weight gain", "Cold intolerance", "Dry skin", "Depression"],
        "causes": ["Hashimoto's thyroiditis (autoimmune)", "Thyroid surgery", "Radiation therapy"],
        "prevention": ["Ensure adequate iodine intake", "Early diagnosis via routine blood tests"],
        "screening": "Serum TSH (Thyroid-Stimulating Hormone) blood test."
    },
    "Fatty Liver Disease (NAFLD)": {
        "category": "Metabolic",
        "overview": "Excess fat buildup in liver cells not caused by heavy alcohol consumption.",
        "symptoms": ["Fatigue", "Pain in upper right abdomen", "Often asymptomatic"],
        "causes": ["Obesity", "Insulin resistance", "High intake of refined sugars/fructose"],
        "prevention": ["Avoid sugary beverages", "Regular resistance & aerobic training", "Weight management"],
        "screening": "Liver enzyme blood tests (ALT/AST) and abdominal ultrasound."
    },
    "Asthma": {
        "category": "Respiratory",
        "overview": "Chronic condition where airways narrow, swell, and produce extra mucus.",
        "symptoms": ["Wheezing", "Coughing (especially at night)", "Chest tightness", "Shortness of breath"],
        "causes": ["Genetic triggers", "Allergens (pollen, dust mites)", "Respiratory infections", "Cold air"],
        "prevention": ["Identify/avoid environmental triggers", "Annual flu vaccine", "Use prescribed preventive inhalers"],
        "screening": "Spirometry / Pulmonary Function Testing (PFT)."
    },
    "COPD": {
        "category": "Respiratory",
        "overview": "Progressive inflammatory lung disease causing obstructed airflow from the lungs.",
        "symptoms": ["Chronic cough with mucus", "Shortness of breath", "Frequent respiratory infections"],
        "causes": ["Long-term cigarette smoking", "Air pollution exposure", "Chemical fumes"],
        "prevention": ["Zero tobacco smoking", "Use respirator masks in toxic environments", "Pneumococcal vaccination"],
        "screening": "Spirometry and chest X-rays."
    },
    "Pneumonia": {
        "category": "Respiratory Infection",
        "overview": "Infection that inflames air sacs in one or both lungs, which may fill with fluid or pus.",
        "symptoms": ["High fever/chills", "Cough with phlegm", "Chest pain when breathing", "Shortness of breath"],
        "causes": ["Bacteria (Streptococcus pneumoniae)", "Viruses (Flu, COVID-19)", "Fungi"],
        "prevention": ["Pneumococcal and Influenza vaccines", "Good hand hygiene", "Avoid smoking"],
        "screening": "Chest X-ray, sputum culture, and pulse oximetry."
    },
    "Tuberculosis (TB)": {
        "category": "Infectious",
        "overview": "Potentially serious infectious bacterial disease mainly affecting the lungs.",
        "symptoms": ["Cough lasting 3+ weeks", "Coughing up blood", "Night sweats", "Unintentional weight loss"],
        "causes": ["Mycobacterium tuberculosis spread via airborne droplets"],
        "prevention": ["BCG vaccine in endemic areas", "Proper ventilation", "Treating latent TB infections"],
        "screening": "Mantoux Tuberculin Skin Test (TST) or IGRA Blood Test."
    },
    "Malaria": {
        "category": "Infectious",
        "overview": "Mosquito-borne disease caused by a microscopic parasite.",
        "symptoms": ["High fever", "Shaking chills", "Headache", "Nausea/vomiting", "Muscle pain"],
        "causes": ["Plasmodium parasite transmitted via Anopheles mosquito bite"],
        "prevention": ["Insecticide-treated bed nets", "Prophylactic antimalarial medication", "Insect repellent (DEET)"],
        "screening": "Rapid Diagnostic Test (RDT) or thick/thin blood smear microscopic exam."
    },
    "Hepatitis B": {
        "category": "Infectious / Liver",
        "overview": "Serious liver infection caused by the Hepatitis B virus (HBV).",
        "symptoms": ["Jaundice (yellow eyes/skin)", "Dark urine", "Abdominal pain", "Fatigue"],
        "causes": ["Exposure to infected blood or bodily fluids", "Unsafe injections", "Mother to child"],
        "prevention": ["Hepatitis B vaccination (3-dose series)", "Safe medical practices", "Avoid sharing personal items"],
        "screening": "HBsAg (Hepatitis B surface antigen) blood panel."
    },
    "Lyme Disease": {
        "category": "Infectious",
        "overview": "Bacterial illness transmitted by infected blacklegged ticks.",
        "symptoms": ["'Bullseye' rash (Erythema migrans)", "Fever", "Joint pain", "Neurological issues if untreated"],
        "causes": ["Borrelia burgdorferi bacterium via tick bite"],
        "prevention": ["Wear long sleeves/pants in wooded areas", "Use DEET/Permethrin", "Check body for ticks promptly"],
        "screening": "Two-tiered antibody blood testing (ELISA followed by Western Blot)."
    },
    "Alzheimer's Disease": {
        "category": "Neurological",
        "overview": "Progressive neurodegenerative disease causing brain cells to waste away and die.",
        "symptoms": ["Memory loss affecting daily life", "Disorientation", "Language difficulties", "Behavioral changes"],
        "causes": ["Amyloid plaque & tau tangle accumulation", "Genetics (APOE-e4)", "Age"],
        "prevention": ["Regular cognitive exercises", "Social engagement", "Cardiovascular health maintenance"],
        "screening": "Cognitive assessment tests (MMSE), brain MRI/PET scans."
    },
    "Parkinson's Disease": {
        "category": "Neurological",
        "overview": "Central nervous system disorder affecting movement and dopamine-producing neurons.",
        "symptoms": ["Resting tremor", "Bradykinesia (slowed movement)", "Muscle rigidity", "Postural instability"],
        "causes": ["Loss of dopamine neurons in substantia nigra", "Genetic mutation", "Environmental toxins"],
        "prevention": ["Regular high-intensity aerobic exercise", "Diet rich in antioxidants"],
        "screening": "Clinical evaluation by a neurologist; DaTscan imaging."
    },
    "Major Depressive Disorder": {
        "category": "Mental Health",
        "overview": "A mood disorder causing persistent feelings of sadness and loss of interest.",
        "symptoms": ["Persistent low mood", "Anhedonia", "Changes in sleep/appetite", "Fatigue", "Low concentration"],
        "causes": ["Neurochemical imbalances", "Genetic vulnerability", "Chronic stress or trauma"],
        "prevention": ["Building strong social support systems", "Regular physical activity", "Stress management"],
        "screening": "PHQ-9 (Patient Health Questionnaire) screening tool."
    },
    "Osteoporosis": {
        "category": "Musculoskeletal",
        "overview": "Condition where bones become weak and brittle, increasing fracture risk.",
        "symptoms": ["Bone fractures from minor falls", "Loss of height over time", "Stooped posture"],
        "causes": ["Aging", "Estrogen decline in post-menopause", "Calcium & Vitamin D deficiency"],
        "prevention": ["Adequate daily Calcium (1000-1200mg) and Vitamin D", "Weight-bearing exercises"],
        "screening": "DEXA (Dual-energy X-ray absorptiometry) bone density scan."
    },
    "Osteoarthritis": {
        "category": "Musculoskeletal",
        "overview": "Degenerative joint disease caused by breakdown of joint cartilage.",
        "symptoms": ["Joint pain and stiffness", "Loss of flexibility", "Grating sensation during movement"],
        "causes": ["Joint wear and tear", "Prior joint injuries", "Obesity"],
        "prevention": ["Maintain a healthy weight", "Low-impact exercises (swimming/cycling)", "Protect joints from injury"],
        "screening": "Joint X-rays and clinical physical examination."
    },
    "Chronic Kidney Disease": {
        "category": "Renal",
        "overview": "Gradual loss of kidney function over time, leading to dangerous fluid/waste buildup.",
        "symptoms": ["Swollen ankles/feet", "Fatigue", "Changes in urination frequency", "Nausea"],
        "causes": ["Uncontrolled diabetes", "Long-term hypertension", "Glomerulonephritis"],
        "prevention": ["Tight blood sugar & pressure control", "Avoid long-term overuse of NSAIDs (e.g., ibuprofen)"],
        "screening": "eGFR (Estimated Glomerular Filtration Rate) blood test and urine albumin test."
    },
    "Colorectal Cancer": {
        "category": "Oncology",
        "overview": "Cancer starting in the colon or rectum, usually developing from precancerous polyps.",
        "symptoms": ["Changes in bowel habits", "Blood in stool", "Unexplained weight loss", "Abdominal cramping"],
        "causes": ["Age", "Family history", "Diet high in processed meats", "Smoking & alcohol"],
        "prevention": ["High-fiber diet", "Limit red/processed meats", "Regular physical activity"],
        "screening": "Colonoscopy starting at age 45 (or earlier with family history)."
    },
    "Breast Cancer": {
        "category": "Oncology",
        "overview": "Cancer that forms in the tissue and cells of the breasts.",
        "symptoms": ["Painless breast lump", "Changes in breast shape/size", "Skin dimpling", "Nipple discharge"],
        "causes": ["BRCA1/BRCA2 gene mutations", "Hormonal factors", "Increasing age", "Alcohol consumption"],
        "prevention": ["Maintain healthy weight", "Limit hormone replacement therapy", "Limit alcohol"],
        "screening": "Annual or biennial Screening Mammogram starting at age 40."
    }
}

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="HealthNav AI - Medical Dashboard",
    page_icon="⚕️",
    layout="wide"
)

# --- STYLING (dark theme matching original desktop app) ---
st.markdown("""
<style>
    .stApp { background-color: #1e1e2e; }
    section[data-testid="stSidebar"] { background-color: #181825; }
    h1, h2, h3 { color: #89b4fa; }
    .category-badge {
        display: inline-block;
        background-color: #181825;
        color: #a6e3a1;
        font-weight: bold;
        font-size: 0.8rem;
        padding: 4px 10px;
        border-radius: 4px;
        margin-bottom: 12px;
    }
    .section-header {
        color: #f9e2af;
        font-weight: bold;
        font-size: 1.05rem;
        margin-top: 18px;
        margin-bottom: 6px;
    }
    .bullet-item { color: #a6adc8; margin-left: 10px; }
    .overview-text, .screening-text { color: #cdd6f4; }
    .disclaimer {
        color: #a6adc8;
        font-size: 0.8rem;
        font-style: italic;
        border-top: 1px solid #313244;
        margin-top: 25px;
        padding-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("## ⚕️ HealthNav Medical Assistant")
st.caption("Educational Medical AI Explorer — search by disease name, category, or symptom")

# --- SIDEBAR: SEARCH + DISEASE LIST ---
with st.sidebar:
    st.markdown("**SEARCH DISEASES / SYMPTOMS**")
    query = st.text_input("Search", label_visibility="collapsed", placeholder="e.g. cough, diabetes, fatigue...")

    def filter_diseases(q):
        if not q:
            return list(DISEASES_DB.keys())
        q = q.lower()
        results = []
        for name, data in DISEASES_DB.items():
            in_symptoms = any(q in s.lower() for s in data["symptoms"])
            if q in name.lower() or q in data["category"].lower() or in_symptoms:
                results.append(name)
        return results

    filtered_names = filter_diseases(query)
    st.markdown(f"**DISEASE INDEX ({len(filtered_names)})**")

    if not filtered_names:
        st.info("No matches found.")
        selected_disease = None
    else:
        selected_disease = st.radio(
            "Diseases", filtered_names, label_visibility="collapsed"
        )

# --- MAIN DETAIL VIEW ---
if selected_disease:
    data = DISEASES_DB[selected_disease]

    st.markdown(f"### {selected_disease}")
    st.markdown(f"<span class='category-badge'>{data['category'].upper()}</span>", unsafe_allow_html=True)

    st.markdown("<div class='section-header'>OVERVIEW</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='overview-text'>{data['overview']}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-header'>COMMON SYMPTOMS</div>", unsafe_allow_html=True)
    for item in data["symptoms"]:
        st.markdown(f"<div class='bullet-item'>• {item}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-header'>CAUSES & RISK FACTORS</div>", unsafe_allow_html=True)
    for item in data["causes"]:
        st.markdown(f"<div class='bullet-item'>• {item}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-header'>PREVENTION STRATEGIES</div>", unsafe_allow_html=True)
    for item in data["prevention"]:
        st.markdown(f"<div class='bullet-item'>• {item}</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-header'>RECOMMENDED SCREENING</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='screening-text'>{data['screening']}</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='disclaimer'>⚠️ This tool is for educational purposes only and is not a substitute "
    "for professional medical diagnosis. Please consult a licensed healthcare provider.</div>",
    unsafe_allow_html=True
)
