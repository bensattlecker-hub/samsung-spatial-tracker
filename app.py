import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Samsung Spatial Content Hub", 
    layout="wide", 
    page_icon="🖥️",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------
# Data Persistence Engine
# ----------------------------------------------------
DB_FILE = "spatial_pipeline_db.csv"

if os.path.exists(DB_FILE):
    try:
        st.session_state.pipeline_data = pd.read_csv(DB_FILE)
    except Exception:
        st.session_state.pipeline_data = pd.DataFrame(columns=["Project ID", "Project Name", "Target Display", "Prompt Concept", "Status", "Date Created"])
else:
    if "pipeline_data" not in st.session_state:
        st.session_state.pipeline_data = pd.DataFrame(columns=["Project ID", "Project Name", "Target Display", "Prompt Concept", "Status", "Date Created"])

# Global Inject: Framer-style Styling
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    .stApp { background-color: #090909 !important; color: #ffffff !important; font-family: 'Inter', sans-serif !important; }
    .display-header { font-size: 52px !important; font-weight: 500 !important; line-height: 0.95; letter-spacing: -3.1px !important; color: #ffffff; margin-top: 10px; margin-bottom: 2px; }
    .display-caption { color: #999999 !important; font-size: 15px !important; letter-spacing: -0.15px !important; margin-bottom: 25px; }
    div[data-testid="stVerticalBlockBorderWrapper"] { background-color: rgba(20, 20, 20, 0.45) !important; backdrop-filter: blur(12px) !important; border: 1px solid rgba(38, 38, 38, 0.6) !important; border-radius: 16px !important; padding: 14px !important; margin-bottom: 10px !important; }
    .bento-title { font-size: 18px !important; font-weight: 700 !important; letter-spacing: -0.8px !important; color: #ffffff !important; margin-bottom: 12px !important; }
    input, textarea, select, .stSelectbox div { background-color: rgba(28, 28, 28, 0.7) !important; color: #ffffff !important; border: 1px solid #262626 !important; border-radius: 10px !important; }
    button[kind="primaryFormSubmit"], button[kind="secondary"], .stButton button { background-color: #ffffff !important; color: #000000 !important; border-radius: 100px !important; font-weight: 500 !important; border: none !important; padding: 8px 20px !important; }
    code, pre, pre span, div[data-testid="stCodeBlock"] pre { color: #0099ff !important; -webkit-text-fill-color: #0099ff !important; background-color: #1c1c1c !important; }
    .bento-spotlight { padding: 20px; border-radius: 15px; color: #ffffff; min-height: 105px; }
    .violet-spot { background: linear-gradient(135deg, #6a4cf5, #3c26b3); }
    .magenta-spot { background: linear-gradient(135deg, #d44df0, #881da1); }
    .orange-spot { background: linear-gradient(135deg, #ff7a3d, #cc440a); }
    .spotlight-num { font-size: 38px; font-weight: 700; letter-spacing: -1.5px; line-height: 1; }
    .spotlight-lbl { font-size: 13px; color: rgba(255,255,255,0.85); letter-spacing: -0.13px; margin-top: 4px; }
    </style>
""", unsafe_allow_html=True)

# Header Title Block Setup
st.markdown('<div class="display-header">Samsung Spatial Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="display-caption">Enterprise production pipeline and localised anamorphic canvas tracker.</div>', unsafe_allow_html=True)

# Pre-calculate counts safely
total_demos = len(st.session_state.pipeline_data)
ready_demos = len(st.session_state.pipeline_data[st.session_state.pipeline_data["Status"] == "5. Live Demo Ready"])
active_production = total_demos - ready_demos

# Metrics Row
m1, m2, m3 = st.columns(3)
m1.markdown(f'<div class="bento-spotlight violet-spot"><div class="spotlight-num">{total_demos}</div><div class="spotlight-lbl">Active Artboards</div></div>', unsafe_allow_html=True)
m2.markdown(f'<div class="bento-spotlight magenta-spot"><div class="spotlight-num">{active_production}</div><div class="spotlight-lbl">In AI Production Pipeline</div></div>', unsafe_allow_html=True)
m3.markdown(f'<div class="bento-spotlight orange-spot"><div class="spotlight-num">{ready_demos}</div><div class="spotlight-lbl">Verified Showroom Ready</div></div>', unsafe_allow_html=True)

st.write("")

# ----------------------------------------------------
# MODULE 1: Configuration Form
# ----------------------------------------------------
with st.container(border=True):
    st.markdown('<div class="bento-title">⚙️ Configure Asset</div>', unsafe_allow_html=True)
    with st.form("pipeline_form", clear_on_submit=True):
        p_name = st.text_input("Project Name")
        d_type = st.selectbox("Target Hardware", ["The Wall (MicroLED)", "The Link (Modular LED)", "90° Anamorphic Corner Cube"])
        r_concept = st.text_area("Core Asset Concept")
        stage = st.selectbox("Workflow State", ["1. Prompt Engineering", "2. Imagen 3 Render", "3. Veo 3.1 Animation", "4. Topaz Upscaling", "5. Live Demo Ready"])
        submit = st.form_submit_button("Deploy to Artboard")
    if submit and p_name:
        p_id = f"SAM-{datetime.now().strftime('%M%S')}"
        new_row = pd.DataFrame([{"Project ID": p_id, "Project Name": p_name, "Target Display": d_type, "Prompt Concept": r_concept, "Status": stage, "Date Created": datetime.now().strftime("%d/%m/%Y")}])
        st.session_state.pipeline_data = pd.concat([st.session_state.pipeline_data, new_row], ignore_index=True)
        st.session_state.pipeline_data.to_csv(DB_FILE, index=False)
        st.rerun()

# ----------------------------------------------------
# MODULE 2: Production Data Grid
# ----------------------------------------------------
with st.container(border=True):
    st.markdown('<div class="bento-title">📊 Studio Production Data</div>', unsafe_allow_html=True)
    if len(st.session_state.pipeline_data) == 0:
        st.info("Your pipeline database is completely blank. Use the configuration box above to deploy your first asset.")
    else:
        edited_df = st.data_editor(st.session_state.pipeline_data, use_container_width=True, num_rows="dynamic")
        if not edited_df.equals(st.session_state.pipeline_data):
            st.session_state.pipeline_data = edited_df
            st.session_state.pipeline_data.to_csv(DB_FILE, index=False)
            st.rerun()

# ----------------------------------------------------
# MODULE 3: Media Loop Verification Drop-zone
# ----------------------------------------------------
with st.container(border=True):
    st.markdown('<div class="bento-title">🎞️ Media Preview Centre</div>', unsafe_allow_html=True)
    uploaded_video = st.file_uploader("Drop showroom MP4 video loops here", type=["mp4", "mov"])
    if uploaded_video is not None:
        st.video(uploaded_video)

# ----------------------------------------------------
# MODULE 4: Anamorphic Prompt Engine
# ----------------------------------------------------
with st.container(border=True):
    st.markdown('<div class="bento-title">✨ Anamorphic Prompt Engine</div>', unsafe_allow_html=True)
    user_input = st.text_input("Enter target product core:", placeholder="e.g., Luxury watch, premium sedan...", key="bento_prompt_input")
    
    st.write("**Option A: 3D Pop-Out Effect (Forced Depth)**")
    prompt_a = f"Anamorphic forced perspective 3D render of a specialised {user_input if user_input else 'asset'}. Hyper-detailed textures, volumetric dramatic backlighting, dark infinity void backdrop. The object slowly rotates and drifts forward breaking the illusionary foreground screen boundary, extreme detail, depth map optimisation, shot on 35mm."
    st.code(prompt_a, language="text")
    
    st.write("**Option B: Ultra-Luxe Ambient Space**")
    prompt_b = f"Minimalist architectural space, central floating holographic {user_input if user_input else 'asset'} suspended in mid-air. Soft light refractions bouncing off glass surfaces, atmospheric dust motes catching golden light rays, hyper-photorealistic 8k, slow continuous camera push-in."
    st.code(prompt_b, language="text")

# ----------------------------------------------------
# MODULE 5: Executive Client Briefing Exporter
# ----------------------------------------------------
with st.container(border=True):
    st.markdown('<div class="bento-title">📋 Enterprise Brief Generator</div>', unsafe_allow_html=True)
    if len(st.session_state.pipeline_data) > 0:
        selected_project = st.selectbox("Select active artboard:", st.session_state.pipeline_data["Project Name"].unique())
        if st.button("Generate Sync Summary"):
            proj_row = st.session_state.pipeline_data[st.session_state.pipeline_data["Project Name"] == selected_project].iloc[0]
            summary_text = f"SAMSUNG SPATIAL DIGITAL BRIEF\\n---------------------------\\nID: {proj_row['Project ID']}\\nCampaign: {proj_row['Project Name']}\\nTarget: {proj_row['Target Display']}\\nStatus: {proj_row['Status']}\\nDate Logged: {proj_row['Date Created']}\\n\\nCONCEPT:\\n\\\"{proj_row['Prompt Concept']}\\\"\\n---------------------------"
            st.code(summary_text, language="text")
    else:
        st.info("Log a project inside the data matrix above to activate the client brief packager system.")
