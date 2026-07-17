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
# Automatic Background Sync Engine (Data Persistence)
# ----------------------------------------------------
DB_FILE = "spatial_pipeline_db.csv"

def load_persistent_data():
    """Loads recorded pipeline assets safely from disk."""
    if os.path.exists(DB_FILE):
        try:
            return pd.read_csv(DB_FILE)
        except Exception:
            pass
    # Return structure matching token expectations if file doesn't exist/fails
    return pd.DataFrame(columns=[
        "Project ID", "Project Name", "Target Display", "Prompt Concept", "Status", "Date Created"
    ])

def save_persistent_data(df):
    """Automatically synchronises changes back to disk in the background."""
    df.to_csv(DB_FILE, index=False)

# Load data into state once
if "pipeline_data" not in st.session_state:
    st.session_state.pipeline_data = load_persistent_data()


# ----------------------------------------------------
# Global Inject: Framer Bento Grid & Glassmorphism Core
# ----------------------------------------------------
st.markdown("""
    <style>
    @import url('https://googleapis.com');
    
    /* Global Base Artboard background canvas */
    .stApp {
        background-color: #090909 !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Aggressive Negative Tracking on Poster-style Display Headers */
    .display-header {
        font-size: 52px !important;
        font-weight: 500 !important;
        line-height: 0.95;
        letter-spacing: -3.1px !important;
        color: #ffffff;
        margin-top: 10px;
        margin-bottom: 2px;
    }
    .display-caption {
        color: #999999 !important;
        font-size: 15px !important;
        letter-spacing: -0.15px !important;
        margin-bottom: 25px;
    }
    
    /* Premium Glassmorphic Bento Box Layout Subsystem */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background-color: rgba(20, 20, 20, 0.45) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(38, 38, 38, 0.6) !important;
        border-radius: 16px !important;
        padding: 14px !important;
        margin-bottom: 10px !important;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4) !important;
    }
    
    /* Bento Box Subheadings */
    .bento-title {
        font-size: 18px !important;
        font-weight: 700 !important;
        letter-spacing: -0.8px !important;
        color: #ffffff !important;
        margin-bottom: 12px !important;
    }
    
    /* Form Inputs styling (Surface 2 UI) */
    input, textarea, select, .stSelectbox div {
        background-color: rgba(28, 28, 28, 0.7) !important;
        color: #ffffff !important;
        border: 1px solid #262626 !important;
        border-radius: 10px !important;
    }
    input:focus, textarea:focus {
        border-color: #0099ff !important;
        box-shadow: 0 0 0 2px rgba(0, 153, 255, 0.2) !important;
    }
    
    /* Pill Form Action Action Buttons (White Pill style) */
    button[kind="primaryFormSubmit"], button[kind="secondary"] {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 100px !important;
        font-weight: 500 !important;
        letter-spacing: -0.14px !important;
        border: none !important;
        padding: 8px 20px !important;
        width: auto !important;
    }
    
    /* Custom Atmosphere Gradient Spotlights for Bento Counters */
    .bento-spotlight {
        padding: 20px;
        border-radius: 15px;
        color: #ffffff;
        min-height: 105px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }
    .violet-spot { background: linear-gradient(135deg, #6a4cf5, #3c26b3); }
    .magenta-spot { background: linear-gradient(135deg, #d44df0, #881da1); }
    .orange-spot { background: linear-gradient(135deg, #ff7a3d, #cc440a); }
    
    .spotlight-num {
        font-size: 38px;
        font-weight: 700;
        letter-spacing: -1.5px;
        line-height: 1;
    }
    .spotlight-lbl {
        font-size: 13px;
        color: rgba(255,255,255,0.85);
        letter-spacing: -0.13px;
        margin-top: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Header Title Block Setup
st.markdown('<div class="display-header">Samsung Spatial Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="display-caption">Enterprise production pipeline and localised anamorphic canvas tracker.</div>', unsafe_allow_html=True)

# Pre-calculate counts dynamically from synchronous tracking state
total_demos = len(st.session_state.pipeline_data)
ready_demos = len(st.session_state.pipeline_data[st.session_state.pipeline_data["Status"] == "5. Live Demo Ready"])
active_production = total_demos - ready_demos


# ----------------------------------------------------
# Bento Grid Row 1: The Atmosphere Spotlight Tiles
# ----------------------------------------------------
metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.markdown(f'<div class="bento-spotlight violet-spot"><div class="spotlight-num">{total_demos}</div><div class="spotlight-lbl">Active Artboards</div></div>', unsafe_allow_html=True)

with metric_col2:
    st.markdown(f'<div class="bento-spotlight magenta-spot"><div class="spotlight-num">{active_production}</div><div class="spotlight-lbl">In AI Production Pipeline</div></div>', unsafe_allow_html=True)

with metric_col3:
    st.markdown(f'<div class="bento-spotlight orange-spot"><div class="spotlight-num">{ready_demos}</div><div class="spotlight-lbl">Verified Showroom Ready</div></div>', unsafe_allow_html=True)

st.write("") # Vertical whitespace layout spacing


# ----------------------------------------------------
# Bento Grid Row 2: Main Operational Workspace Modules
# ----------------------------------------------------
row2_col1, row2_col2 = st.columns([1, 2]) # 1/3 Content vs 2/3 Data Grid Structure layout configuration

with row2_col1:
    # Tile A: Configuration Input Module
    with st.container(border=True):
        st.markdown('<div class="bento-title">Configure Asset</div>', unsafe_allow_html=True)
        with st.form("pipeline_form", clear_on_submit=True):
            proj_name = st.text_input("Project Name")
            display_type = st.selectbox("Target Hardware", ["The Wall (MicroLED)", "The Link (Modular LED)", "90° Anamorphic Corner Cube"])
            raw_concept = st.text_area("Core Asset Concept")
            stage = st.selectbox("Workflow State", ["1. Prompt Engineering", "2. Imagen 3 Render", "3. Veo 3.1 Animation", "4. Topaz Upscaling", "5. Live Demo Ready"])
            
            submit = st.form_submit_button("Deploy to Artboard")

        if submit and proj_name:
            project_id = f"SAM-{datetime.now().strftime('%M%S')}"
            new_entry = {
                "Project ID": project_id,
                "Project Name": proj_name,
                "Target Display": display_type,
                "Prompt Concept": raw_concept,
                "Status": stage,
                "Date Created": datetime.now().strftime("%d/%m/%Y") # en-AU standard local formatting
            }
            # Append new record to tracking state array
            updated_df = pd.concat([st.session_state.pipeline_data, pd.DataFrame([new_entry])], ignore_index=True)
            st.session_state.pipeline_data = updated_df
            
            # Direct background sync operation to save data changes onto storage media
            save_persistent_data(updated_df)
            st.rerun()

with row2_col2:
    # Tile B: Centralized Data Processing Dashboard Block
    with st.container(border=True):
        st.markdown('<div class="bento-title">Studio Production Data</div>', unsafe_allow_html=True)
        if st.session_state.pipeline_data.empty:
            st.info("Your canvas pipeline database is completely blank. Use the configuration module to deploy your first asset.")
        else:
            # Inline modifications to status cells or strings inside the table layer
            edited_df = st.data_editor(st.session_state.pipeline_data, use_container_width=True, num_rows="dynamic")
            
            # Detect table alterations and trigger background data synchronization
            if not edited_df.equals(st.session_state.pipeline_data):
                st.session_state.pipeline_data = edited_df
                save_persistent_data(edited_df)
                st.rerun()


# ----------------------------------------------------
# Bento Grid Row 3: Generation Studios & Export Services
# ----------------------------------------------------
row3_col1, row3_col2 = st.columns([1.5, 1.5]) # Symmetrical bottom-row container splits

with row3_col1:
    # Tile C: Anamorphic Prompt Engine Studio
    with st.container(border=True):
        st.markdown('<div class="bento-title">Anamorphic Prompt Engine</div>', unsafe_allow_html=True)
        st.write("Refine core concepts into optimised forced-perspective templates.")
        user_input = st.text_input("Enter target product core:", placeholder="e.g., Luxury watch, premium sedan...", key="bento_prompt_input")
        
        if st.button("Calculate Spatial Weights"):
            if user_input:
                st.markdown(f"""
                **Option A: 3D Pop-Out Effect (Forced Depth)**
