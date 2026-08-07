import streamlit as st
import random
from collections import Counter

# =========================================================
# MEDICAL DATABASE (42 diseases)
# =========================================================
DISEASES_DB = {
    "Hypertension": {
        "category": "Cardiovascular", "icon": "❤️",
        "overview": "A chronic condition where blood force against artery walls is consistently too high.",
        "symptoms": ["Headaches", "Shortness of breath", "Nosebleeds", "Often asymptomatic ('Silent Killer')"],
        "causes": ["High salt intake", "Obesity", "Lack of exercise", "Genetics", "Stress"],
        "prevention": ["Reduce sodium intake (<2,300mg/day)", "Exercise 150 mins/week", "Maintain healthy BMI", "Limit alcohol"],
        "screening": "Blood pressure check every 1–2 years starting at age 18.",
        "severity": "Moderate",
    },
    "Coronary Artery Disease": {
        "category": "Cardiovascular", "icon": "❤️",
        "overview": "Plaque buildup in the coronary arteries that reduces blood flow to the heart.",
        "symptoms": ["Chest pain (angina)", "Shortness of breath", "Fatigue", "Heart attack"],
        "causes": ["High cholesterol", "Smoking", "Diabetes", "Sedentary lifestyle"],
        "prevention": ["Adopt a Mediterranean diet", "Quit smoking", "Manage cholesterol (LDL < 100 mg/dL)", "Regular cardio"],
        "screening": "Lipid panel every 4–6 years for adults; ECG or stress testing if symptomatic.",
        "severity": "High",
    },
    "Heart Failure": {
        "category": "Cardiovascular", "icon": "❤️",
        "overview": "A condition where the heart muscle doesn't pump blood as efficiently as it should.",
        "symptoms": ["Shortness of breath during exertion/lying down", "Swelling in legs/ankles", "Rapid heartbeat"],
        "causes": ["Uncontrolled hypertension", "Past heart attack", "Cardiomyopathy", "Valve disorders"],
        "prevention": ["Strict control of blood pressure & diabetes", "Avoid excess alcohol", "Low-sodium diet"],
        "screening": "Echocardiogram and BNP blood test evaluated by a cardiologist.",
        "severity": "High",
    },
    "Ischemic Stroke": {
        "category": "Neurological", "icon": "🧠",
        "overview": "Occurs when blood supply to part of the brain is interrupted or drastically reduced.",
        "symptoms": ["Facial drooping", "Arm weakness", "Slurred speech", "Sudden confusion"],
        "causes": ["Blood clots", "Atherosclerosis", "Atrial fibrillation", "Hypertension"],
        "prevention": ["Control blood pressure", "Manage blood sugar", "Treat arrhythmia/AFib", "Avoid smoking"],
        "screening": "Carotid ultrasound, brain CT/MRI, and routine vascular checkups.",
        "severity": "High",
    },
    "Atrial Fibrillation": {
        "category": "Cardiovascular", "icon": "❤️",
        "overview": "An irregular, often rapid heart rhythm originating in the upper chambers of the heart.",
        "symptoms": ["Heart palpitations", "Fatigue", "Dizziness", "Shortness of breath"],
        "causes": ["Aging", "High blood pressure", "Heart valve disease", "Excess alcohol/caffeine"],
        "prevention": ["Manage blood pressure", "Limit stimulants", "Treat sleep apnea", "Routine cardiac checkups"],
        "screening": "ECG (EKG) or wearable heart-rhythm monitor.",
        "severity": "Moderate",
    },
    "Type 2 Diabetes": {
        "category": "Metabolic", "icon": "🩸",
        "overview": "A metabolic disorder characterized by high blood sugar due to insulin resistance.",
        "symptoms": ["Increased thirst", "Frequent urination", "Unexplained weight loss", "Blurred vision"],
        "causes": ["Insulin resistance", "Obesity", "Inactivity", "Genetic predisposition"],
        "prevention": ["Low-glycemic index diet", "30 minutes daily activity", "Weight loss (5-7% of body weight)"],
        "screening": "Fasting blood glucose or HbA1c test annually starting at age 35.",
        "severity": "Moderate",
    },
    "Type 1 Diabetes": {
        "category": "Metabolic", "icon": "🩸",
        "overview": "An autoimmune condition where the pancreas produces little or no insulin.",
        "symptoms": ["Rapid weight loss", "Extreme thirst", "Fatigue", "Fruity-smelling breath"],
        "causes": ["Autoimmune destruction of pancreatic beta cells", "Genetic susceptibility", "Viral triggers"],
        "prevention": ["No known prevention", "Early diagnosis limits complications", "Blood sugar monitoring"],
        "screening": "Fasting glucose, HbA1c, and autoantibody blood tests.",
        "severity": "High",
    },
    "Metabolic Syndrome": {
        "category": "Metabolic", "icon": "🩸",
        "overview": "A cluster of conditions — high blood pressure, high blood sugar, excess abdominal fat, abnormal cholesterol — that raise heart disease risk.",
        "symptoms": ["Large waistline", "Often asymptomatic", "Fatigue", "High blood pressure readings"],
        "causes": ["Insulin resistance", "Obesity", "Sedentary lifestyle", "Genetics"],
        "prevention": ["Weight management", "Regular aerobic exercise", "Reduce refined carbs and sugar"],
        "screening": "Waist circumference, blood pressure, lipid panel, and fasting glucose.",
        "severity": "Moderate",
    },
    "Hypothyroidism": {
        "category": "Endocrine", "icon": "🦋",
        "overview": "Underactive thyroid gland failing to produce sufficient thyroid hormone.",
        "symptoms": ["Fatigue", "Weight gain", "Cold intolerance", "Dry skin", "Depression"],
        "causes": ["Hashimoto's thyroiditis (autoimmune)", "Thyroid surgery", "Radiation therapy"],
        "prevention": ["Ensure adequate iodine intake", "Early diagnosis via routine blood tests"],
        "screening": "Serum TSH (Thyroid-Stimulating Hormone) blood test.",
        "severity": "Low",
    },
    "Hyperthyroidism": {
        "category": "Endocrine", "icon": "🦋",
        "overview": "Overactive thyroid gland producing excess thyroid hormone, speeding up metabolism.",
        "symptoms": ["Unexplained weight loss", "Rapid heartbeat", "Sweating", "Anxiety/irritability"],
        "causes": ["Graves' disease (autoimmune)", "Thyroid nodules", "Excess iodine intake"],
        "prevention": ["No direct prevention", "Regular thyroid function monitoring if at risk"],
        "screening": "Serum TSH, free T4, and T3 blood tests.",
        "severity": "Moderate",
    },
    "Fatty Liver Disease (NAFLD)": {
        "category": "Metabolic", "icon": "🩸",
        "overview": "Excess fat buildup in liver cells not caused by heavy alcohol consumption.",
        "symptoms": ["Fatigue", "Pain in upper right abdomen", "Often asymptomatic"],
        "causes": ["Obesity", "Insulin resistance", "High intake of refined sugars/fructose"],
        "prevention": ["Avoid sugary beverages", "Regular resistance & aerobic training", "Weight management"],
        "screening": "Liver enzyme blood tests (ALT/AST) and abdominal ultrasound.",
        "severity": "Moderate",
    },
    "Asthma": {
        "category": "Respiratory", "icon": "🫁",
        "overview": "Chronic condition where airways narrow, swell, and produce extra mucus.",
        "symptoms": ["Wheezing", "Coughing (especially at night)", "Chest tightness", "Shortness of breath"],
        "causes": ["Genetic triggers", "Allergens (pollen, dust mites)", "Respiratory infections", "Cold air"],
        "prevention": ["Identify/avoid environmental triggers", "Annual flu vaccine", "Use prescribed preventive inhalers"],
        "screening": "Spirometry / Pulmonary Function Testing (PFT).",
        "severity": "Moderate",
    },
    "COPD": {
        "category": "Respiratory", "icon": "🫁",
        "overview": "Progressive inflammatory lung disease causing obstructed airflow from the lungs.",
        "symptoms": ["Chronic cough with mucus", "Shortness of breath", "Frequent respiratory infections"],
        "causes": ["Long-term cigarette smoking", "Air pollution exposure", "Chemical fumes"],
        "prevention": ["Zero tobacco smoking", "Use respirator masks in toxic environments", "Pneumococcal vaccination"],
        "screening": "Spirometry and chest X-rays.",
        "severity": "High",
    },
    "Pneumonia": {
        "category": "Respiratory", "icon": "🫁",
        "overview": "Infection that inflames air sacs in one or both lungs, which may fill with fluid or pus.",
        "symptoms": ["High fever/chills", "Cough with phlegm", "Chest pain when breathing", "Shortness of breath"],
        "causes": ["Bacteria (Streptococcus pneumoniae)", "Viruses (Flu, COVID-19)", "Fungi"],
        "prevention": ["Pneumococcal and Influenza vaccines", "Good hand hygiene", "Avoid smoking"],
        "screening": "Chest X-ray, sputum culture, and pulse oximetry.",
        "severity": "High",
    },
    "Sleep Apnea": {
        "category": "Respiratory", "icon": "🫁",
        "overview": "A disorder where breathing repeatedly stops and starts during sleep.",
        "symptoms": ["Loud snoring", "Gasping during sleep", "Daytime fatigue", "Morning headaches"],
        "causes": ["Obesity", "Airway anatomy", "Alcohol/sedative use", "Aging"],
        "prevention": ["Weight management", "Sleep on your side", "Avoid alcohol before bed"],
        "screening": "Overnight polysomnography (sleep study).",
        "severity": "Moderate",
    },
    "Tuberculosis (TB)": {
        "category": "Infectious", "icon": "🦠",
        "overview": "Potentially serious infectious bacterial disease mainly affecting the lungs.",
        "symptoms": ["Cough lasting 3+ weeks", "Coughing up blood", "Night sweats", "Unintentional weight loss"],
        "causes": ["Mycobacterium tuberculosis spread via airborne droplets"],
        "prevention": ["BCG vaccine in endemic areas", "Proper ventilation", "Treating latent TB infections"],
        "screening": "Mantoux Tuberculin Skin Test (TST) or IGRA Blood Test.",
        "severity": "High",
    },
    "Malaria": {
        "category": "Infectious", "icon": "🦠",
        "overview": "Mosquito-borne disease caused by a microscopic parasite.",
        "symptoms": ["High fever", "Shaking chills", "Headache", "Nausea/vomiting", "Muscle pain"],
        "causes": ["Plasmodium parasite transmitted via Anopheles mosquito bite"],
        "prevention": ["Insecticide-treated bed nets", "Prophylactic antimalarial medication", "Insect repellent (DEET)"],
        "screening": "Rapid Diagnostic Test (RDT) or thick/thin blood smear microscopic exam.",
        "severity": "High",
    },
    "Dengue Fever": {
        "category": "Infectious", "icon": "🦠",
        "overview": "A mosquito-borne viral infection common in tropical and subtropical climates.",
        "symptoms": ["High fever", "Severe headache", "Pain behind the eyes", "Rash", "Joint/muscle pain"],
        "causes": ["Dengue virus transmitted by Aedes mosquitoes"],
        "prevention": ["Eliminate standing water", "Use mosquito repellent", "Wear protective clothing"],
        "screening": "NS1 antigen test or dengue IgM/IgG antibody blood test.",
        "severity": "Moderate",
    },
    "Influenza": {
        "category": "Infectious", "icon": "🦠",
        "overview": "A contagious respiratory illness caused by influenza viruses.",
        "symptoms": ["Fever", "Chills", "Muscle aches", "Cough", "Fatigue"],
        "causes": ["Influenza A or B virus, spread via respiratory droplets"],
        "prevention": ["Annual flu vaccination", "Frequent handwashing", "Avoid close contact when sick"],
        "screening": "Rapid influenza diagnostic test (RIDT) or PCR swab.",
        "severity": "Low",
    },
    "COVID-19": {
        "category": "Infectious", "icon": "🦠",
        "overview": "A respiratory illness caused by the SARS-CoV-2 virus, ranging from mild to severe.",
        "symptoms": ["Fever", "Cough", "Loss of taste/smell", "Fatigue", "Shortness of breath"],
        "causes": ["SARS-CoV-2 virus spread via respiratory droplets/aerosols"],
        "prevention": ["Vaccination and boosters", "Ventilation", "Hand hygiene", "Masking in high-risk settings"],
        "screening": "PCR or rapid antigen test.",
        "severity": "Moderate",
    },
    "HIV/AIDS": {
        "category": "Infectious", "icon": "🦠",
        "overview": "A viral infection that attacks the immune system; untreated it progresses to AIDS.",
        "symptoms": ["Flu-like illness early on", "Recurrent infections", "Swollen lymph nodes", "Weight loss"],
        "causes": ["HIV virus transmitted via blood, sexual contact, or mother-to-child"],
        "prevention": ["PrEP medication", "Condom use", "Sterile needles", "Regular testing"],
        "screening": "HIV antibody/antigen blood test.",
        "severity": "High",
    },
    "Typhoid Fever": {
        "category": "Infectious", "icon": "🦠",
        "overview": "A bacterial infection spread through contaminated food or water.",
        "symptoms": ["Sustained high fever", "Weakness", "Abdominal pain", "Headache", "Loss of appetite"],
        "causes": ["Salmonella Typhi bacteria via contaminated food/water"],
        "prevention": ["Typhoid vaccination", "Safe drinking water", "Good food hygiene"],
        "screening": "Blood culture (Widal test or PCR).",
        "severity": "Moderate",
    },
    "Hepatitis B": {
        "category": "Infectious", "icon": "🦠",
        "overview": "Serious liver infection caused by the Hepatitis B virus (HBV).",
        "symptoms": ["Jaundice (yellow eyes/skin)", "Dark urine", "Abdominal pain", "Fatigue"],
        "causes": ["Exposure to infected blood or bodily fluids", "Unsafe injections", "Mother to child"],
        "prevention": ["Hepatitis B vaccination (3-dose series)", "Safe medical practices", "Avoid sharing personal items"],
        "screening": "HBsAg (Hepatitis B surface antigen) blood panel.",
        "severity": "Moderate",
    },
    "Lyme Disease": {
        "category": "Infectious", "icon": "🦠",
        "overview": "Bacterial illness transmitted by infected blacklegged ticks.",
        "symptoms": ["'Bullseye' rash (Erythema migrans)", "Fever", "Joint pain", "Neurological issues if untreated"],
        "causes": ["Borrelia burgdorferi bacterium via tick bite"],
        "prevention": ["Wear long sleeves/pants in wooded areas", "Use DEET/Permethrin", "Check body for ticks promptly"],
        "screening": "Two-tiered antibody blood testing (ELISA followed by Western Blot).",
        "severity": "Low",
    },
    "Alzheimer's Disease": {
        "category": "Neurological", "icon": "🧠",
        "overview": "Progressive neurodegenerative disease causing brain cells to waste away and die.",
        "symptoms": ["Memory loss affecting daily life", "Disorientation", "Language difficulties", "Behavioral changes"],
        "causes": ["Amyloid plaque & tau tangle accumulation", "Genetics (APOE-e4)", "Age"],
        "prevention": ["Regular cognitive exercises", "Social engagement", "Cardiovascular health maintenance"],
        "screening": "Cognitive assessment tests (MMSE), brain MRI/PET scans.",
        "severity": "High",
    },
    "Parkinson's Disease": {
        "category": "Neurological", "icon": "🧠",
        "overview": "Central nervous system disorder affecting movement and dopamine-producing neurons.",
        "symptoms": ["Resting tremor", "Bradykinesia (slowed movement)", "Muscle rigidity", "Postural instability"],
        "causes": ["Loss of dopamine neurons in substantia nigra", "Genetic mutation", "Environmental toxins"],
        "prevention": ["Regular high-intensity aerobic exercise", "Diet rich in antioxidants"],
        "screening": "Clinical evaluation by a neurologist; DaTscan imaging.",
        "severity": "High",
    },
    "Migraine": {
        "category": "Neurological", "icon": "🧠",
        "overview": "A neurological condition causing intense, recurring headaches often with additional symptoms.",
        "symptoms": ["Throbbing head pain", "Nausea", "Sensitivity to light/sound", "Visual aura"],
        "causes": ["Genetic predisposition", "Hormonal changes", "Stress", "Certain foods or triggers"],
        "prevention": ["Identify and avoid triggers", "Regular sleep schedule", "Stress management", "Stay hydrated"],
        "screening": "Clinical diagnosis based on headache history; MRI to rule out other causes.",
        "severity": "Low",
    },
    "Epilepsy": {
        "category": "Neurological", "icon": "🧠",
        "overview": "A neurological disorder marked by recurrent, unprovoked seizures.",
        "symptoms": ["Seizures (convulsive or non-convulsive)", "Temporary confusion", "Staring spells", "Loss of consciousness"],
        "causes": ["Brain injury", "Genetics", "Stroke", "Infections affecting the brain"],
        "prevention": ["Prevent head injuries", "Manage fevers in children promptly", "Medication adherence if diagnosed"],
        "screening": "EEG (Electroencephalogram) and brain imaging.",
        "severity": "Moderate",
    },
    "Multiple Sclerosis": {
        "category": "Neurological", "icon": "🧠",
        "overview": "An autoimmune disease where the immune system attacks the protective covering of nerves.",
        "symptoms": ["Numbness or weakness in limbs", "Vision problems", "Fatigue", "Balance issues"],
        "causes": ["Autoimmune nerve damage", "Genetic susceptibility", "Environmental factors (e.g. low vitamin D)"],
        "prevention": ["No known prevention", "Vitamin D sufficiency may lower risk", "Avoid smoking"],
        "screening": "MRI of brain/spine and lumbar puncture (spinal fluid analysis).",
        "severity": "High",
    },
    "Major Depressive Disorder": {
        "category": "Mental Health", "icon": "🧩",
        "overview": "A mood disorder causing persistent feelings of sadness and loss of interest.",
        "symptoms": ["Persistent low mood", "Anhedonia", "Changes in sleep/appetite", "Fatigue", "Low concentration"],
        "causes": ["Neurochemical imbalances", "Genetic vulnerability", "Chronic stress or trauma"],
        "prevention": ["Building strong social support systems", "Regular physical activity", "Stress management"],
        "screening": "PHQ-9 (Patient Health Questionnaire) screening tool.",
        "severity": "Moderate",
    },
    "Generalized Anxiety Disorder": {
        "category": "Mental Health", "icon": "🧩",
        "overview": "A mental health condition marked by excessive, persistent worry about everyday matters.",
        "symptoms": ["Excessive worry", "Restlessness", "Muscle tension", "Difficulty concentrating", "Sleep problems"],
        "causes": ["Genetics", "Brain chemistry", "Chronic stress", "Trauma"],
        "prevention": ["Stress-reduction techniques", "Limit caffeine", "Regular exercise", "Adequate sleep"],
        "screening": "GAD-7 questionnaire and clinical psychological evaluation.",
        "severity": "Moderate",
    },
    "Bipolar Disorder": {
        "category": "Mental Health", "icon": "🧩",
        "overview": "A mental health condition causing extreme mood swings between mania/hypomania and depression.",
        "symptoms": ["Episodes of elevated mood/energy", "Depressive episodes", "Impulsivity", "Sleep disturbances"],
        "causes": ["Genetic factors", "Brain structure/chemistry differences", "Stressful life events"],
        "prevention": ["No known prevention", "Early treatment reduces episode severity", "Consistent sleep routine"],
        "screening": "Clinical psychiatric evaluation; mood disorder questionnaires.",
        "severity": "High",
    },
    "Osteoporosis": {
        "category": "Musculoskeletal", "icon": "🦴",
        "overview": "Condition where bones become weak and brittle, increasing fracture risk.",
        "symptoms": ["Bone fractures from minor falls", "Loss of height over time", "Stooped posture"],
        "causes": ["Aging", "Estrogen decline in post-menopause", "Calcium & Vitamin D deficiency"],
        "prevention": ["Adequate daily Calcium (1000-1200mg) and Vitamin D", "Weight-bearing exercises"],
        "screening": "DEXA (Dual-energy X-ray absorptiometry) bone density scan.",
        "severity": "Moderate",
    },
    "Osteoarthritis": {
        "category": "Musculoskeletal", "icon": "🦴",
        "overview": "Degenerative joint disease caused by breakdown of joint cartilage.",
        "symptoms": ["Joint pain and stiffness", "Loss of flexibility", "Grating sensation during movement"],
        "causes": ["Joint wear and tear", "Prior joint injuries", "Obesity"],
        "prevention": ["Maintain a healthy weight", "Low-impact exercises (swimming/cycling)", "Protect joints from injury"],
        "screening": "Joint X-rays and clinical physical examination.",
        "severity": "Low",
    },
    "Rheumatoid Arthritis": {
        "category": "Musculoskeletal", "icon": "🦴",
        "overview": "An autoimmune disorder causing chronic inflammation of the joints.",
        "symptoms": ["Symmetrical joint pain/swelling", "Morning stiffness", "Fatigue", "Low-grade fever"],
        "causes": ["Autoimmune attack on joint lining", "Genetic factors", "Smoking"],
        "prevention": ["No known prevention", "Avoid smoking", "Early treatment slows joint damage"],
        "screening": "Rheumatoid factor (RF) and anti-CCP antibody blood tests.",
        "severity": "Moderate",
    },
    "Gout": {
        "category": "Musculoskeletal", "icon": "🦴",
        "overview": "A form of inflammatory arthritis caused by excess uric acid crystallizing in joints.",
        "symptoms": ["Sudden severe joint pain (often big toe)", "Redness and swelling", "Warmth in joint"],
        "causes": ["High uric acid levels", "Diet high in purines (red meat, alcohol)", "Obesity"],
        "prevention": ["Limit alcohol and red meat", "Stay hydrated", "Maintain healthy weight"],
        "screening": "Serum uric acid test and joint fluid analysis.",
        "severity": "Low",
    },
    "Chronic Kidney Disease": {
        "category": "Renal", "icon": "🫘",
        "overview": "Gradual loss of kidney function over time, leading to dangerous fluid/waste buildup.",
        "symptoms": ["Swollen ankles/feet", "Fatigue", "Changes in urination frequency", "Nausea"],
        "causes": ["Uncontrolled diabetes", "Long-term hypertension", "Glomerulonephritis"],
        "prevention": ["Tight blood sugar & pressure control", "Avoid long-term overuse of NSAIDs (e.g., ibuprofen)"],
        "screening": "eGFR (Estimated Glomerular Filtration Rate) blood test and urine albumin test.",
        "severity": "High",
    },
    "Kidney Stones": {
        "category": "Renal", "icon": "🫘",
        "overview": "Hard mineral deposits that form inside the kidneys and can cause severe pain when passing.",
        "symptoms": ["Severe flank/back pain", "Blood in urine", "Nausea/vomiting", "Painful urination"],
        "causes": ["Dehydration", "High-sodium/high-oxalate diet", "Obesity", "Family history"],
        "prevention": ["Drink plenty of water", "Limit sodium and animal protein", "Reduce oxalate-rich foods"],
        "screening": "CT scan or ultrasound of the kidneys.",
        "severity": "Moderate",
    },
    "GERD": {
        "category": "Gastrointestinal", "icon": "🍽️",
        "overview": "A digestive disorder where stomach acid frequently flows back into the esophagus.",
        "symptoms": ["Heartburn", "Regurgitation", "Chest discomfort", "Difficulty swallowing"],
        "causes": ["Weak lower esophageal sphincter", "Obesity", "Hiatal hernia", "Certain foods"],
        "prevention": ["Avoid large/late meals", "Limit caffeine, alcohol, spicy food", "Maintain healthy weight"],
        "screening": "Clinical diagnosis; endoscopy or pH monitoring if severe.",
        "severity": "Low",
    },
    "Irritable Bowel Syndrome (IBS)": {
        "category": "Gastrointestinal", "icon": "🍽️",
        "overview": "A common disorder affecting the large intestine, causing chronic digestive discomfort.",
        "symptoms": ["Abdominal pain/cramping", "Bloating", "Diarrhea or constipation", "Gas"],
        "causes": ["Gut-brain axis dysfunction", "Food sensitivities", "Stress", "Altered gut microbiota"],
        "prevention": ["Identify trigger foods", "Manage stress", "Regular meal patterns", "Fiber intake"],
        "screening": "Clinical diagnosis based on symptom criteria (Rome IV); rules out other conditions.",
        "severity": "Low",
    },
    "Celiac Disease": {
        "category": "Gastrointestinal", "icon": "🍽️",
        "overview": "An autoimmune disorder where gluten ingestion damages the small intestine lining.",
        "symptoms": ["Diarrhea/bloating after gluten", "Fatigue", "Weight loss", "Anemia"],
        "causes": ["Autoimmune reaction to gluten", "Genetic predisposition (HLA-DQ2/DQ8)"],
        "prevention": ["No known prevention", "Strict gluten-free diet once diagnosed manages symptoms"],
        "screening": "tTG-IgA antibody blood test, confirmed by intestinal biopsy.",
        "severity": "Moderate",
    },
    "Psoriasis": {
        "category": "Dermatological", "icon": "🩹",
        "overview": "A chronic autoimmune skin condition causing rapid buildup of skin cells.",
        "symptoms": ["Red, scaly patches", "Itching or burning", "Thickened nails", "Joint pain (in some cases)"],
        "causes": ["Immune system dysfunction", "Genetics", "Triggers like stress or infection"],
        "prevention": ["Manage stress", "Avoid known triggers", "Moisturize skin regularly"],
        "screening": "Clinical skin examination; skin biopsy if diagnosis unclear.",
        "severity": "Low",
    },
    "Eczema (Atopic Dermatitis)": {
        "category": "Dermatological", "icon": "🩹",
        "overview": "A chronic condition causing dry, itchy, and inflamed skin, often starting in childhood.",
        "symptoms": ["Itchy, dry skin", "Red to brownish-gray patches", "Small raised bumps that may leak fluid"],
        "causes": ["Genetic skin barrier defects", "Immune system overreaction", "Allergens/irritants"],
        "prevention": ["Regular moisturizing", "Avoid harsh soaps/irritants", "Identify and avoid allergens"],
        "screening": "Clinical skin examination; allergy testing if triggers unclear.",
        "severity": "Low",
    },
    "Colorectal Cancer": {
        "category": "Oncology", "icon": "🎗️",
        "overview": "Cancer starting in the colon or rectum, usually developing from precancerous polyps.",
        "symptoms": ["Changes in bowel habits", "Blood in stool", "Unexplained weight loss", "Abdominal cramping"],
        "causes": ["Age", "Family history", "Diet high in processed meats", "Smoking & alcohol"],
        "prevention": ["High-fiber diet", "Limit red/processed meats", "Regular physical activity"],
        "screening": "Colonoscopy starting at age 45 (or earlier with family history).",
        "severity": "High",
    },
    "Breast Cancer": {
        "category": "Oncology", "icon": "🎗️",
        "overview": "Cancer that forms in the tissue and cells of the breasts.",
        "symptoms": ["Painless breast lump", "Changes in breast shape/size", "Skin dimpling", "Nipple discharge"],
        "causes": ["BRCA1/BRCA2 gene mutations", "Hormonal factors", "Increasing age", "Alcohol consumption"],
        "prevention": ["Maintain healthy weight", "Limit hormone replacement therapy", "Limit alcohol"],
        "screening": "Annual or biennial Screening Mammogram starting at age 40.",
        "severity": "High",
    },
    "Lung Cancer": {
        "category": "Oncology", "icon": "🎗️",
        "overview": "Cancer that begins in the lungs, most commonly linked to tobacco smoke exposure.",
        "symptoms": ["Persistent cough", "Coughing up blood", "Chest pain", "Unexplained weight loss"],
        "causes": ["Cigarette smoking", "Secondhand smoke", "Radon exposure", "Air pollution"],
        "prevention": ["Avoid smoking and secondhand smoke", "Test home for radon", "Avoid occupational carcinogens"],
        "screening": "Low-dose CT scan for high-risk current/former smokers aged 50–80.",
        "severity": "High",
    },
    "Prostate Cancer": {
        "category": "Oncology", "icon": "🎗️",
        "overview": "Cancer that develops in the prostate gland, common in older men.",
        "symptoms": ["Difficulty urinating", "Weak urine stream", "Blood in urine/semen", "Often asymptomatic early"],
        "causes": ["Age", "Family history", "Genetic mutations", "Race/ethnicity risk factors"],
        "prevention": ["Diet rich in vegetables", "Maintain healthy weight", "Regular exercise"],
        "screening": "PSA (Prostate-Specific Antigen) blood test and digital rectal exam.",
        "severity": "Moderate",
    },
    "Melanoma": {
        "category": "Oncology", "icon": "🎗️",
        "overview": "The most serious type of skin cancer, developing in pigment-producing cells.",
        "symptoms": ["New or changing mole", "Asymmetric borders", "Multiple colors in one spot", "Diameter growth"],
        "causes": ["UV radiation exposure", "Sunburn history", "Fair skin", "Family history"],
        "prevention": ["Use SPF 30+ sunscreen daily", "Avoid tanning beds", "Wear protective clothing"],
        "screening": "Annual full-body skin examination by a dermatologist.",
        "severity": "High",
    },
}

