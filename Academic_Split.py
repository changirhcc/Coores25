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
    
    topics_data = {'Topic 1': ['Effective communication and coordination with local authorities',
  'Importance of local knowledge and resources for operations',
  'Addressing language barriers in multi-national teams',
  'Prioritisation of human lives and essential supplies',
  'Need for proper training and preparedness of teams',
  'Challenges in navigating legal and political constraints',
  'Regular updates and information sharing among teams',
  'Utilisation of technology for coordination and mapping',
  'Ensuring team rest and rotation for effectiveness',
  'Establishing clear command structures and leadership'],
 'Topic 4': ['Coordination between military and civilian teams',
  'Ensuring equitable access for vulnerable populations',
  'Cultural considerations in healthcare delivery',
  'Logistics challenges in remote healthcare access',
  'Importance of neutrality and respect for sovereignty',
  'Need for clear roles to avoid duplication',
  'Open information sharing for effective response',
  'Credentials and standards for foreign medical teams',
  'Addressing psychosocial support and trauma care',
  'Building trust and mutual respect among teams'],
 'Topic 2': ['Coordination challenges between military and civilian entities',
  'Importance of situational awareness and real-time information sharing',
  'Need for standardised SOPs and training across teams',
  'Defining clear roles and responsibilities in SAR operations',
  'Utilisation of technology for detection and communication',
  'Impact of weather and sea conditions on operations',
  'Collaboration and interoperability among international stakeholders',
  'Effective management of resources and assets during SAR',
  'Establishing a centralised Rescue Coordination Centre',
  'Addressing language barriers in communication and coordination'],
 'Topic 3': ['Need for appropriate detection capabilities',
  'Challenges in training for CBRE missions',
  'Importance of public warning systems',
  'Coordination difficulties among various agencies',
  'Risks of contamination from natural disasters',
  'Necessity for effective PPE preparation',
  'Limited resources for manufacturing PPE',
  'Awareness of incident locations and scopes',
  'Need for knowledge sharing on CBRE risks',
  'Importance of realistic training exercises']}


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
