import streamlit as st
from databricks.sdk import WorkspaceClient

st.set_page_config(page_title="My Databricks App", page_icon="🏠", layout="wide")

w = WorkspaceClient()
current_user = w.current_user.me()

st.title("🚀 Welcome to your Databricks App!")
st.markdown(f"Hello, **{current_user.display_name}**!")

st.divider()

st.subheader("Getting Started")
st.markdown(
    """
    This is a starter Streamlit app running on Databricks Apps.
    Edit `app.py` to build your application.

    **Useful resources:**
    - [Databricks Apps docs](https://docs.databricks.com/dev-tools/databricks-apps/)
    - [Streamlit API reference](https://docs.streamlit.io/library/api-reference)
    - [Databricks SDK for Python](https://docs.databricks.com/dev-tools/sdk-python.html)
    """
)

st.subheader("Example: List Catalogs")
if st.button("List Unity Catalog catalogs"):
    with st.spinner("Fetching catalogs..."):
        catalogs = list(w.catalogs.list())
        if catalogs:
            st.dataframe(
                [{"name": c.name, "comment": c.comment or ""} for c in catalogs],
                use_container_width=True,
            )
        else:
            st.info("No catalogs found.")