CATEGORY_ICONS = {
    "Cardiovascular": "❤️", "Neurological": "🧠", "Metabolic": "🩸", "Endocrine": "🦋",
    "Respiratory": "🫁", "Infectious": "🦠", "Mental Health": "🧩", "Musculoskeletal": "🦴",
    "Renal": "🫘", "Gastrointestinal": "🍽️", "Dermatological": "🩹", "Oncology": "🎗️",
}
SEVERITY_COLOR = {"Low": "#a6e3a1", "Moderate": "#f9e2af", "High": "#f38ba8"}

# =========================================================
# PAGE CONFIG + STYLING
# =========================================================
st.set_page_config(page_title="Healix — Medical Explorer", page_icon="⚕️", layout="wide")

if "theme" not in st.session_state:
    st.session_state.theme = "Dark"
if "favorites" not in st.session_state:
    st.session_state.favorites = set()

def inject_css(theme: str):
    if theme == "Dark":
        bg, sidebar_bg, card_bg, text, subtext, accent, border = (
            "#1e1e2e", "#181825", "#232336", "#cdd6f4", "#a6adc8", "#89b4fa", "#313244"
        )
    else:
        bg, sidebar_bg, card_bg, text, subtext, accent, border = (
            "#f5f5fa", "#ffffff", "#ffffff", "#1e1e2e", "#4c4f69", "#1e66f5", "#dcdcf0"
        )
    st.markdown(f"""
    <style>
    .stApp {{ background-color: {bg}; }}
    section[data-testid="stSidebar"] {{ background-color: {sidebar_bg}; }}
    h1, h2, h3 {{ color: {accent}; }}
    div[data-testid="stMetric"] {{
        background-color: {card_bg}; border: 1px solid {border}; border-radius: 10px; padding: 10px;
    }}
    .healix-card {{
        background-color: {card_bg}; border: 1px solid {border}; border-radius: 14px;
        padding: 18px 22px; margin-bottom: 14px;
    }}
    .healix-title {{ font-size: 1.6rem; font-weight: 800; color: {text}; }}
    .category-badge {{
        display: inline-block; background-color: {sidebar_bg}; color: #a6e3a1; font-weight: bold;
        font-size: 0.78rem; padding: 4px 10px; border-radius: 999px; margin-right: 6px;
    }}
    .severity-badge {{
        display: inline-block; font-weight: bold; font-size: 0.78rem; padding: 4px 10px;
        border-radius: 999px; color: #1e1e2e;
    }}
    .bullet-item {{ color: {subtext}; margin-left: 4px; margin-bottom: 4px; }}
    .body-text {{ color: {text}; line-height: 1.5; }}
    .disclaimer {{
        color: {subtext}; font-size: 0.8rem; font-style: italic; border-top: 1px solid {border};
        margin-top: 25px; padding-top: 10px;
    }}
    .match-pill {{
        display:inline-block; background:{accent}; color:#1e1e2e; border-radius:999px;
        padding:2px 10px; font-size:0.75rem; font-weight:700; margin-left:8px;
    }}
    </style>
    """, unsafe_allow_html=True)

