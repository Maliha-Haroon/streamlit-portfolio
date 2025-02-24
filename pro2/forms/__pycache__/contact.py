import streamlit as st 

# Contact Form Function
def show_contact_form():
    with st.form("contact_form"):
        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="Enter your email")
        message = st.text_area("Message", placeholder="Write your message here")
        submit_button = st.form_submit_button("Send Message")
        
        # Handling form submission
        if submit_button:
            if name and email and message:
                st.success(f"Thank you, {name}! Your message has been received.")
            else:
                st.error("Please fill out all fields before submitting.")

    # Social Media Links inside the form
    st.subheader("Connect with me:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[LinkedIn](https://www.linkedin.com/in/maliha-haroon-08b037294/)")
    with col2:
        st.markdown("[GitHub](https://github.com/Maliha-Haroon)")
    with col3:
        st.markdown("[Twitter](https://twitter.com/Malihaharoo8165)")

# Hero Section
col1, col2 = st.columns([1, 2], gap="small")
with col1:
    st.image("./assets/image.1.PNG", width=230)

with col2:
    st.title("Maliha Haroon")
    st.write("Junior Data Analyst & Full Stack Developer")
    
    # Contact Me Button
    if st.button("✉️ Contact Me"):
        show_contact_form()
