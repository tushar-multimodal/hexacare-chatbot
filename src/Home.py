import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Hexacare | AI Chat-Bot 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

 
    st.write("**Mail** : tush.r1711@mail.com")
    st.write("**Created by Tushar Upadhyay**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Hexacare, Ask me Anything about Hexaware 🤖</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm Hexacare, an AI chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive interactions. I know everything about Hexaware.
    </h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Hexaware's Pages
st.subheader("🚀 Hexaware'ss Pages")
st.write("""
- **Hexaware-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **Hexaware-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
- **Hexaware-Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
""")
st.markdown("---")


#Contributing
#st.markdown("### 🎯 Contributing")
###st.markdown("""
#**Robby is under regular development. Feel free to contribute and help me make it even more data-aware!**
#""", unsafe_allow_html=True)