inject_css(st.session_state.theme)

# =========================================================
# HELPERS
# =========================================================
def all_categories():
    return sorted({d["category"] for d in DISEASES_DB.values()})

def all_symptoms():
    s = set()
    for d in DISEASES_DB.values():
        s.update(d["symptoms"])
    return sorted(s)

def search_diseases(query, categories):
    query = (query or "").lower().strip()
    results = []
    for name, d in DISEASES_DB.items():
        if categories and d["category"] not in categories:
            continue
        haystack = " ".join([name, d["category"], d["overview"], " ".join(d["symptoms"]),
                              " ".join(d["causes"])]).lower()
        if not query or query in haystack:
            results.append(name)
    return sorted(results)

def render_disease_card(name, data, show_favorite=True):
    st.markdown(f"<div class='healix-title'>{data['icon']} {name}</div>", unsafe_allow_html=True)
    sev = data.get("severity", "Moderate")
    st.markdown(
        f"<span class='category-badge'>{data['category'].upper()}</span>"
        f"<span class='severity-badge' style='background-color:{SEVERITY_COLOR.get(sev,'#f9e2af')}'>{sev.upper()} CONCERN</span>",
        unsafe_allow_html=True,
    )
    st.write("")
    if show_favorite:
        is_fav = name in st.session_state.favorites
        if st.button(("★ Remove Favorite" if is_fav else "☆ Add to Favorites"), key=f"fav_{name}"):
            if is_fav:
                st.session_state.favorites.discard(name)
            else:
                st.session_state.favorites.add(name)
            st.rerun()

    tabs = st.tabs(["📋 Overview", "🩺 Symptoms", "⚠️ Causes", "🛡️ Prevention", "🔬 Screening"])
    with tabs[0]:
        st.markdown(f"<div class='body-text'>{data['overview']}</div>", unsafe_allow_html=True)
    with tabs[1]:
        for item in data["symptoms"]:
            st.markdown(f"<div class='bullet-item'>• {item}</div>", unsafe_allow_html=True)
    with tabs[2]:
        for item in data["causes"]:
            st.markdown(f"<div class='bullet-item'>• {item}</div>", unsafe_allow_html=True)
    with tabs[3]:
        for item in data["prevention"]:
            st.markdown(f"<div class='bullet-item'>• {item}</div>", unsafe_allow_html=True)
    with tabs[4]:
        st.markdown(f"<div class='body-text'>{data['screening']}</div>", unsafe_allow_html=True)

    export_text = (
        f"{name} ({data['category']})\n\nOverview:\n{data['overview']}\n\n"
        f"Symptoms:\n" + "\n".join(f"- {s}" for s in data["symptoms"]) + "\n\n"
        f"Causes:\n" + "\n".join(f"- {c}" for c in data["causes"]) + "\n\n"
        f"Prevention:\n" + "\n".join(f"- {p}" for p in data["prevention"]) + "\n\n"
        f"Screening:\n{data['screening']}\n"
    )
    st.download_button("⬇ Download summary (.txt)", export_text, file_name=f"{name}.txt", key=f"dl_{name}")

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================
with st.sidebar:
    st.markdown("## ⚕️ Healix")
    st.caption("Educational medical explorer")
    mode = st.radio(
        "Mode",
        ["🔎 Browse", "🩺 Symptom Checker", "⚖️ Compare", "⭐ Favorites", "📊 Stats"],
        label_visibility="collapsed",
    )
    st.divider()
    st.session_state.theme = st.select_slider("Theme", options=["Dark", "Light"], value=st.session_state.theme)
    st.divider()
    if st.button("🎲 Surprise me (random disease)"):
        st.session_state["_random_pick"] = random.choice(list(DISEASES_DB.keys()))

