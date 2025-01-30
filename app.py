import streamlit as st
from streamlit_push_notifications import send_push
import time

st.title("Streamlit Timer with Notification")

# Set the duration for the timer (in seconds)
timer_duration = 10  # 10 seconds for demonstration

# Display the countdown timer
countdown_placeholder = st.empty()
for remaining_time in range(timer_duration, 0, -1):
    minutes, seconds = divmod(remaining_time, 60)
    countdown_placeholder.metric("Time Remaining", f"{minutes:02}:{seconds:02}")
    time.sleep(1)

# Send a notification after the timer completes
send_push(
    title="Timer Complete",
    body="The specified duration has elapsed."
)

# Inform the user that the timer has completed
st.success("The timer has completed. A notification has been sent.")
