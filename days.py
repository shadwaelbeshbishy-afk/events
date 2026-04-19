import streamlit as st

st.title("📅 PlanFlow - Smart Scheduler")

n = st.number_input("How many events?", min_value=1, step=1)

events = []

st.write("Enter events (start must be < end)")

for i in range(int(n)):
    col1, col2 = st.columns(2)

    with col1:
        start = st.number_input(f"Start {i+1}", key=f"start{i}", step=1)

    with col2:
        end = st.number_input(f"End {i+1}", key=f"end{i}", step=1)

    # validation
    if start < end:
        events.append((start, end))

def schedule_days(arr):
    arr = sorted(arr, key=lambda x: x[0])
    days = []

    for event in arr:
        placed = False

        for day in days:
            if event[0] >= day[-1][1]:
                day.append(event)
                placed = True
                break

        if not placed:
            days.append([event])

    return days

if st.button("Generate Schedule"):
    if not events:
        st.error("No valid events entered!")
    else:
        days = schedule_days(events)

        st.success(f"Created {len(days)} day(s) 📅")

        for i, day in enumerate(days, 1):
            st.subheader(f"Day {i}")
            for start, end in day:
                st.write(f"🕒 {start} → {end}")
