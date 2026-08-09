import streamlit as st

# --- MEDICAL DATABASE (22 Diseases, with medicines added) ---
# Medicines are listed as commonly used drug CLASSES with a familiar
# example in brackets -- never doses or personal instructions.

DISEASES_DB = {
    "Hypertension": {
        "category": "Cardiovascular",
        "overview": "A chronic condition where blood force against artery walls is consistently too high.",
        "symptoms": ["Headaches", "Shortness of breath", "Nosebleeds", "Often asymptomatic ('Silent Killer')"],
        "causes": ["High salt intake", "Obesity", "Lack of exercise", "Genetics", "Stress"],
        "medicines": ["ACE inhibitors (e.g., lisinopril)", "ARBs (e.g., losartan)", "Diuretics / water pills (e.g., hydrochlorothiazide)", "Calcium channel blockers (e.g., amlodipine)", "Beta blockers"],
        "prevention": ["Reduce sodium intake (<2,300mg/day)", "Exercise 150 mins/week", "Maintain healthy BMI", "Limit alcohol"],
        "screening": "Blood pressure check every 1-2 years starting at age 18."
    },
    "Coronary Artery Disease": {
        "category": "Cardiovascular",
        "overview": "Plaque buildup in the coronary arteries that reduces blood flow to the heart.",
        "symptoms": ["Chest pain (angina)", "Shortness of breath", "Fatigue", "Heart attack"],
        "causes": ["High cholesterol", "Smoking", "Diabetes", "Sedentary lifestyle"],
        "medicines": ["Statins (e.g., atorvastatin)", "Low-dose aspirin", "Beta blockers", "Nitrates for chest pain"],
        "prevention": ["Adopt a Mediterranean diet", "Quit smoking", "Manage cholesterol (LDL < 100 mg/dL)", "Regular cardio"],
        "screening": "Lipid panel every 4-6 years for adults; ECG or stress testing if symptomatic."
    },
    "Heart Failure": {
        "category": "Cardiovascular",
        "overview": "A condition where the heart muscle doesn't pump blood as efficiently as it should.",
        "symptoms": ["Shortness of breath during exertion/lying down", "Swelling in legs/ankles", "Rapid heartbeat"],
        "causes": ["Uncontrolled hypertension", "Past heart attack", "Cardiomyopathy", "Valve disorders"],
        "medicines": ["ACE inhibitors or ARBs", "Beta blockers", "Diuretics / water pills", "SGLT2 inhibitors"],
        "prevention": ["Strict control of blood pressure & diabetes", "Avoid excess alcohol", "Low-sodium diet"],
        "screening": "Echocardiogram and BNP blood test evaluated by a cardiologist."
    },
    "Ischemic Stroke": {
        "category": "Cardiovascular / Neurological",
        "overview": "Occurs when blood supply to part of the brain is interrupted or drastically reduced.",
        "symptoms": ["Facial drooping", "Arm weakness", "Slurred speech", "Sudden confusion"],
        "causes": ["Blood clots", "Atherosclerosis", "Atrial fibrillation", "Hypertension"],
        "medicines": ["Aspirin or clopidogrel", "Blood thinners for AFib (e.g., a DOAC or warfarin)", "Statins", "Blood pressure medicine"],
        "prevention": ["Control blood pressure", "Manage blood sugar", "Treat arrhythmia/AFib", "Avoid smoking"],
        "screening": "Carotid ultrasound, brain CT/MRI, and routine vascular checkups."
    },
    "Type 2 Diabetes": {
        "category": "Metabolic",
        "overview": "A metabolic disorder characterized by high blood sugar due to insulin resistance.",
        "symptoms": ["Increased thirst", "Frequent urination", "Unexplained weight loss", "Blurred vision"],
        "causes": ["Insulin resistance", "Obesity", "Inactivity", "Genetic predisposition"],
        "medicines": ["Metformin (usually first-line)", "SGLT2 inhibitors", "GLP-1 receptor agonists", "Insulin, if prescribed"],
        "prevention": ["Low-glycemic index diet", "30 minutes daily activity", "Weight loss (5-7% of body weight)"],
        "screening": "Fasting blood glucose or HbA1c test annually starting at age 35."
    },
    "Hypothyroidism": {
        "category": "Endocrine",
        "overview": "Underactive thyroid gland failing to produce sufficient thyroid hormone.",
        "symptoms": ["Fatigue", "Weight gain", "Cold intolerance", "Dry skin", "Depression"],
        "causes": ["Hashimoto's thyroiditis (autoimmune)", "Thyroid surgery", "Radiation therapy"],
        "medicines": ["Levothyroxine (daily thyroid hormone replacement)"],
        "prevention": ["Ensure adequate iodine intake", "Early diagnosis via routine blood tests"],
        "screening": "Serum TSH (Thyroid-Stimulating Hormone) blood test."
    },
    "Fatty Liver Disease (NAFLD)": {
        "category": "Metabolic",
        "overview": "Excess fat buildup in liver cells not caused by heavy alcohol consumption.",
        "symptoms": ["Fatigue", "Pain in upper right abdomen", "Often asymptomatic"],
        "causes": ["Obesity", "Insulin resistance", "High intake of refined sugars/fructose"],
        "medicines": ["No drug directly cures NAFLD", "Vitamin E or pioglitazone in select cases", "Treating cholesterol/diabetes helps protect the liver"],
        "prevention": ["Avoid sugary beverages", "Regular resistance & aerobic training", "Weight management"],
        "screening": "Liver enzyme blood tests (ALT/AST) and abdominal ultrasound."
    },
    "Asthma": {
        "category": "Respiratory",
        "overview": "Chronic condition where airways narrow, swell, and produce extra mucus.",
        "symptoms": ["Wheezing", "Coughing (especially at night)", "Chest tightness", "Shortness of breath"],
        "causes": ["Genetic triggers", "Allergens (pollen, dust mites)", "Respiratory infections", "Cold air"],
        "medicines": ["Reliever inhaler (e.g., albuterol)", "Inhaled corticosteroids (preventer)", "Long-acting beta agonists", "Leukotriene modifiers"],
        "prevention": ["Identify/avoid environmental triggers", "Annual flu vaccine", "Use prescribed preventive inhalers"],
        "screening": "Spirometry / Pulmonary Function Testing (PFT)."
    },
    "COPD": {
        "category": "Respiratory",
        "overview": "Progressive inflammatory lung disease causing obstructed airflow from the lungs.",
        "symptoms": ["Chronic cough with mucus", "Shortness of breath", "Frequent respiratory infections"],
        "causes": ["Long-term cigarette smoking", "Air pollution exposure", "Chemical fumes"],
        "medicines": ["Bronchodilator inhalers", "Combination inhalers (steroid + bronchodilator)", "Antibiotics during a flare-up"],
        "prevention": ["Zero tobacco smoking", "Use respirator masks in toxic environments", "Pneumococcal vaccination"],
        "screening": "Spirometry and chest X-rays."
    },
    "Pneumonia": {
        "category": "Respiratory Infection",
        "overview": "Infection that inflames air sacs in one or both lungs, which may fill with fluid or pus.",
        "symptoms": ["High fever/chills", "Cough with phlegm", "Chest pain when breathing", "Shortness of breath"],
        "causes": ["Bacteria (Streptococcus pneumoniae)", "Viruses (Flu, COVID-19)", "Fungi"],
        "medicines": ["Antibiotics (bacterial cases)", "Antivirals (viral cases)", "Fever/pain relief (e.g., paracetamol)"],
        "prevention": ["Pneumococcal and Influenza vaccines", "Good hand hygiene", "Avoid smoking"],
        "screening": "Chest X-ray, sputum culture, and pulse oximetry."
    },
    "Tuberculosis (TB)": {
        "category": "Infectious",
        "overview": "Potentially serious infectious bacterial disease mainly affecting the lungs.",
        "symptoms": ["Cough lasting 3+ weeks", "Coughing up blood", "Night sweats", "Unintentional weight loss"],
        "causes": ["Mycobacterium tuberculosis spread via airborne droplets"],
        "medicines": ["Combination antibiotics (isoniazid, rifampin, ethambutol, pyrazinamide) for 6+ months, set by your doctor"],
        "prevention": ["BCG vaccine in endemic areas", "Proper ventilation", "Treating latent TB infections"],
        "screening": "Mantoux Tuberculin Skin Test (TST) or IGRA Blood Test."
    },
    "Malaria": {
        "category": "Infectious",
        "overview": "Mosquito-borne disease caused by a microscopic parasite.",
        "symptoms": ["High fever", "Shaking chills", "Headache", "Nausea/vomiting", "Muscle pain"],
        "causes": ["Plasmodium parasite transmitted via Anopheles mosquito bite"],
        "medicines": ["Antimalarial medicine chosen by a doctor based on the parasite type and region", "Preventive antimalarial tablets before travel to risk areas"],
        "prevention": ["Insecticide-treated bed nets", "Prophylactic antimalarial medication", "Insect repellent (DEET)"],
        "screening": "Rapid Diagnostic Test (RDT) or thick/thin blood smear microscopic exam."
    },
    "Hepatitis B": {
        "category": "Infectious / Liver",
        "overview": "Serious liver infection caused by the Hepatitis B virus (HBV).",
        "symptoms": ["Jaundice (yellow eyes/skin)", "Dark urine", "Abdominal pain", "Fatigue"],
        "causes": ["Exposure to infected blood or bodily fluids", "Unsafe injections", "Mother to child"],
        "medicines": ["Antivirals for chronic cases needing treatment (e.g., tenofovir, entecavir)"],
        "prevention": ["Hepatitis B vaccination (3-dose series)", "Safe medical practices", "Avoid sharing personal items"],
        "screening": "HBsAg (Hepatitis B surface antigen) blood panel."
    },
    "Lyme Disease": {
        "category": "Infectious",
        "overview": "Bacterial illness transmitted by infected blacklegged ticks.",
        "symptoms": ["'Bullseye' rash (Erythema migrans)", "Fever", "Joint pain", "Neurological issues if untreated"],
        "causes": ["Borrelia burgdorferi bacterium via tick bite"],
        "medicines": ["Antibiotics such as doxycycline or amoxicillin, usually for a few weeks"],
        "prevention": ["Wear long sleeves/pants in wooded areas", "Use DEET/Permethrin", "Check body for ticks promptly"],
        "screening": "Two-tiered antibody blood testing (ELISA followed by Western Blot)."
    },
    "Alzheimer's Disease": {
        "category": "Neurological",
        "overview": "Progressive neurodegenerative disease causing brain cells to waste away and die.",
        "symptoms": ["Memory loss affecting daily life", "Disorientation", "Language difficulties", "Behavioral changes"],
        "causes": ["Amyloid plaque & tau tangle accumulation", "Genetics (APOE-e4)", "Age"],
        "medicines": ["Cholinesterase inhibitors (e.g., donepezil)", "Memantine, sometimes used alongside them"],
        "prevention": ["Regular cognitive exercises", "Social engagement", "Cardiovascular health maintenance"],
        "screening": "Cognitive assessment tests (MMSE), brain MRI/PET scans."
    },
    "Parkinson's Disease": {
        "category": "Neurological",
        "overview": "Central nervous system disorder affecting movement and dopamine-producing neurons.",
        "symptoms": ["Resting tremor", "Bradykinesia (slowed movement)", "Muscle rigidity", "Postural instability"],
        "causes": ["Loss of dopamine neurons in substantia nigra", "Genetic mutation", "Environmental toxins"],
        "medicines": ["Levodopa combined with carbidopa (main treatment)", "Dopamine agonists", "MAO-B inhibitors"],
        "prevention": ["Regular high-intensity aerobic exercise", "Diet rich in antioxidants"],
        "screening": "Clinical evaluation by a neurologist; DaTscan imaging."
    },
    "Major Depressive Disorder": {
        "category": "Mental Health",
        "overview": "A mood disorder causing persistent feelings of sadness and loss of interest.",
        "symptoms": ["Persistent low mood", "Anhedonia", "Changes in sleep/appetite", "Fatigue", "Low concentration"],
        "causes": ["Neurochemical imbalances", "Genetic vulnerability", "Chronic stress or trauma"],
        "medicines": ["SSRIs (e.g., sertraline)", "SNRIs", "Other antidepressants -- often combined with talking therapy"],
        "prevention": ["Building strong social support systems", "Regular physical activity", "Stress management"],
        "screening": "PHQ-9 (Patient Health Questionnaire) screening tool."
    },
    "Osteoporosis": {
        "category": "Musculoskeletal",
        "overview": "Condition where bones become weak and brittle, increasing fracture risk.",
        "symptoms": ["Bone fractures from minor falls", "Loss of height over time", "Stooped posture"],
        "causes": ["Aging", "Estrogen decline in post-menopause", "Calcium & Vitamin D deficiency"],
        "medicines": ["Bisphosphonates (e.g., alendronate)", "Calcium and vitamin D supplements", "Other bone-strengthening medicines as prescribed"],
        "prevention": ["Adequate daily Calcium (1000-1200mg) and Vitamin D", "Weight-bearing exercises"],
        "screening": "DEXA (Dual-energy X-ray absorptiometry) bone density scan."
    },
    "Osteoarthritis": {
        "category": "Musculoskeletal",
        "overview": "Degenerative joint disease caused by breakdown of joint cartilage.",
        "symptoms": ["Joint pain and stiffness", "Loss of flexibility", "Grating sensation during movement"],
        "causes": ["Joint wear and tear", "Prior joint injuries", "Obesity"],
        "medicines": ["Paracetamol for pain", "NSAIDs (e.g., ibuprofen)", "Topical gels", "Steroid injections for bad flare-ups"],
        "prevention": ["Maintain a healthy weight", "Low-impact exercises (swimming/cycling)", "Protect joints from injury"],
        "screening": "Joint X-rays and clinical physical examination."
    },
    "Chronic Kidney Disease": {
        "category": "Renal",
        "overview": "Gradual loss of kidney function over time, leading to dangerous fluid/waste buildup.",
        "symptoms": ["Swollen ankles/feet", "Fatigue", "Changes in urination frequency", "Nausea"],
        "causes": ["Uncontrolled diabetes", "Long-term hypertension", "Glomerulonephritis"],
        "medicines": ["ACE inhibitors or ARBs (protect the kidneys)", "Medicines to manage diabetes and cholesterol", "Avoid regular NSAID use (e.g., ibuprofen)"],
        "prevention": ["Tight blood sugar & pressure control", "Avoid long-term overuse of NSAIDs (e.g., ibuprofen)"],
        "screening": "eGFR (Estimated Glomerular Filtration Rate) blood test and urine albumin test."
    },
    "Colorectal Cancer": {
        "category": "Oncology",
        "overview": "Cancer starting in the colon or rectum, usually developing from precancerous polyps.",
        "symptoms": ["Changes in bowel habits", "Blood in stool", "Unexplained weight loss", "Abdominal cramping"],
        "causes": ["Age", "Family history", "Diet high in processed meats", "Smoking & alcohol"],
        "medicines": ["Treatment (surgery, chemotherapy, and/or targeted therapy) is planned individually by a cancer specialist"],
        "prevention": ["High-fiber diet", "Limit red/processed meats", "Regular physical activity"],
        "screening": "Colonoscopy starting at age 45 (or earlier with family history)."
    },
    "Breast Cancer": {
        "category": "Oncology",
        "overview": "Cancer that forms in the tissue and cells of the breasts.",
        "symptoms": ["Painless breast lump", "Changes in breast shape/size", "Skin dimpling", "Nipple discharge"],
        "causes": ["BRCA1/BRCA2 gene mutations", "Hormonal factors", "Increasing age", "Alcohol consumption"],
        "medicines": ["Treatment (surgery, chemotherapy, hormone therapy, and/or targeted therapy) is planned individually by a cancer specialist"],
        "prevention": ["Maintain healthy weight", "Limit hormone replacement therapy", "Limit alcohol"],
        "screening": "Annual or biennial Screening Mammogram starting at age 40."
    }
}

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Healix Companion - Your Health Helper",
    page_icon="⚕️",
    layout="wide"
)

