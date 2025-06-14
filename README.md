import streamlit as st
import random
import time

# Food items and initial prices
food_items = {
    "Onion": 200,
    "Plantain": 500,
    "Banana": 300,
    "Tomatoes": 400,
    "Sugarcane": 150,
    "Yam": 1000,
    "Rice": 700,
    "Beans": 650,
    "Gari": 250,
    "Orange": 350,
    "Mango": 300,
    "Cucumber": 200,
    "Pineapple": 500
}

# Simulate price change
def simulate_prices(prices):
    new_prices = {}
    for item, price in prices.items():
        change_percent = random.uniform(-0.05, 0.05)  # -5% to +5%
        new_price = round(price * (1 + change_percent))
        new_prices[item] = max(1, new_price)  # Price can't go below 1
    return new_prices

# Main app
st.title("🥦 Food Market Simulator")
st.caption("Prices update every 1 minute")

# Session state to store prices
if "prices" not in st.session_state:
    st.session_state.prices = food_items.copy()
if "last_updated" not in st.session_state:
    st.session_state.last_updated = time.time()

# Timer check (every 60 seconds)
current_time = time.time()
if current_time - st.session_state.last_updated > 60:
    st.session_state.prices = simulate_prices(st.session_state.prices)
    st.session_state.last_updated = current_time

# Display prices
st.write("### 📊 Current Food Prices (₦)")
for item, price in st.session_state.prices.items():
    st.write(f"- **{item}**: ₦{price}")

# Optional: refresh timer display
countdown = int(60 - (current_time - st.session_state.last_updated))
st.info(f"🔄 Next update in: {countdown} seconds")
