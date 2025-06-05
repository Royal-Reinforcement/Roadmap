import streamlit as st
import pandas as pd
import smartsheet


def smartsheet_to_dataframe(sheet_id):
    smartsheet_client = smartsheet.Smartsheet(st.secrets['smartsheet']['access_token'])
    sheet             = smartsheet_client.Sheets.get_sheet(sheet_id)
    columns           = [col.title for col in sheet.columns]
    rows              = []
    for row in sheet.rows: rows.append([cell.value for cell in row.cells])
    return pd.DataFrame(rows, columns=columns)


st.set_page_config(page_title="Roadmap", page_icon="🗺️", layout="centered")

st.image(st.secrets['images']['logo'], width=100)

st.title('Project Roadmap')
st.info(f"Want to work on something together? [Send me a message!]({st.secrets['contacts']['email']})", icon='👋')
st.success('Below is a record of projects that are in the works and coming soon!')


df = smartsheet_to_dataframe(st.secrets['smartsheet']['sheet_id']['projects'])
df = df.sort_values(by='Started_Using', ascending=False)


with st.expander('See past projects'):
    for index, item in df[df.Status == 'Done'].iterrows():
        st.markdown(f"{item.Emoji} **{item.Project}** :green-badge[Delivered {item.Started_Using}]")
        st.caption(item.Description)

st.header('Coming soon')

for index, item in df[df.Status == 'Working'].iterrows():
        st.markdown(f"{item.Emoji} **{item.Project}** :violet-badge[Working]")
        st.caption(item.Description)

for index, item in df[df.Status == 'Planning'].iterrows():
        st.markdown(f"{item.Emoji} **{item.Project}** :blue-badge[Planning]")
        st.caption(item.Description)

for index, item in df[df.Status == 'Future'].iterrows():
        st.markdown(f"{item.Emoji} **{item.Project}**")
        st.caption(item.Description)