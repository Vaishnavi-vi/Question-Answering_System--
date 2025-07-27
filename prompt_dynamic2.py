from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
import streamlit as st
from PIL import Image

load_dotenv()
llm1=HuggingFaceEndpoint(repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1",task="text-generation",model_kwargs={"api_key":os.getenv("HUGGINGFACEHUB_API_TOKEN")})
model=ChatHuggingFace(llm=llm1)
st.set_page_config(page_title="Text generation",layout="centered")
page=st.sidebar.radio("Select one anomg the following:",["Go To:","Science","English","Math","Social Science"])
if page=="Go To:":
    st.title("Question-Answering System")
    image=Image.open("C:\\Users\\Dell\\Downloads\\QA.png") 
    st.image(image,use_container_width=True)
elif page=="Science":
    st.header("Science Question-Answering System")
    explanation_layout=st.selectbox("Select Explanation level:",["select","Beginner","Intermediate","Advanced"])
    length_=st.selectbox("Select Explanation length",["Select","long","short","medium"])
    user_input=st.text_input("Please Enter you question:")
    template=PromptTemplate(template="""Give the answer of the question "{user_input}" with certain specification as:
                            Explanation Style:"{explanation_layout}"
                            Explanation length:"{length_}"
                            1.Mathematical Details
                            -Include relevant mathematical equations if present in the paper.
                            2.Analogies:
                           -Use relatable analogies to simplify complex ideas.""",
    input_variables=["user_input","explanation_layout","length_"])
    prompt=template.invoke({"user_input":user_input,"explanation_layout":explanation_layout,"length_":length_})
    
    if st.button("Generate"):
        if user_input=="":
            st.warning("Please add Valid Questions")
        else:
            with st.spinner("Thinking"):
                result=model.invoke(prompt)
                st.success("Response:")
                st.write(result.content)
                
elif page=="English":
    st.header("English Quesion-Answering System") 
    explanation_layout=st.selectbox("Select Explanation level:",["select","Beginner","Intermediate","Advanced"])
    length_=st.selectbox("Select Explanation length",["Select","long","short","medium"])
    user_input=st.text_input("Please Enter you question:")
    template=PromptTemplate(template=""" Give answer of the following question "{user_input}" with certain explanation as:
                            Explanation layout:"{explanation_layout}
                            Explanation length:"{length_}"
                            Use relevant ideas to simplify complex attributes""",input_variables=["user_input","explanation_layout","length_"])
    
    prompt=template.invoke({"user_input":user_input,"explanation_layout":explanation_layout,"length_":length_})
    
    if st.button("Generate"):
        if user_input=="":
            st.warning("Please add valid Questions")
        else:
            with st.spinner("Thinking..."):
                result=model.invoke(prompt)
                st.success("Response")
                st.write(result.content)
                
elif page=="Math":
    st.header("Math Quesion-Answering System") 
    explanation_layout=st.selectbox("Select Explanation level:",["select","Beginner","Intermediate","Advanced"])
    length_=st.selectbox("Select Explanation length",["Select","long","short","medium"])
    user_input=st.text_input("Please Enter you question:")
    template=PromptTemplate(template=""" Give answer of the following question "{user_input}" with certain explanation as:
                            Explanation layout:"{explanation_layout}
                            Explanation length:"{length_}"
                            1.Mathmatical Explanation:
                            -Include mathematical explanation with example.
                            2.Conceptual Explanation:
                            -Include relevant ideas to show theoretical knowledge.""",input_variables=["user_input","explanation_layout","length_"])
    
    prompt=template.invoke({"user_input":user_input,"explanation_layout":explanation_layout,"length_":length_})
    
    if st.button("Generate"):
        if user_input=="":
            st.warning("Please add valid Questions")
        else:
            with st.spinner("Thinking..."):
                result=model.invoke(prompt)
                st.success("Response")
                st.write(result.content)
                

elif page=="Social Science":
    st.header("Social Science Quesion-Answering System") 
    explanation_layout=st.selectbox("Select Explanation level:",["select","Beginner","Intermediate","Advanced"])
    length_=st.selectbox("Select Explanation length",["Select","long","short","medium"])
    user_input=st.text_input("Please Enter you question:")
    template=PromptTemplate(template=""" Give answer of the following question "{user_input}" with certain explanation as:
                            Explanation layout:"{explanation_layout}
                            Explanation length:"{length_}"
                            Include relevant ideas to show theoretical knowledge and Use relatable analogies to simplify complex ideas.""",input_variables=["user_input","explanation_layout","length_"])
    
    prompt=template.invoke({"user_input":user_input,"explanation_layout":explanation_layout,"length_":length_})
    
    if st.button("Generate"):
        if user_input=="":
            st.warning("Please add valid Questions")
        else:
            with st.spinner("Thinking..."):
                result=model.invoke(prompt)
                st.success("Response")
                st.write(result.content) 
            