# --- STYLING (light, high-contrast, large-text theme for older users) ---
st.markdown("""
<style>
    html, body, [class*="css"]  { font-size: 19px !important; }
    .stApp { background-color: #F6F8F3; }
    section[data-testid="stSidebar"] { background-color: #EAF1EA; }
    h1, h2, h3 { color: #154F46 !important; }
    .stChatMessage { font-size: 19px; }
    .stButton button {
        font-size: 18px !important;
        padding: 0.6em 1.2em !important;
        border-radius: 12px !important;
        border: 2px solid #1F6F63 !important;
        min-height: 48px;
    }
    .category-badge {
        display: inline-block;
        background-color: #FBEED8;
        color: #C9861A;
        font-weight: bold;
        font-size: 0.9rem;
        padding: 4px 10px;
        border-radius: 4px;
        margin-bottom: 12px;
    }
    .section-header {
        color: #154F46;
        font-weight: bold;
        font-size: 1.15rem;
        margin-top: 18px;
        margin-bottom: 6px;
    }
    .bullet-item { color: #16211E; margin-left: 10px; font-size: 1.05rem; }
    .overview-text, .screening-text { color: #16211E; font-size: 1.1rem; }
    .disclaimer {
        color: #A5402F;
        background-color: #FBEAE6;
        font-size: 0.95rem;
        border-radius: 8px;
        margin-top: 20px;
        padding: 12px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown("## \u2695\ufe0f Healix Companion")
st.caption("A simple health chatbot -- ask about a condition, its symptoms, and the medicines commonly used for it.")

# --- TEXT SIZE CONTROL (sidebar, big buttons) ---
with st.sidebar:
    st.markdown("### Text size")
    size = st.radio("Text size", ["Normal", "Larger", "Largest"], label_visibility="collapsed", horizontal=False)
    size_map = {"Normal": "19px", "Larger": "22px", "Largest": "26px"}
    st.markdown(f"<style>html, body, [class*='css'] {{ font-size: {size_map[size]} !important; }}</style>", unsafe_allow_html=True)

    st.markdown("### Browse by category")
    categories = sorted(set(d["category"] for d in DISEASES_DB.values()))
    for cat in categories:
        if st.button(cat, use_container_width=True, key=f"cat_{cat}"):
            st.session_state["pending_disease"] = None
            st.session_state["pending_category"] = cat

# --- CHAT STATE ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "text": "Hello! \U0001F44B I'm Healix Companion. Ask me about a health condition "
                                       "(like 'diabetes' or 'asthma') or a symptom (like 'cough' or 'fatigue'), "
                                       "or use the category buttons in the sidebar."}
    ]
if "pending_category" not in st.session_state:
    st.session_state["pending_category"] = None


def render_disease_card(name):
    d = DISEASES_DB[name]
    lines = [f"### {name}", f"<span class='category-badge'>{d['category'].upper()}</span>", ""]
    html = f"<span class='category-badge'>{d['category'].upper()}</span>"
    html += "<div class='section-header'>OVERVIEW</div>"
    html += f"<div class='overview-text'>{d['overview']}</div>"
    html += "<div class='section-header'>COMMON SYMPTOMS</div>"
    for item in d["symptoms"]:
        html += f"<div class='bullet-item'>&bull; {item}</div>"
    html += "<div class='section-header'>MEDICINES COMMONLY USED</div>"
    for item in d["medicines"]:
        html += f"<div class='bullet-item'>&bull; {item}</div>"
    html += "<div class='section-header'>PREVENTION STRATEGIES</div>"
    for item in d["prevention"]:
        html += f"<div class='bullet-item'>&bull; {item}</div>"
    html += "<div class='section-header'>RECOMMENDED SCREENING</div>"
    html += f"<div class='screening-text'>{d['screening']}</div>"
    html += ("<div class='disclaimer'>\u26A0\uFE0F This is general information only, not a prescription. "
             "Please check with your doctor or pharmacist before starting, stopping, or changing any medicine.</div>")
    return f"### {name}\n" + html


def find_matches(query):
    q = query.lower().strip()
    if not q:
        return []
    results = []
    for name, d in DISEASES_DB.items():
        in_symptoms = any(q in s.lower() for s in d["symptoms"])
        if q in name.lower() or q in d["category"].lower() or in_symptoms:
            results.append(name)
    return results


# --- Handle a category button click from the sidebar ---
if st.session_state["pending_category"]:
    cat = st.session_state["pending_category"]
    names = [n for n, d in DISEASES_DB.items() if d["category"] == cat]
    reply = f"Here are the conditions I know about in **{cat}**:"
    st.session_state["messages"].append({"role": "assistant", "text": reply, "options": names})
    st.session_state["pending_category"] = None

# --- Render chat history ---
for i, msg in enumerate(st.session_state["messages"]):
    with st.chat_message("assistant" if msg["role"] == "assistant" else "user"):
        st.markdown(msg["text"], unsafe_allow_html=True)
        if msg.get("options"):
            cols = st.columns(min(3, len(msg["options"])) or 1)
            for j, opt in enumerate(msg["options"]):
                if cols[j % len(cols)].button(opt, key=f"opt_{i}_{j}"):
                    st.session_state["messages"].append({"role": "user", "text": opt})
                    if opt in DISEASES_DB:
                        st.session_state["messages"].append({"role": "assistant", "text": render_disease_card(opt)})
                    st.rerun()

# --- Chat input ---
user_input = st.chat_input("Type a condition or symptom, like 'diabetes' or 'cough'...")
if user_input:
    st.session_state["messages"].append({"role": "user", "text": user_input})
    matches = find_matches(user_input)
    if len(matches) == 0:
        st.session_state["messages"].append({
            "role": "assistant",
            "text": f"I couldn't find a match for \"{user_input}\". Try a simpler word, like a symptom "
                    f"(e.g. 'cough') or a condition name (e.g. 'diabetes')."
        })
    elif len(matches) == 1:
        st.session_state["messages"].append({"role": "assistant", "text": render_disease_card(matches[0])})
    else:
        st.session_state["messages"].append({
            "role": "assistant",
            "text": f"I found a few matches for \"{user_input}\". Which one did you mean?",
            "options": matches
        })
    st.rerun()
