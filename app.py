import streamlit as st

# Define a function to perform the Caesar Cipher shift
def caesar_cipher(message, shift):
  """
  Encrypts or decrypts a message using the Caesar Cipher.

  Args:
      message: The message string to be encrypted or decrypted.
      shift: The shift value (1-25) for the Caesar Cipher.

  Returns:
      The encrypted or decrypted message string.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  new_text = ''
  lowercase_message = message.lower()  # Convert to lowercase for case-insensitive handling
  for char in lowercase_message:
    if char.isalpha():
      new_index = (alphabet.index(char) + shift) % 26
      new_char = alphabet[new_index]
      new_text += new_char.upper() if char.isupper() else new_char
    else:
      new_text += char
  return new_text

# Center the title and description with CSS
st.markdown("""
<style>
  .title {
    text-align: center;
  }
</style>

<h1 class="title">The Caesar Cipher</h1>
<p class="title">Encrypt or decrypt messages with ease!</p>
""", unsafe_allow_html=True)

# User Input section with a container for centering
with st.container():
  st.expander("Enter your message and choose an action:", expanded=True)  # Set default to open
  message = st.text_area("Message:", key="message_input")
  # Validate message input (check for alphabets and spaces only)
  if not all(char.isalpha() or char.isspace() for char in message):
    st.error("Please enter a valid message (alphabets and spaces only).")
    message = ""  # Clear the input if invalid

  action = st.radio("Action:", ("Encrypt", "Decrypt"), key="action", index=0)  # Set default action to "Encrypt"
  shift = st.number_input("Shift value (1-25):", min_value=1, max_value=25, key="shift_value")

# Submit button and results section
if st.button("Submit"):
  if action == "Encrypt":
    cipher_text = caesar_cipher(message, shift)
    st.success(f"**Encrypted Text:** {cipher_text}")  # Use markdown formatting for bold text
  else:
    plain_text = caesar_cipher(message, -shift)
    st.success(f"**Decrypted Text:** {plain_text}")  # Use markdown formatting for bold text
