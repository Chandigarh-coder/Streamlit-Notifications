import streamlit.components.v1 as components

def send_push(title, body, icon):
    components.declare_component(
        "push_notification",
        path="frontend/build",
    )
    components.push_notification(
        title=title,
        body=body,
        icon=icon,
    )
