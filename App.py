import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AdForge AI",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background-color: #f7f8fc;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}

section[data-testid="stSidebar"] * {
    color: white;
}

.logo {
    font-size: 25px;
    font-weight: 800;
    color: white;
    margin-bottom: 30px;
}

.hero {
    background: linear-gradient(135deg, #5b4bdb, #7c5cff);
    padding: 35px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 38px;
    margin-bottom: 8px;
}

.hero p {
    font-size: 17px;
    opacity: 0.9;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
}

.metric {
    font-size: 30px;
    font-weight: 800;
    color: #111827;
}

.label {
    color: #6b7280;
    font-size: 14px;
}

.ad-preview {
    background: linear-gradient(145deg, #ede9fe, #ddd6fe);
    height: 350px;
    border-radius: 18px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 25px;
}

.ad-preview h2 {
    font-size: 30px;
    color: #111827;
}

.ad-preview p {
    color: #4b5563;
}

.badge {
    background: #ede9fe;
    color: #5b4bdb;
    padding: 6px 12px;
    border-radius: 20px;
    font-size: 12px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------

with st.sidebar:

    st.markdown(
        '<div class="logo">✨ AdForge AI</div>',
        unsafe_allow_html=True
    )

    page = st.radio(
        "MENU",
        [
            "Dashboard",
            "Create Ad",
            "My Creatives",
            "Templates",
            "Brand Kit",
            "Analytics",
            "Settings"
        ]
    )

    st.markdown("---")

    st.markdown("### AI Credits")

    st.progress(0.72)

    st.caption("72 / 100 credits used")

    st.markdown("---")

    st.write("👤 Shreyash")
    st.caption("Free Plan")


# ============================================================
# DASHBOARD
# ============================================================

if page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <h1>Create high-converting ads with AI ✨</h1>
        <p>
        Generate professional advertising creatives, copy and campaigns
        in seconds.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("＋ Create New Ad", use_container_width=False):
        st.session_state["page"] = "Create Ad"

    st.markdown("## Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
        <div class="label">Total Creatives</div>
        <div class="metric">128</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <div class="label">Impressions</div>
        <div class="metric">24.8K</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <div class="label">Engagement</div>
        <div class="metric">8.6%</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
        <div class="label">Conversions</div>
        <div class="metric">1,284</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("## Recent Creatives")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
        <div class="ad-preview">
        <span class="badge">Instagram</span>
        <h2>Summer Sale</h2>
        <p>Up to 50% OFF</p>
        <strong>SHOP NOW →</strong>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <div class="ad-preview">
        <span class="badge">Facebook</span>
        <h2>New Collection</h2>
        <p>Discover something new.</p>
        <strong>EXPLORE →</strong>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <div class="ad-preview">
        <span class="badge">LinkedIn</span>
        <h2>Grow Your Business</h2>
        <p>Powerful tools for modern teams.</p>
        <strong>LEARN MORE →</strong>
        </div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# CREATE AD
# ============================================================

elif page == "Create Ad":

    st.title("✨ Create New Ad")
    st.caption("Tell AI about your product and generate a complete advertising creative.")

    left, right = st.columns([1, 1])

    with left:

        st.markdown("### Campaign Details")

        product = st.text_input(
            "Product / Brand Name",
            placeholder="e.g. Nike Air Max"
        )

        description = st.text_area(
            "Product Description",
            placeholder="Describe your product or service..."
        )

        audience = st.text_input(
            "Target Audience",
            placeholder="e.g. College students aged 18-25"
        )

        objective = st.selectbox(
            "Campaign Objective",
            [
                "Brand Awareness",
                "Conversions",
                "Website Traffic",
                "Lead Generation",
                "Product Launch"
            ]
        )

        platform = st.multiselect(
            "Advertising Platforms",
            [
                "Instagram",
                "Facebook",
                "Google Ads",
                "LinkedIn"
            ],
            default=["Instagram"]
        )

        format_type = st.selectbox(
            "Ad Format",
            [
                "Square 1:1",
                "Portrait 4:5",
                "Story 9:16",
                "Landscape 16:9"
            ]
        )

        tone = st.selectbox(
            "Brand Tone",
            [
                "Professional",
                "Friendly",
                "Bold",
                "Luxury",
                "Playful"
            ]
        )

        cta = st.selectbox(
            "Call To Action",
            [
                "Shop Now",
                "Learn More",
                "Get Started",
                "Sign Up",
                "Buy Now"
            ]
        )

        generate = st.button(
            "✨ Generate Creative",
            use_container_width=True
        )

    with right:

        st.markdown("### Live Preview")

        if generate:

            if product == "":
                product = "Your Product"

            st.markdown(f"""
            <div class="ad-preview">

                <span class="badge">
                {platform[0] if platform else "Social Media"}
                </span>

                <h2>
                {product}
                </h2>

                <p>
                Discover something amazing designed
                especially for you.
                </p>

                <strong>
                {cta.upper()} →
                </strong>

            </div>
            """, unsafe_allow_html=True)

            st.success("🎉 Your AI creative is ready!")

            st.markdown("### AI Generated Copy")

            st.info(
                f"**Headline:** Discover {product} Like Never Before"
            )

            st.write(
                f"Transform your experience with {product}. "
                "Designed to deliver quality, performance and style."
            )

            st.button("↻ Regenerate")
            st.button("✏️ Edit Creative")
            st.button("⬇️ Download")

        else:

            st.markdown("""
            <div class="ad-preview">

                <h2>✨ AI Creative Preview</h2>

                <p>
                Your generated advertisement will appear here.
                </p>

            </div>
            """, unsafe_allow_html=True)


# ============================================================
# MY CREATIVES
# ============================================================

elif page == "My Creatives":

    st.title("🎨 My Creatives")
    st.caption("Manage all your generated advertisements.")

    search = st.text_input(
        "🔍 Search creatives",
        placeholder="Search by campaign or product..."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.selectbox(
            "Platform",
            ["All", "Instagram", "Facebook", "Google", "LinkedIn"]
        )

    with col2:
        st.selectbox(
            "Sort",
            ["Newest", "Oldest", "Best Performing"]
        )

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    ads = [
        ("Summer Sale", "Instagram"),
        ("New Collection", "Facebook"),
        ("Business Growth", "LinkedIn")
    ]

    for col, (title, platform_name) in zip(
        [c1, c2, c3], ads
    ):

        with col:

            st.markdown(f"""
            <div class="card">

            <div class="ad-preview">
            <span class="badge">{platform_name}</span>
            <h2>{title}</h2>
            <p>AI generated advertisement</p>
            <strong>SHOP NOW →</strong>
            </div>

            <br>

            <b>{title}</b>

            </div>
            """, unsafe_allow_html=True)

            st.button(
                "Edit",
                key=title
            )


# ============================================================
# TEMPLATES
# ============================================================

elif page == "Templates":

    st.title("📚 Ad Templates")
    st.caption("Start with a professional template.")

    category = st.selectbox(
        "Category",
        [
            "All Templates",
            "Social Media",
            "E-commerce",
            "Product Launch",
            "Promotions",
            "Brand Awareness"
        ]
    )

    st.markdown("---")

    cols = st.columns(3)

    templates = [
        "Modern Product",
        "Flash Sale",
        "Minimal Business",
        "New Launch",
        "Luxury Brand",
        "Social Promotion"
    ]

    for i, template in enumerate(templates):

        with cols[i % 3]:

            st.markdown(f"""
            <div class="card">

            <div class="ad-preview">
            <h2>{template}</h2>
            <p>Professional AI-ready template</p>
            </div>

            </div>
            """, unsafe_allow_html=True)

            st.button(
                "Use Template",
                key=f"template_{i}",
                use_container_width=True
            )


# ============================================================
# BRAND KIT
# ============================================================

elif page == "Brand Kit":

    st.title("🎯 Brand Kit")
    st.caption("Keep your advertising creatives consistent.")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Brand Information")

        st.text_input(
            "Brand Name",
            placeholder="Your brand name"
        )

        st.text_area(
            "Brand Voice",
            placeholder="Describe your brand personality..."
        )

        st.file_uploader(
            "Upload Brand Logo",
            type=["png", "jpg", "jpeg"]
        )

    with col2:

        st.markdown("### Brand Colors")

        color1 = st.color_picker(
            "Primary Color",
            "#5B4BDB"
        )

        color2 = st.color_picker(
            "Secondary Color",
            "#111827"
        )

        st.markdown("### Typography")

        st.selectbox(
            "Font",
            [
                "Inter",
                "Roboto",
                "Poppins",
                "Montserrat"
            ]
        )

    st.button(
        "💾 Save Brand Kit",
        use_container_width=True
    )


# ============================================================
# ANALYTICS
# ============================================================

elif page == "Analytics":

    st.title("📊 Analytics")
    st.caption("Track the performance of your advertising creatives.")

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("Impressions", "24.8K"),
        ("Clicks", "4.2K"),
        ("CTR", "8.6%"),
        ("Conversions", "1,284")
    ]

    for col, (label, value) in zip(
        [c1, c2, c3, c4],
        metrics
    ):

        with col:

            st.markdown(f"""
            <div class="card">
            <div class="label">{label}</div>
            <div class="metric">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("## Campaign Performance")

    chart_data = {
        "Monday": 120,
        "Tuesday": 180,
        "Wednesday": 150,
        "Thursday": 240,
        "Friday": 310,
        "Saturday": 280,
        "Sunday": 350
    }

    st.line_chart(chart_data)

    st.markdown("## Top Performing Creatives")

    st.dataframe(
        {
            "Creative": [
                "Summer Sale",
                "New Collection",
                "Business Growth",
                "Product Launch"
            ],
            "CTR": [
                "12.4%",
                "10.8%",
                "9.6%",
                "8.9%"
            ],
            "Conversions": [
                420,
                315,
                286,
                241
            ]
        },
        use_container_width=True
    )


# ============================================================
# SETTINGS
# ============================================================

elif page == "Settings":

    st.title("⚙️ Settings")

    st.markdown("### Account")

    st.text_input(
        "Name",
        value="Shreyash"
    )

    st.text_input(
        "Email",
        value="shreyash@example.com"
    )

    st.markdown("### Preferences")

    st.toggle(
        "Email Notifications",
        value=True
    )

    st.toggle(
        "AI Suggestions",
        value=True
    )

    st.markdown("### Subscription")

    st.info("Free Plan — 100 AI credits")

    st.button(
        "Upgrade to Pro",
        use_container_width=True
    )