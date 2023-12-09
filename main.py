import base64
import plotly.express as px
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Elliana's Blog", page_icon="😉", layout="wide")

df = px.data.iris()

@st.cache_data
def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()


img = get_img_as_base64("back.jpg")
page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-size: 110%;
    background-attachment: local;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# ---- LOAD ASSETS ----
img_contact_form = Image.open("premarital.jpg")
img_lottie_animation = Image.open("image23.jpg")

# ---- HEADER SECTION ----

with st.container():
    cols1, cols2 = st.columns([3,1])
    with cols1:
        st.subheader("Hi there!,Welcome to Elliana Jane's Blog :wave:")
        st.title("A BSCpE Student from SNSU")
        st.write(
            "In the Language of Logic, We Shape Tomorrow's Reality."
        )
    with cols2:
        st.image("propic.png")
        st.write("[Learn More About](https://www.facebook.com/ellianajane.terrazula.3)")
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.title("📣Pre-Marital sex and Early Pregnancy Compaign📣")
    left_column, right_column = st.columns(2)
    with left_column:
         col1, col2 = st.columns(2)
        
    v1 = col1.button("Awareness Compaign🎤")
    if v1:
            with st.container():
                col1, col2,  = st.columns(2)
                # Replace 'your_video_file1.mp4' and 'your_video_file2.mp4' with the paths to your video files
                with col1:
                   st.write("""
                            Understanding Pre-Marital Sex:

                                - Define pre-marital sex and stress the importance of informed decisions.
                            Relationship Dynamics:

                                - Emphasize open communication, mutual respect, and shared decision-making.
                            Safe Practices:

                            - Briefly highlight contraception methods and responsible sexual health practices.
                            Early Pregnancy Awareness:

                            - Provide quick info on early signs and available support services.
                            Embracing Choices:

                            - Encourage respecting diverse choices and challenging societal stigmas.
                            Supportive Communities:

                            - Highlight the importance of non-judgmental communities and share real stories.
                                                        
                            
                            """)
                with col2:
                    st.image("aware.jpg")
            st.write("[Read More >](https://starlegacyfoundation.org/awareness-month/#:~:text=If%20you%20or%20someone%20you,and%20Infant%20Loss%20Awareness%20Month)")
    v2 = col2.button("Prevention Tips🙅‍♀️")
    if v2:
            with st.container():
                col1, col2,  = st.columns(2)
                # Replace 'your_video_file1.mp4' and 'your_video_file2.mp4' with the paths to your video files
                with col1:
                   st.write("""
                           Education:

                                - Stay informed about contraception methods.
                                Understand emotional and physical aspects of pre-marital sex.
                                Communication:

                                - Establish open communication with your partner.
                                Discuss expectations, boundaries, and family planning.
                                Contraception:

                                - Choose a suitable method and use it consistently.
                                Consider dual protection for added security.
                                Health Check-ups:

                                - Schedule regular check-ups for reproductive health.
                                Consult healthcare professionals for family planning advice.
                                Set Boundaries:

                                - Clearly define and communicate personal boundaries.
                                Ensure decisions are mutual and consensual.
                                Community Support:

                                - Surround yourself with a supportive community.
                                Seek guidance when needed from friends, family, or support groups.
                                Write to Elliana
                                        
                            
                            """)
                with col2:
                    st.image("prevention.jpg")
            st.write("[Read More >](https://stoptherise.initiatives.qld.gov.au/blog/9-contraception-options)")
# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Defination of Terms📕")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Pregnancy")
        st.write(
            """
            Definition: 
            - The physiological condition in which a woman carries and nurtures a developing fetus within her uterus. It begins with fertilization, followed by implantation of the embryo onto the uterine wall, and typically lasts about 40 weeks, divided into three trimesters, until childbirth.
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=4l9GE_eaMSs)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("♀️Pre-Marital Sex♂️")
        st.write(
            """
           Definition:
           - Sexual activity or intercourse between individuals who are not married to each other. This term refers to consensual and voluntary engagement in sexual relations before formalizing a marital union
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=CA_yTgh6g48)")

# ---- CONTACT ----
st.markdown("---")    
st.header(":mailbox: Get In Touch With Me!")
contact_form = """
        <form action="https://formsubmit.co/mark.anthony.alegre05@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
        </form>
        """
st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
def local_css(file_name):
                with open(file_name) as f:
                        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")