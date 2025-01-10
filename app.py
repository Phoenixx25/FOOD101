import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
model = load_model('food_classifier_model.h5')

# Label dictionary
label_dict = {
    0: 'burger',
    1: 'butter_naan',
    2: 'chai',
    3: 'chapati',
    4: 'chole_bhature',
    5: 'dal_makhani',
    6: 'dhokla',
    7: 'fried_rice',
    8: 'idli',
    9: 'jalebi',
    10: 'kathi_roll',
    11: 'kadhai_paneer',
    12: 'kulfi',
    13: 'masala_dosa',
    14: 'momos',
    15: 'paani_puri',
    16: 'pakode',
    17: 'pav_bhaji',
    18: 'pizza',
    19: 'samosa'
}

def predict_image(image_path):
    image = load_img(image_path, target_size=(128, 128))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Normalize to [0, 1]
    probabilities = model.predict(image)[0]
    predicted_label_index = np.argmax(probabilities)
    predicted_label = label_dict[predicted_label_index]
    return predicted_label, probabilities

st.title('Food Classifier')
st.write("Upload an image of food to get the classification.")

uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with open("uploaded_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    predicted_label, probabilities = predict_image("uploaded_image.jpg")
    st.write(f"Predicted Label: **{predicted_label}**")

    # Display probabilities
    st.write("Probabilities:")
    for i, prob in enumerate(probabilities):
        st.write(f"{label_dict[i]}: {prob:.4f}")
