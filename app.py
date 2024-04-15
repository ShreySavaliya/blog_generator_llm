import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers


## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,no_words,blog_style):
    llm=CTransformers(model='D:\Project\LLM\llama2\llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template

    template="""
         Write a blog about {input_text} as I am a {blog_style} within approximately {no_words} number of words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('Enter the number of words you want for your article: ')
with col2:
    blog_style=st.selectbox("Who you are?", ("Researcher", "Data Scientist", "Student", "Doctor", "Musician", "Teacher"), index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,no_words,blog_style))