# =========================================================
# MODE: BROWSE
# =========================================================
if mode == "🔎 Browse":
    st.markdown("## ⚕️ Healix Medical Explorer")
    st.caption("Search by disease name, category, symptom, or cause.")

    col_search, col_cat = st.columns([2, 1])
    with col_search:
        query = st.text_input("Search", placeholder="e.g. cough, diabetes, fatigue...", label_visibility="collapsed")
    with col_cat:
        categories = st.multiselect("Filter by category", all_categories(), label_visibility="collapsed",
                                     placeholder="Filter by category")

    filtered = search_diseases(query, categories)

    left, right = st.columns([1, 2])
    with left:
        st.markdown(f"**DISEASE INDEX ({len(filtered)})**")
        if not filtered:
            st.info("No matches found. Try a different search term.")
            selected = None
        else:
            default_pick = st.session_state.pop("_random_pick", None)
            idx = filtered.index(default_pick) if default_pick in filtered else 0
            selected = st.radio("Diseases", filtered, index=idx, label_visibility="collapsed",
                                 format_func=lambda n: f"{DISEASES_DB[n]['icon']} {n}")
    with right:
        if selected:
            with st.container(border=True):
                render_disease_card(selected, DISEASES_DB[selected])

# =========================================================
# MODE: SYMPTOM CHECKER
# =========================================================
elif mode == "🩺 Symptom Checker":
    st.markdown("## 🩺 Symptom Checker")
    st.caption("Select the symptoms you're experiencing — Healix will rank the closest matches. "
               "This is educational only and not a diagnosis.")

    picked = st.multiselect("Select symptoms", all_symptoms(), placeholder="Start typing a symptom...")

    if picked:
        scored = []
        for name, d in DISEASES_DB.items():
            overlap = len(set(picked) & set(d["symptoms"]))
            if overlap > 0:
                scored.append((name, d, overlap))
        scored.sort(key=lambda x: x[2], reverse=True)

        if not scored:
            st.info("No diseases in the database match those symptoms.")
        else:
            st.markdown(f"**{len(scored)} possible matches**, ranked by number of overlapping symptoms:")
            for name, d, overlap in scored[:10]:
                pct = int(100 * overlap / len(d["symptoms"]))
                with st.expander(f"{d['icon']} {name}  —  {overlap} symptom match"):
                    st.progress(min(pct, 100), text=f"{pct}% of this condition's known symptoms matched")
                    render_disease_card(name, d, show_favorite=True)
    else:
        st.info("Pick one or more symptoms above to see possible matches.")

    st.markdown(
        "<div class='disclaimer'>⚠️ This tool is for educational purposes only and cannot diagnose any condition. "
        "Symptom overlap does not imply likelihood or causation — always consult a licensed healthcare provider.</div>",
        unsafe_allow_html=True,
    )

