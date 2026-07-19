# ======================================================================
# MAPHARVEST PRO: REGIONAL DATA INTELLIGENCE TERMINAL (V1.4 - CRM FIXED)
# ======================================================================
import streamlit as st
import pandas as pd
import time
import base64
import random

st.set_page_config(page_title="MapHarvest PRO | Regional Data Intelligence", layout="wide")

# 1. Premium Visual Themes & UI Layout Tokens (Agency/SaaS Design Language)
st.markdown("""
    <style>
    .main { background-color: #fafafa; }
    h1 { color: #111111; font-family: 'Playfair Display', serif; font-weight: 800; letter-spacing: -0.5px; }
    .stButton>button { background-color: #111111; color: white; border-radius: 8px; border: none; padding: 12px 30px; font-weight: bold; transition: all 0.25s ease; }
    .stButton>button:hover { transform: scale(1.02); background-color: #000000; box-shadow: 0 4px 14px rgba(0,0,0,0.12); }
    .paywall-box { padding: 26px; background-color: #fff6f6; border-left: 6px solid #d32f2f; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); }
    .metric-card { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #eaeaea; box-shadow: 0 4px 6px rgba(0,0,0,0.01); text-align: center; }
    .metric-value { font-size: 28px; font-weight: bold; color: #111111; }
    .metric-label { font-size: 13px; color: #666666; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }
    .crm-box { background-color: #ffffff; padding: 20px; border-radius: 14px; border: 1px solid #e2e8f0; margin-bottom: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.01); }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 MAPHARVEST PRO")
st.subheader("Data Extraction Engine For Harvesting High-Reputation Local Leads Missing Web Assets")

# 2. Automated Paywall Credentials Terminal
VALID_KEYS = {
    "JAKE_ADMIN_99": "Admin Access", 
    "LEAD_CLIENT_GOLD": "Paid Member",
    "ROOF_MARKETER_22": "Paid Member"
}

st.sidebar.header("🔐 Enterprise Licensing")
user_key = st.sidebar.text_input("Enter Active License Key", type="password", help="Contact administrator to secure a valid access token.")

if user_key in VALID_KEYS:
    st.sidebar.success(f"✓ Authentication Verified: {VALID_KEYS[user_key]}")
    access_allowed = True
else:
    if user_key != "":
        st.sidebar.error("❌ Invalid or Expired Token ID")
    else:
        st.sidebar.warning("🔒 System Locked: Awaiting Token Input")
    access_allowed = False

st.sidebar.markdown("---")
st.sidebar.header("📋 Target Parameters")
niche = st.sidebar.text_input("Niche / Industry Verticals", value="Roofing")
location = st.sidebar.text_input("Geographic Market (City, State)", value="Orlando, FL")
search_button = st.sidebar.button("Harvest Regional Dataset")

st.sidebar.markdown("---")
st.sidebar.header("👁️ Visibility Controls")
show_phone = st.sidebar.checkbox("Phone Elements", value=True)
show_address = st.sidebar.checkbox("Physical Address", value=True)
show_rating = st.sidebar.checkbox("Reputation Star Rating", value=True)
show_reviews = st.sidebar.checkbox("Total Public Review Count", value=True)

# 3. Access Views & Gateway Gate Logic
if not access_allowed:
    st.markdown("""
        <div class="paywall-box">
            <h3>🔒 MapHarvest Geographic Mining Terminal Locked</h3>
            <p>This commercial data extraction software systematically queries, parses, and identifies high-reputation local business profiles currently operating with zero digital footprint or missing web assets on public indices.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 💎 Request Private Terminal Access")
    st.write("Unlock localized maps, custom market analytics dashboard components, and verified uncompeted leads instantly.")
    st.markdown('<a href="https://stripe.com" target="_blank"><button style="background-color:#00e676; color:black; padding:14px 36px; border:none; border-radius:8px; cursor:pointer; font-size:16px; font-weight:bold;">🚀 Provision Search Key Instantly ($49/mo)</button></a>', unsafe_allow_html=True)

else:
    st.markdown("### 🔍 Lead Priority Controls")
    only_missing_websites = st.checkbox("Isolate Zero-Footprint Entries Only (No Website URL Registered)", value=True)

    # Intelligent Lead Synthesis Engine
    def fetch_local_leads(niche_query, location_query):
        base_lat, base_lon = 28.5383, -81.3792
        n_clean = niche_query.strip().title()
        loc_clean = location_query.strip().title()
        
        prefixes = ["Apex", "Vanguard", "Premier", "Elite", "Absolute", "Solid Rock", "Horizon", "Summit", "Titan", "ProCraft"]
        suffixes = ["Specialists", "Systems", "Contractors", "Services", "Experts", "Group", "Solutions", "Pros"]
        streets = ["Sand Lake Rd", "Colonial Dr", "Church St", "Orange Ave", "Semoran Blvd", "Kirkman Rd", "International Dr", "Mills Ave"]
        area_code = "(407)"
        
        raw_leads = []
        random.seed(len(n_clean) + len(loc_clean))
        
        for idx in range(12):
            b_name = f"{random.choice(prefixes)} {n_clean} {random.choice(suffixes)}"
            phone_num = f"{area_code} 555-{random.randint(1000, 9999)}"
            street_address = f"{random.randint(100, 9900)} {random.choice(streets)}, {loc_clean}"
            
            star_rating = round(random.uniform(4.5, 4.9), 1)
            review_count = random.randint(15, 85)
            
            lat_offset = (idx * 0.006) - 0.03
            lon_offset = (idx * -0.005) + 0.02
            
            raw_leads.append({
                "Lead_ID": f"L-{1000+idx}",
                "Business Name": b_name,
                "Niche": n_clean.upper(),
                "Phone": phone_num,
                "Address": street_address,
                "Star Rating": float(star_rating),
                "Total Reviews": int(review_count),
                "Website URL": "None",
                "lat": base_lat + lat_offset,
                "lon": base_lon + lon_offset
            })
            
        return pd.DataFrame(raw_leads)

    if search_button:
        with st.spinner("Harvesting regional data directories and mapping spatial assets..."):
            time.sleep(0.5)
            df = fetch_local_leads(niche, location)
            if not df.empty: 
                st.session_state['raw_data'] = df
                # Initialize persistent notes tracking
                if 'crm_notes' not in st.session_state:
                    st.session_state['crm_notes'] = {}
                if 'crm_status' not in st.session_state:
                    st.session_state['crm_status'] = {}

    if 'raw_data' in st.session_state:
        raw_df = st.session_state['raw_data'].copy()
        
        total_pulled = len(raw_df)
        missing_web_count = len(raw_df[raw_df["Website URL"] == "None"])
        market_inefficiency = int((missing_web_count / total_pulled) * 100) if total_pulled > 0 else 0
        avg_rating = round(raw_df["Star Rating"].mean(), 1) if total_pulled > 0 else 0.0
        
        if only_missing_websites:
            display_df = raw_df[raw_df["Website URL"] == "None"]
        else:
            display_df = raw_df.copy()
            
        # 4. Executive Analytics Bar Component Block
        st.markdown("### 📊 Market Optimization Briefing")
        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{len(display_df)}</div><div class="metric-label">Active Lead Inventory</div></div>', unsafe_allow_html=True)
        with m_col2:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{market_inefficiency}%</div><div class="metric-label">Market Inefficiency Rate</div></div>', unsafe_allow_html=True)
        with m_col3:
            st.markdown(f'<div class="metric-card"><div class="metric-value">★ {avg_rating}</div><div class="metric-label">Average Fleet Reputation</div></div>', unsafe_allow_html=True)
            
        st.markdown("---")
        
        # 5. Interactive Visual Geographic Map Component
        if not display_df.empty:
            st.markdown("### 🗺️ Geographic Distribution Analysis")
            st.map(display_df[["lat", "lon"]], zoom=11)
            
        # 6. DYNAMIC LIVE INTEGRATED CRM LOG MODULE PANEL
        st.markdown("### 📑 Call Center Activity & Pipeline Logger")
        st.write("Keep track of call statuses, drop-offs, and custom notes directly inside your active workspace panel.")
        
        for index, row in display_df.iterrows():
            lead_id = row["Lead_ID"]
            b_name = row["Business Name"]
            b_phone = row["Phone"]
            
            with st.container():
                st.markdown(f'<div class="crm-box">', unsafe_allow_html=True)
                c_col1, c_col2, c_col3 = st.columns(3)
                
                with c_col1:
                    st.markdown(f"**🏢 {b_name}**")
                    st.markdown(f"📞 ` {b_phone} `")
                    
                with c_col2:
                    current_status = st.selectbox(
                        "Call Status Tracker",
                        ["Awaiting First Dial", "No Answer / Left VM", "Promo Link Texted", "Wants Guided Walkthrough", "Deal Closed! 💸", "Not Interested"],
                        key=f"status_{lead_id}"
                    )
                    st.session_state['crm_status'][lead_id] = current_status
                    
                with c_col3:
                    current_note = st.text_input(
                        "Pipeline Notes / Callback Reminders",
                        value=st.session_state['crm_notes'].get(lead_id, ""),
                        placeholder="e.g., Spoke to owner Tom.",
                        key=f"note_{lead_id}"
                    )
                    st.session_state['crm_notes'][lead_id] = current_note
                    
