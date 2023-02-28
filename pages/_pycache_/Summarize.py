import openai
import json
import os
import fitz
import streamlit as st
import time


def Summarize(pdf_file_name):
    # Retrieve Key
    OPENAI_API_KEY = ''
    with open('/Users/trongphan/Downloads/finalfantasyxv-main/OpenAI.json', 'r') as file_to_read:
        json_data = json.load(file_to_read)
        OPENAI_API_KEY = json_data["OPENAI_API_KEY"]

    openai.api_key = OPENAI_API_KEY

    # get docs file
    doc = fitz.open(
        '/Users/trongphan/Downloads/finalfantasyxv-main/pdf_folder/' + pdf_file_name + '.pdf')

    # get summarization text list
    summary_list = []
    for page in doc:
        text = page.get_text("text")
        prompt = ("Summarize " + pdf_file_name +
                  "in under 500 words" + text)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=120,
            top_p=0.9,
            frequency_penalty=0.0,
            presence_penalty=1
        )
        summary_list.append(response["choices"][0]["text"])
    # print summarization of text
    summary_text = ' '.join(summary_list)
    return summary_text


def main():
    # Set page title
    st.set_page_config(page_title='Paper Summarization',
                       page_icon=':memo:', layout='wide')

    # Display a file uploader widget
    st.sidebar.title("Drag your Paper here for Summarization :')))")
    uploaded_file = st.sidebar.file_uploader("", type="pdf")
    pdf_file_name = None
    if uploaded_file is not None:
        pdf_file_name = uploaded_file.name.replace('.pdf', '')

    # Get the summarization
    if pdf_file_name is not None:
        # Create a progress bar
        my_bar = st.progress(0)
        # Start the summarization
        summary_text = Summarize(pdf_file_name)
        # Update the progress bar
        my_bar.progress(100)

        # Display the text content
        st.title("Summarization")
        st.write(summary_text)

    # Ask Question
    st.title("Ask a question")
    s = st.text_input(
        "Type something you want to ask about this paper summarization:")
    if s:
        prompt = s + " " + summary_text
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=400,
            top_p=0.9,
            frequency_penalty=0.0,
            presence_penalty=1
        )
        st.write(response["choices"][0]["text"])


if __name__ == '__main__':
    main()
