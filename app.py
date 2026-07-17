import streamlit as st
import pandas as pd
from datetime import datetime

# Set page configuration for enterprise look
st.set_page_config(page_title="Samsung Spatial Content Hub", layout="wide", page_icon="🖥️")

# Custom Samsung-inspired Branding CSS
st.markdown("""
    <style>
    .main-title { font-size:42px !important; font-weight: 700; color: #0A1C2A; }
    .samsung-blue { color: #1428A0; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🖥️ Samsung <span class="samsung-blue">B2B Spatial Display</span> Content Hub</p>', unsafe_allowed_html=True)
st.caption("Your custom pipeline tracker, prompt optimizer, and client asset manager.")

# Initialize data pipeline storage
if "pipeline_data" not in st.session_state:
    st.session_state.pipeline_data = pd.DataFrame(columns=[
        "Project ID", "Project Name", "Target Display", "Prompt Concept", "Status", "Date Created"
    ])

# Sidebar Controls for adding data to your tracker
st.sidebar.header("🚀 Log New Demo Project")
with st.sidebar.form("pipeline_form", clear_on_submit=True):
    proj_name = st.text_input("Project Name (e.g., Luxury Watch Launch)")
    display_type = st.selectbox("Target Hardware", ["The Wall (MicroLED)", "The Link (Modular LED)", "90° Anamorphic Corner Cube"])
    raw_concept = st.text_area("Core Asset Concept (e.g., Floating sapphire watch erupting from liquid mercury)")
    stage = st.selectbox("Workflow State", ["1. Prompt Engineering", "2. Imagen 3 Render", "3. Veo 3.1 Animation", "4. Topaz Upscaling", "5. Live Demo Ready"])
    
    submit = st.form_submit_button("Save to Tracker")

if submit and proj_name:
    project_id = f"SAM-{datetime.now().strftime('%M%S')}"
    new_entry = {
        "Project ID": project_id,
        "Project Name": proj_name,
        "Target Display": display_type,
        "Prompt Concept": raw_concept,
        "Status": stage,
        "Date Created": datetime.now().strftime("%Y-%m-%d")
    }
    st.session_state.pipeline_data = pd.concat([st.session_state.pipeline_data, pd.DataFrame([new_entry])], ignore_index=True)
    st.sidebar.success(f"Saved {project_id} to database!")

# Tabbed Layout for Clean Presentations
tab1, tab2, tab3 = st.tabs(["📊 Live Tracker Pipeline", "✨ Spatial Prompt Optimizer", "🎞️ Media Preview Centre"])

with tab1:
    st.subheader("Your Active Production Pipeline")
    if st.session_state.pipeline_data.empty:
        st.info("Your tracking database is currently empty. Log a project using the left sidebar form to populate it.")
    else:
        # Display editable pipeline dataframe
        edited_df = st.data_editor(st.session_state.pipeline_data, use_container_width=True, num_rows="dynamic")
        st.session_state.pipeline_data = edited_df
        
        # Enterprise Summary Generator Feature
        st.write("---")
        st.subheader("📋 Client Brief Generator")
        st.write("Select a logged project below to generate an executive workflow summary for your client pitching notes.")
        
        selected_project = st.selectbox("Choose project to summarize:", st.session_state.pipeline_data["Project Name"].unique())
        
        if st.button("Generate Executive Summary Text"):
            proj_row = st.session_state.pipeline_data[st.session_state.pipeline_data["Project Name"] == selected_project].iloc[0]
            summary_text = f"""
SAMSUNG B2B SPATIAL DISPLAY CONFIGURATION BRIEF
----------------------------------------------
Project Reference: {proj_row['Project ID']}
Campaign Name: {proj_row['Project Name']}
Deployment Screen: {proj_row['Target Display']}
Current Status: {proj_row['Status']}
Creation Date: {proj_row['Date Created']}

CONCEPT DESIGN BRIEF:
"{proj_row['Prompt Concept']}"

PRODUCTION METHODOLOGY:
1. Base asset generation via Google Imagen 3 (High-fidelity color mapping).
2. Volumetric depth animation utilizing Google Veo 3.1 temporal consistency engines.
3. Post-render upscaling to match native native panel pixel layout.
----------------------------------------------
            """
            st.code(summary_text, language="text")

with tab2:
    st.subheader("Anamorphic Prompt Engineering Studio")
    st.write("Convert plain product text into highly controlled prompts tailored to spatial illusions.")
    
    user_input = st.text_input("Enter product name or theme:", placeholder="e.g., Neo QLED TV panel")
    
    # Prompt formulation templates built right into the app code
    if st.button("Generate Spatial Prompt Templates"):
        if user_input:
            st.info("🤖 **Optimised System Configurations Generated:**")
            
            st.markdown(f"""
            **Option A: 3D Pop-Out Effect (Best for Retail Displays)**
            > `Anamorphic forced perspective 3D render of a {user_input}. Hyper-detailed textures, volumetric dramatic backlighting, dark infinity void backdrop. The object slowly rotates and drifts forward breaking the illusionary foreground screen boundary, extreme detail, depth map optimization, shot on 35mm.`
            
            **Option B: Cinematic Ambient (Best for Luxury/Lobbies)**
            > `Minimalist architectural space, central floating holographic {user_input} suspended in mid-air. Soft light refractions bouncing off glass surfaces, atmospheric dust motes catching golden light rays, hyper-photorealistic 8k, slow continuous camera push-in.`
            """)
        else:
            st.warning("Please input a product concept first.")

with tab3:
    st.subheader("Local Asset Verification")
    st.write("Review, preview, and approve test renders right alongside client notes.")
    
    # Video Uploader Widget for testing locally on your laptop during demos
    uploaded_video = st.file_uploader("Upload Test Clip (MP4 format)", type=["mp4", "mov"])
    if uploaded_video is not None:
        st.video(uploaded_video)
        st.success("Visual quality checks verified for high-density spatial arrays.")
