import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Function to connect to MongoDB
def connect_to_mongodb():
    with st.spinner('Connecting to MongoDB...'):
        try:
            # MongoDB connection string (replace with your actual connection details)
            client = MongoClient('mongodb+srv://med:1234@cluster0.xa1kvtz.mongodb.net/')
            db = client['medical_data']

            # Initialize collections
            patients_collection = db['patients']
            diagnosis_medicine_collection = db['diagnosis_medicine']
            medicines_collection = db['medicines']
            purchases_collection = db['purchases']

            return client, patients_collection, diagnosis_medicine_collection, medicines_collection, purchases_collection, db

        except Exception as e:
            st.exception(e)
            return None, None, None, None, None, None

# CRUD Operations for Medicines
def add_medicine(name, price, quantity, medicines_collection):
    medicine_data = {'name': name, 'price': price, 'quantity': quantity}
    medicines_collection.insert_one(medicine_data)
    st.sidebar.success('Medicine added successfully!')

def update_medicine(name, price, quantity, medicines_collection):
    query = {'name': name}
    new_values = {'$set': {'price': price, 'quantity': quantity}}
    medicines_collection.update_one(query, new_values)
    st.sidebar.success('Medicine updated successfully!')

def delete_medicine(name, medicines_collection):
    query = {'name': name}
    medicines_collection.delete_one(query)
    st.sidebar.success('Medicine deleted successfully!')

def get_medicine_data(medicines_collection):
    medicines_data = list(medicines_collection.find())
    return pd.DataFrame(medicines_data)

# Shopping Operations
def buy_medicine(medicine_name, quantity, medicines_collection, purchases_collection, cart):
    medicine = medicines_collection.find_one({'name': medicine_name})

    if medicine and medicine['quantity'] >= quantity:
        purchase_data = {
            'medicine_name': medicine_name,
            'price': medicine['price'],
            'quantity': quantity,
            'total_price': medicine['price'] * quantity,
            'timestamp': pd.to_datetime('now'),
        }
        purchases_collection.insert_one(purchase_data)

        # Update medicine quantity after purchase
        new_quantity = medicine['quantity'] - quantity
        update_medicine(medicine_name, medicine['price'], new_quantity, medicines_collection)

        # Add to cart
        cart.append(purchase_data)

        st.success(f'Purchase successful! Total amount: ${purchase_data["total_price"]}')
    else:
        st.warning('Medicine not available in sufficient quantity.')

# Patient Operations
def add_patient(name, age, problem, patients_collection, diagnosis_medicine_collection):
    patient_data = {'name': name, 'age': age, 'problem': problem}
    patients_collection.insert_one(patient_data)

    # Recommend medicine based on the patient's problem
    recommended_medicine = recommend_medicine(problem, diagnosis_medicine_collection)

    if recommended_medicine:
        st.sidebar.success(f'Patient added successfully! Recommended Medicine: {recommended_medicine}')
        st.sidebar.text(f'To Buy the recommended medicine, go to the "Buy Medicine" operation.')
    else:
        st.sidebar.warning('Patient added successfully! No specific recommendation available for this problem.')

def get_patient_data(patients_collection):
    patients_data = list(patients_collection.find())
    return pd.DataFrame(patients_data)

# Replace the existing diagnosis-to-medicine mapping with the provided data
def replace_diagnosis_mapping(diagnosis_medicine_collection):
    diagnosis_medicine_collection.delete_many({})

    # Insert new data
    diagnosis_medicine_collection.insert_many([
        {"problem": "Cold", "medicine": "Antihistamines"},
        {"problem": "Cough", "medicine": "Dextromethorphan-based cough syrup"},
        {"problem": "Flu", "medicine": "Antiviral medications"},
        {"problem": "Headache", "medicine": "Ibuprofen"},
        {"problem": "Allergies", "medicine": "Antihistamines"},
        {"problem": "Heartburn", "medicine": "Antacids"},
        {"problem": "Minor Burns", "medicine": "Antiseptic Cream"},
        {"problem": "Muscle Pain", "medicine": "Ibuprofen"},
        {"problem": "Nausea", "medicine": "Antiemetics"},
        {"problem": "Insomnia", "medicine": "Over-the-counter Sleep Aids"},
    ])

# Function to recommend medicine based on the patient's problem
def recommend_medicine(problem, diagnosis_medicine_collection):
    diagnosis_data = diagnosis_medicine_collection.find_one({'problem': problem})
    print(f"Diagnosis Data for {problem}: {diagnosis_data}")  # Add this line for debugging
    if diagnosis_data:
        return diagnosis_data['medicine']
    else:
        return "No specific recommendation available for this problem."

