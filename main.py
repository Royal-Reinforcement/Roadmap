import streamlit as st

st.image(st.secrets['images']['logo'], width=100)

st.title('Project Roadmap')
st.info(f"Want to work on something together? [Send me a message!]({st.secrets['contacts']['email']})", icon='👋')
st.success('Below is a record of projects that are in the works and coming soon!')

with st.expander('See past projects'):
    for item in st.secrets['archive']:
        st.markdown(f"{item[1]} **{item[0]}** :green-badge[Delivered]")
        st.caption(item[2])

st.header('Coming soon')

for item in st.secrets['working']:
        st.markdown(f"{item[1]} **{item[0]}** :violet-badge[Working]")
        st.caption(item[2])

for item in st.secrets['planning']:
        st.markdown(f"{item[1]} **{item[0]}** :blue-badge[Planning]")
        st.caption(item[2])

for item in st.secrets['future']:
        st.markdown(f"{item[1]} **{item[0]}**")
        st.caption(item[2])