# =========================================================
# MODE: COMPARE
# =========================================================
elif mode == "⚖️ Compare":
    st.markdown("## ⚖️ Compare Diseases")
    st.caption("Pick two conditions to see them side by side.")

    names = sorted(DISEASES_DB.keys())
    c1, c2 = st.columns(2)
    with c1:
        pick_a = st.selectbox("Condition A", names, index=0)
    with c2:
        pick_b = st.selectbox("Condition B", names, index=1 if len(names) > 1 else 0)

    col_a, col_b = st.columns(2)
    for col, pick in [(col_a, pick_a), (col_b, pick_b)]:
        with col:
            with st.container(border=True):
                d = DISEASES_DB[pick]
                render_disease_card(pick, d, show_favorite=True)

# =========================================================
# MODE: FAVORITES
# =========================================================
elif mode == "⭐ Favorites":
    st.markdown("## ⭐ Your Favorites")
    if not st.session_state.favorites:
        st.info("You haven't favorited any conditions yet. Star a disease from Browse, Compare, or the Symptom Checker to save it here.")
    else:
        for name in sorted(st.session_state.favorites):
            with st.container(border=True):
                render_disease_card(name, DISEASES_DB[name])

# =========================================================
# MODE: STATS
# =========================================================
elif mode == "📊 Stats":
    st.markdown("## 📊 Database Stats")

    total = len(DISEASES_DB)
    cat_counts = Counter(d["category"] for d in DISEASES_DB.values())
    sev_counts = Counter(d.get("severity", "Moderate") for d in DISEASES_DB.values())

    m1, m2, m3 = st.columns(3)
    m1.metric("Total conditions", total)
    m2.metric("Categories covered", len(cat_counts))
    m3.metric("High-severity conditions", sev_counts.get("High", 0))

    st.markdown("#### Conditions by category")
    st.bar_chart(dict(sorted(cat_counts.items(), key=lambda x: -x[1])))

    st.markdown("#### Conditions by severity")
    st.bar_chart(dict(sev_counts))

st.markdown(
    "<div class='disclaimer'>⚠️ Healix is for educational purposes only and is not a substitute for "
    "professional medical diagnosis. Please consult a licensed healthcare provider.</div>",
    unsafe_allow_html=True,
)
