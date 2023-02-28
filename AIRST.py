import streamlit as st
#from pages.Search_for_papers import Search_for_papers
#from pages.Upload import Upload
from pages.Summarize import Summarize
from pages.Ask_Everything import Ask_Everything

# Create a Streamlit app with sidebar


def main():
    st.set_page_config(page_title='AI Research Summary Tool',
                       page_icon=':medical_symbol:', layout='wide')

    st.title(
        ':medical_symbol: :blue[AI R]esearch :blue[S]ummary :blue[T]ool   	')
    # Set background color and font style
    st.write('\n')
    st.markdown(
        '<style>body {background-color: #f5f5f5; font-family: Arial;}</style>', unsafe_allow_html=True)

    # Add a banner image
    st.image('Thumbnail.jpeg', use_column_width=True)

    # Add a call-to-action button
    st.write('\n')

    st.button('Get Started')

    # Add a section header
    st.subheader('About Our Tool')

    # Add some descriptive text
    st.write('Our tool is designed to convert research articles into a variety of formats that are easy to understand and consume. This tool will allow healthcare professionals to quickly and easily access and digest the latest research and findings, as well as create informative and engaging presentations for their colleagues and patients.')

    # Add some more descriptive text
    st.write('Our AI technology is powered by OpenAI, which uses state-of-the-art natural language processing algorithms to generate accurate and concise summaries of research articles. Our tool also includes advanced search and filtering features, so you can easily find the articles that are most relevant to your needs.')

    # Add some testimonials

    # Add a footer
    st.write('© 2023 AI Research Summary Tool. All rights reserved.')


if __name__ == '__main__':
    main()
