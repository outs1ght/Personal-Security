import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Hi, I am Sven :wave:")
    st.title("A Data Analyst From Germany")
    st.write("I am passionate about finding ways to use Python and VBA to be more efficient")
    st.write("[Learn More >](https://www.python.org/)")



with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            This is just a practice website
            """
        )

        st.write("[Youtube Channel](https://www.python.org/)")

with st.container():
    st.write("---")
    st.header("How to contact me:")
    st.write("##")

contact_form = """
<form action="https://formsubmit.co/143gn0gr@duck.com" method="POST">
     <input type="hidden" name="_captcha" value="false">    
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form> 
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()