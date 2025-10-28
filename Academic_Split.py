import streamlit as st
import time
import base64
import os

# Encode image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load image
bg_image_path = "background1.jpg"
if not os.path.exists(bg_image_path):
    st.error("background.jpg not found!")
    st.stop()

bg_base64 = get_base64_image(bg_image_path)

# --- Custom CSS for layout and style ---
st.set_page_config(layout="wide")
st.markdown(f"""
    <style>
        /* Background Image as fixed div */
        .bg-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: -1;
            background-image: url('data:image/png;base64,{bg_base64}');
            background-repeat: no-repeat;
            background-size: contain;
            background-position: bottom center;
            opacity: 0.15;
        }}

        /* Make the main app and containers transparent */
        .stApp {{
            background-color: rgba(255, 255, 255, 0.0);
        }}
        .block-container {{
            background-color: rgba(255, 255, 255, 0.0);
            padding: 2rem;
            border-radius: 8px;
        }}
            
        .grid-cell {{
            padding: 40px 60px;
            font-family: Calibri, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            border: 1px solid #cccccc;
            box-sizing: border-box;
        }}

        .grid-cell h3 {{
            text-align: justify;
            text-justify: inter-word;
            color: #003366;
            font-size: 35px;
            margin-bottom: 20px;
            line-height: 1.4;
        }}

        .grid-cell ul {{
            font-size: 25px;
            padding-left: 20px;
            margin: 0;
            text-align: justify;
            text-justify: inter-word;
        }}

        .fade-title {{
            opacity: 0;
            animation: fadeIn 1s forwards;
            animation-delay: 0.1s;
        }}

        @keyframes fadeIn {{
            to {{
                opacity: 1;
            }}
        }}

        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        .st-emotion-cache-13ln4jf {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# Insert the background div
st.markdown('<div class="bg-container"></div>', unsafe_allow_html=True)


# --- Animated topic box function ---
def topic_box_animated(title, points, delay=0.4):
    st.markdown(f"""
        <h3 style="
            font-size: 35px;
            margin-bottom: 20px;
            text-align: justify;
            text-justify: inter-word;
            line-height: 1.4;
        ">
            {title}
        </h3>
    """, unsafe_allow_html=True)

    container = st.container()
    with container:
        for point in points:
            clean_point = point.lstrip("1234567890. ").strip()
            st.markdown(f"<li style='font-size: 20px; margin-left: 15px; text-align: justify; text-justify: inter-word;'><b>{clean_point}</b></li>", unsafe_allow_html=True)
            time.sleep(delay)


# --- Main App ---
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
        "Medical Responses during HADR"
    ]

    # Create tabs for each topic
    tab1, tab2, tab3, tab4 = st.tabs(topics)

    with tab1:
        topic_box_animated(topics[0], topics_data.get("Topic 1", []))

    with tab2:
        topic_box_animated(topics[1], topics_data.get("Topic 2", []))

    with tab3:
        topic_box_animated(topics[2], topics_data.get("Topic 3", []))

    with tab4:
        topic_box_animated(topics[3], topics_data.get("Topic 4", []))


if __name__ == "__main__":
    main()
