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
            
        .cross-grid {{
            display: grid;
            grid-template-columns: minmax(400px, 1fr) minmax(400px, 1fr);
            grid-template-rows: auto auto;
            width: 100%;
            max-width: 1400px;
            margin: 0 auto;
            position: relative;
        }}

        .cross-grid::before,
        .cross-grid::after {{
            content: "";
            position: absolute;
            background-color: #bbb;
        }}

        /* Horizontal center line */
        .cross-grid::before {{
            top: 50%;
            left: 0;
            width: 100%;
            height: 2px;
            transform: translateY(-1px);
        }}

        /* Vertical center line */
        .cross-grid::after {{
            left: 50%;
            top: 0;
            height: 100%;
            width: 2px;
            transform: translateX(-1px);
        }}

        .grid-cell {{
            padding: 40px 60px;
            font-family: Calibri, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            border: 1px solid #cccccc; /* Add border */
            box-sizing: border-box;
        }}

        .grid-cell h3 {{
            text-align: left;
            color: #003366;
            font-size: 35px;
            margin-bottom: 20px;
        }}

        .grid-cell ul {{
            font-size: 25px;
            padding-left: 20px;
            margin: 0;
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

# Insert the background div!
st.markdown('<div class="bg-container"></div>', unsafe_allow_html=True)

def topic_box_animated(title, points, delay=0.4):
    # st.markdown(f"<h3 style='text-align: center; color: #003366;'>{title}</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <h3 style="
        font-size: 25px;
        margin-bottom: 20px;
        text-align: justify;
        text-justify: inter-word;
        line-height: 1.4;
    ">
        {title}
    </h3>
    """, unsafe_allow_html=True)
    # st.markdown(f"<h3 class='fade-title'>{title}</h3>", unsafe_allow_html=True)
    container = st.container()
    with container:
        for point in points:
            # Remove any leading numbers like "1.", "2.", etc.
            clean_point = point.lstrip("1234567890. ").strip()
            st.markdown(f"<li style='font-size: 20px; margin-left: 15px;'><b>{clean_point}<b></li>", unsafe_allow_html=True)
            time.sleep(delay)

def main():
    st.set_page_config(layout="wide")
    
    # Example topics_data dictionary you already have:
    topics_data = {'Topic 1': ['Justification for military support based on local capability',
  'National caveats affecting deployment decisions',
  'Urgency and availability of response assets',
  'Coordination challenges between military and civilian operations',
  'Assessment of risks and hazards in affected areas',
  'Host nation priorities influencing support decisions',
  'Need for formal requests and clearances',
  'Concerns over strategic communications and visibility',
  'Potential for compounding dangers if unsupported',
  'Exit strategies and sustainability of deployed forces']}


    # Topic 1 Q1
    # topics = [
    #     "Immediate Needs and Assessment. What are the possible immediate needs of the Affected Country following the disaster? How can Assisting States assess the Affected State’s immediate needs without deploying a Needs Assessment Team?"
    # ]

    # # Topic 1 Q2
    # topics = [
    #     "Terms of Reference (TORs). In your respective groups, discuss the roles and responsibilities, and possible challenges when operating in the MNCC."
    # ]

    # # Topic 3 Q1
    # topics = [
    #     "Situation Assessment. How do the UXO threat and chemical leak impact humanitarian access and safety? What information gaps exist, and which agencies are best placed to fill them?"
    # ]

    # # Topic 3 Q2
    topics = [
        "Military-Civil Defence Asset (MCDA) Deployment. What factors should be considered before approving a request for MCDA? What are potential reasons to support the MCDA request? What are possible reasons not to support the request?"
    ]
    
    # # Topic 3 Q3
    # topics = [
    #     "Coordination and Communication. How can military assets be deployed without compromising humanitarian principles (neutrality, impartiality, independence)? What coordination mechanisms should be established between MNCC, UN ISCG, and NGOs to ensure smooth information flow?"
    # ]

    # # Topic 3 Q4
    # topics = [
    #     "Planning and Decision-Making. What are the expected outcomes and deliverables of the upcoming coordination meeting? What follow-up actions or reporting mechanisms should be established post-meeting?"
    # ]

    topic_box_animated(topics[0], topics_data.get("Topic 1", []))

if __name__ == "__main__":
    main()
