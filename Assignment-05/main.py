import streamlit as st
import hashlib
import json
import os
import time
import base64
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

# File paths
KEY_FILE = "secret.key"
DATA_FILE = "encrypted_data.json"
LOCKOUT_FILE = "lockout_info.json"

# Generate/load a key for encryption
def get_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
        return key

# Initialize key and cipher
KEY = get_or_create_key()
cipher = Fernet(KEY)

# Load stored data from file or initialize empty dictionary
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Load or initialize stored data
stored_data = load_data()

# Initialize session state for failed attempts and lockout
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0
if 'lockout_until' not in st.session_state:
    st.session_state.lockout_until = None

# Function to hash passkey with PBKDF2
def hash_passkey(passkey):
    # For new passkeys, generate a salt
    salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    key = base64.urlsafe_b64encode(kdf.derive(passkey.encode()))
    return {
        "key": key.decode(),
        "salt": base64.urlsafe_b64encode(salt).decode()
    }

# Function to verify passkey
def verify_passkey(passkey, stored_hash_data):
    try:
        salt = base64.urlsafe_b64decode(stored_hash_data["salt"])
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        derived_key = base64.urlsafe_b64encode(kdf.derive(passkey.encode())).decode()
        return derived_key == stored_hash_data["key"]
    except Exception:
        return False

# Function to encrypt data
def encrypt_data(text, passkey):
    return cipher.encrypt(text.encode()).decode()

# Function to decrypt data
def decrypt_data(encrypted_text, passkey):
    # Check if user is in lockout period
    if st.session_state.lockout_until and st.session_state.lockout_until > datetime.now():
        time_remaining = (st.session_state.lockout_until - datetime.now()).seconds
        st.error(f"🔒 Account is locked. Try again in {time_remaining} seconds.")
        return None
    
    # Reset lockout if it has expired
    if st.session_state.lockout_until and st.session_state.lockout_until <= datetime.now():
        st.session_state.lockout_until = None
        st.session_state.failed_attempts = 0

    for key, value in stored_data.items():
        if value["encrypted_text"] == encrypted_text:
            # Check if the passkey matches
            if verify_passkey(passkey, value["passkey"]):
                st.session_state.failed_attempts = 0
                return cipher.decrypt(encrypted_text.encode()).decode()
    
    # Passkey incorrect, increment failed attempts
    st.session_state.failed_attempts += 1
    
    # Apply time-based lockout after 3 failed attempts
    if st.session_state.failed_attempts >= 3:
        lockout_minutes = min(5, st.session_state.failed_attempts - 2)  # Incremental lockout
        st.session_state.lockout_until = datetime.now() + timedelta(minutes=lockout_minutes)
        
        # Save lockout info to file for persistence across sessions
        lockout_info = {
            "lockout_until": st.session_state.lockout_until.isoformat() if st.session_state.lockout_until else None,
            "failed_attempts": st.session_state.failed_attempts
        }
        with open(LOCKOUT_FILE, "w") as f:
            json.dump(lockout_info, f)
            
        st.error(f"🔒 Too many failed attempts! Account locked for {lockout_minutes} minutes.")
    
    return None

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using unique passkeys.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data, passkey)
            stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            save_data(stored_data)  # Save to file
            st.success("✅ Data stored securely!")
            # Display the encrypted text for the user to copy
            st.code(encrypted_text, language="text")
            st.info("👆 Copy this encrypted text to retrieve your data later")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted_text = decrypt_data(encrypted_text, passkey)

            if decrypted_text:
                st.success(f"✅ Decrypted Data: {decrypted_text}")
            else:
                st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - st.session_state.failed_attempts}")

                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Hardcoded for demo, replace with proper auth
            global failed_attempts
            failed_attempts = 0
            st.success("✅ Reauthorized successfully! Redirecting to Retrieve Data...")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")