# Main Page Content
def main_page(client, medicines_collection, purchases_collection, patients_collection, diagnosis_medicine_collection, cart):
    st.title('Medical Management System')

    # Connection Page
    connection_status = st.empty()

    if client is not None and medicines_collection is not None and purchases_collection is not None \
            and patients_collection is not None and diagnosis_medicine_collection is not None:
        connection_status.write("Connected to MongoDB!")

        # Replace the existing diagnosis-to-medicine mapping with the provided data
        replace_diagnosis_mapping(diagnosis_medicine_collection)

        # Sidebar for CRUD operations
        st.sidebar.header('Medicine Operations')
        medicine_operation = st.sidebar.selectbox('Select Operation', ['Add', 'Update', 'Delete', 'Buy'])

        if medicine_operation == 'Add':
            st.sidebar.header('Add Medicine')
            medicine_name = st.sidebar.text_input('Medicine Name')
            medicine_price = st.sidebar.number_input('Medicine Price', min_value=0.0, value=0.0)
            medicine_quantity = st.sidebar.number_input('Medicine Quantity', min_value=0, value=0)

            if st.sidebar.button('Add Medicine'):
                add_medicine(medicine_name, medicine_price, medicine_quantity, medicines_collection)

        elif medicine_operation == 'Update':
            st.sidebar.header('Update Medicine')
            medicine_name = st.sidebar.text_input('Enter Medicine Name to Update')
            medicine_price = st.sidebar.number_input('Updated Medicine Price', min_value=0.0, value=0.0)
            medicine_quantity = st.sidebar.number_input('Updated Medicine Quantity', min_value=0, value=0)

            if st.sidebar.button('Update Medicine'):
                update_medicine(medicine_name, medicine_price, medicine_quantity, medicines_collection)

        elif medicine_operation == 'Delete':
            st.sidebar.header('Delete Medicine')
            medicine_name = st.sidebar.text_input('Enter Medicine Name to Delete')

            if st.sidebar.button('Delete Medicine'):
                delete_medicine(medicine_name, medicines_collection)

        elif medicine_operation == 'Buy':
            st.sidebar.header('Buy Medicine')
            medicine_name = st.sidebar.text_input('Enter Medicine Name to Buy')
            quantity_to_buy = st.sidebar.number_input('Enter Quantity to Buy', min_value=1, value=1)

            if st.sidebar.button('Buy Medicine'):
                buy_medicine(medicine_name, quantity_to_buy, medicines_collection, purchases_collection, cart)

        # Patient Operations
        st.sidebar.header('Patient Operations')
        patient_operation = st.sidebar.selectbox('Select Operation', ['Add'])

        if patient_operation == 'Add':
            st.sidebar.header('Add Patient')
            patient_name = st.sidebar.text_input('Patient Name')
            patient_age = st.sidebar.number_input('Patient Age', min_value=0, max_value=150, value=0)
            patient_problem = st.sidebar.selectbox('Patient Problem', ['Cold', 'Cough', 'Flu', 'Headache', 'Allergies', 'Heartburn', 'Minor Burns', 'Muscle Pain', 'Nausea', 'Insomnia'])

            if st.sidebar.button('Add Patient'):
                add_patient(patient_name, patient_age, patient_problem, patients_collection, diagnosis_medicine_collection)

        # Display medicine data
        st.header('Medicine Data')
        medicine_data = get_medicine_data(medicines_collection)
        st.dataframe(medicine_data)

        # Display purchase history
        st.header('Purchase History')
        purchase_history = pd.DataFrame(list(purchases_collection.find()))
        st.dataframe(purchase_history)

        # Display shopping cart
        st.header('Shopping Cart')
        if cart:
            cart_df = pd.DataFrame(cart)
            st.dataframe(cart_df)
        else:
            st.info('Shopping cart is empty.')

        # Display patient data
        st.header('Patient Data')
        patient_data = get_patient_data(patients_collection)
        st.dataframe(patient_data)

        # Logout button
        if st.button('Logout'):
            st.session_state.is_logged_in = False
            st.experimental_rerun()

        # Close MongoDB connection
        client.close()

    else:
        connection_status.write("Failed to connect to MongoDB. Please check your connection details.")

# Login Page
def login_page():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        # Replace with your authentication logic
        if username == '1' and password == '1':
            st.session_state.is_logged_in = True
            st.success('Login successful!')
            st.experimental_rerun()
        else:
            st.warning('Login failed. Please check your credentials.')

# Streamlit UI
def main():
    # Check if the user is logged in
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    if not st.session_state.is_logged_in:
        login_page()
    else:
        # Attempt to connect to MongoDB
        client, medicines_collection, purchases_collection, patients_collection, diagnosis_medicine_collection, db = connect_to_mongodb()
        cart = []
        main_page(client, medicines_collection, purchases_collection, patients_collection, diagnosis_medicine_collection, cart)

if __name__ == '__main__':
    main()
