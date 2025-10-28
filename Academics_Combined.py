import streamlit as st
import time
import base64
import os

# Encode image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load background
bg_image_path = "background1.jpg"
if not os.path.exists(bg_image_path):
    st.error("background1.jpg not found!")
    st.stop()

bg_base64 = get_base64_image(bg_image_path)

# --- Custom CSS ---
st.set_page_config(layout="wide")
st.markdown(f"""
    <style>
        .bg-container {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            z-index: -1;
            background-image: url('data:image/png;base64,{bg_base64}');
            background-repeat: no-repeat;
            background-size: contain;
            background-position: bottom center;
            opacity: 0.15;
        }}
        .stApp {{
            background-color: rgba(255,255,255,0.0);
        }}
        .block-container {{
            background-color: rgba(255,255,255,0.0);
            padding: 2rem;
        }}
        .grid-cell h3 {{
            color: #003366;
            font-size: 35px;
            margin-bottom: 20px;
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="bg-container"></div>', unsafe_allow_html=True)


def topic_box_animated(title, points, delay=0.4):
    st.markdown(f"<h3>{title}</h3>", unsafe_allow_html=True)
    st.markdown("<ul>", unsafe_allow_html=True)
    for point in points:
        clean_point = point.lstrip("1234567890. ").strip()
        st.markdown(f"<li style='font-size:20px;'><b>{clean_point}</b></li>", unsafe_allow_html=True)
        time.sleep(delay)
    st.markdown("</ul>", unsafe_allow_html=True)


def main():
    st.set_page_config(layout="wide")
    
    topics_data = {
        'Topic 1': [
            "Point 1",
            "",
            "",
            "",
        ],
        'Topic 2': [
            "Point 2",
            "",
            "",
            "",
        ],
        'Topic 3': [
            "",
            "",
            "",
            "",
        ],
        'Topic 4': [
            "",
            "",
            "",
            "",
        ],
    }

    topics = [
        "Urban Search and Rescue (USAR)",
        "Maritime Search and Rescue (MSAR)",
        "CBRE impact during Natural Hazards",
        "Medical Responses during HADR",
    ]

    col1_row1, col2_row1 = st.columns([2, 2])
    with col1_row1:
        topic_box_animated(topics[0], topics_data["Topic 1"])
    with col2_row1:
        topic_box_animated(topics[1], topics_data["Topic 2"])

    st.markdown("<div style='margin: 50px 0;'></div>", unsafe_allow_html=True)

    col1_row2, col2_row2 = st.columns([2, 2])
    with col1_row2:
        topic_box_animated(topics[2], topics_data["Topic 3"])
    with col2_row2:
        topic_box_animated(topics[3], topics_data["Topic 4"])


if __name__ == "__main__":
    main()
