import streamlit as st
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader

# CSS for Light and Dark Themes
LIGHT_THEME = """
    <style>
    body { background-color: white; color: black; }
    .stApp { background-color: white; color: black; }

    /* Input and Button Styles */
    .stTextInput>div>input { background-color: white; color: black; }
    .stButton>button { background-color: white; color: black; }

    /* Sidebar Styles */
    [data-testid="stSidebar"] { background-color: #f8f9fa; color: black; }
    [data-testid="stSidebar"] .widget-label { color: black; }

    /* Title, Headings, and Widget Labels */
    h1, h2, h3, h4, h5, h6 { color: black; }
    .stRadio>div label, .stCheckbox>div label, .stTextInput label { 
        color: black !important; 
    }

    /* Code Block Styling */
    .element-container pre, .element-container code { 
        background-color: #f1f1f1; 
        color: black; 
    }
    </style>
"""

DARK_THEME = """
    <style>
    body { background-color: #2e2e2e; color: white; }
    .stApp { background-color: #2e2e2e; color: white; }

    /* Input and Button Styles */
    .stTextInput>div>input { background-color: #3e3e3e; color: white; }
    .stButton>button { background-color: #4e4e4e; color: white; }

    /* Sidebar Styles */
    [data-testid="stSidebar"] { background-color: #1e1e1e; color: white; }
    [data-testid="stSidebar"] .widget-label { color: white; }

    /* Title, Headings, and Widget Labels */
    h1, h2, h3, h4, h5, h6 { color: #f1f1f1; }
    .stRadio>div label, .stCheckbox>div label, .stTextInput label { 
        color: white !important; 
    }

    /* Code Block Styling - For Email Text */
    .element-container pre, .element-container code { 
        background-color: #1e1e1e; 
        color: #ffffff; 
    }

    /* Icon and Emoji Styles */
    .emoji { filter: invert(1); }
    </style>
"""

def create_streamlit_app(llm, portfolio, clean_text):
    # Sidebar Content
    with st.sidebar:
        st.title("⚙️ Options")
        
        ab_test_option = st.checkbox("Enable A/B Testing", value = False)
        
        theme = st.radio("Select Theme:", ("Light", "Dark"))

        if theme == "Dark":
            st.markdown(DARK_THEME, unsafe_allow_html = True)
        else:
            st.markdown(LIGHT_THEME, unsafe_allow_html = True)

        st.markdown("**About the Tool:**")
        st.write(
            "This outreach tool helps generate professional cold emails "
            "to connect with potential clients based on job postings. "
            "Input a URL containing post data of less than 6000 words."
        )

        st.markdown("[Leave Feedback](https://feedback.link)")

    # Main App Content
    st.title("💼 Professional Outreach Tool")
    url_input = st.text_input("Enter Job Posting URL")

    if st.button("Generate Email"):
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)

            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)

                if ab_test_option:
                    email_a, email_b = llm.write_ab_test_mails(job, links)
                    st.subheader("Variation A")
                    st.code(email_a, language = 'markdown')
                    st.subheader("Variation B")
                    st.code(email_b, language = 'markdown')
                else:
                    email = llm.write_mail(job, links)
                    st.code(email, language = 'markdown')

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout = "wide", page_title = "Outreach Tool", page_icon = "💼")
    create_streamlit_app(chain, portfolio, clean_text)
