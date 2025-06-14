import streamlit as st
import time
import random

st.set_page_config(page_title="Food Market App", layout="centered")

# Base prices for each item (in Naira)
base_prices = {
    "Onion": 100,
    "Plantain": 150,
    "Banana": 120,
    "Tomatoes": 200,
    "Sugarcane": 80,
    "Yam": 250,
    "Rice": 300,
    "Beans": 280,
    "Gari": 160,
    "Orange": 100,
    "Mango": 120,
    "Cucumber": 90,
    "Pineapple": 180,
}

# Simulated prices with fluctuation
def simulate_price(last_price):
    change_percent = random.uniform(-0.03, 0.03)  # -3% to +3%
    new_price = round(last_price * (1 + change_percent), 2)
    return max(new_price, 1)  # Never drop below ₦1

# Initialize session state
if "prices" not in st.session_state:
    st.session_state.prices = {item: price for item, price in base_prices.items()}
    st.session_state.last_update = time.time()

# Auto-update every 1 minute
current_time = time.time()
if current_time - st.session_state.last_update >= 60:
    for item in st.session_state.prices:
        st.session_state.prices[item] = simulate_price(st.session_state.prices[item])
    st.session_state.last_update = current_time

# UI
st.title("🛒 Virtual Food Market")
st.write("Prices update every 1 minute based on simulated market logic.")

st.markdown("### 🥑 Current Market Prices (₦)")

for item, price in st.session_state.prices.items():
    st.metric(label=item, value=f"₦{price}")

st.info("Refresh the page manually every 1 minute to see updated prices.")
