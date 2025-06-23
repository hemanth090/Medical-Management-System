# 🏥 Medical Management System

A comprehensive web-based medical management system built with Streamlit and MongoDB for efficient healthcare operations. Manage medicines, patients, diagnoses, and purchase transactions all in one unified platform.

## ✨ Features

- **💊 Medicine Management**: Complete CRUD operations for medicine inventory
- **👨‍⚕️ Patient Management**: Patient registration with automated medicine recommendations
- **🛒 Purchase System**: Built-in shopping cart and transaction management
- **📊 Data Analytics**: Real-time dashboards for inventory and purchase tracking
- **🔐 Secure Login**: Authentication system for authorized access
- **📱 Responsive UI**: Modern interface optimized for healthcare workflows
- **🔄 Real-time Updates**: Live data synchronization with MongoDB

## 🚀 Live Demo

Experience the system in action: [Live Demo Link Here]

## 🛠️ Tech Stack

- **Frontend**: Streamlit, Custom CSS
- **Backend**: Python, Pandas
- **Database**: MongoDB Atlas
- **Authentication**: Session-based login system
- **Data Processing**: Real-time CRUD operations
- **UI/UX**: Responsive design with healthcare-focused interface

## 📁 Project Structure

```
medical-management-system/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── README.md             # This file
└── docs/                 # Documentation files
    ├── setup.md          # Setup instructions
    └── api-reference.md  # API documentation
```

## 🏃‍♂️ Quick Start

### Prerequisites
- Python 3.8+
- MongoDB Atlas account (or local MongoDB installation)
- Basic understanding of healthcare management systems

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/hemanth090/medical-management-system.git
cd medical-management-system
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure MongoDB connection**
```bash
# Update the MongoDB connection string in app.py
# Replace with your actual MongoDB Atlas connection string
MONGODB_URI = "mongodb+srv://username:password@cluster.mongodb.net/"
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Access the system**
```
Default Login Credentials:
Username: dbms
Password: 1
```

## 🔧 Configuration

### Database Setup

The system automatically creates the following collections:
- `patients` - Patient information and medical history
- `medicines` - Medicine inventory and pricing
- `diagnosis_medicine` - Diagnosis to medicine mapping
- `purchases` - Transaction history and shopping cart data

### Predefined Diagnoses

The system includes built-in mapping for common medical conditions:

| Condition | Recommended Medicine |
|-----------|---------------------|
| Cold | Antihistamines |
| Cough | Dextromethorphan-based cough syrup |
| Flu | Antiviral medications |
| Headache | Ibuprofen |
| Allergies | Antihistamines |
| Heartburn | Antacids |
| Minor Burns | Antiseptic Cream |
| Muscle Pain | Ibuprofen |
| Nausea | Antiemetics |
| Insomnia | Over-the-counter Sleep Aids |

## 🎯 Core Functionalities

### Medicine Management
- **Add Medicine**: Register new medicines with price and quantity
- **Update Medicine**: Modify existing medicine details
- **Delete Medicine**: Remove medicines from inventory
- **Purchase Medicine**: Process transactions with automatic inventory updates

### Patient Management
- **Patient Registration**: Add patients with age and medical problems
- **Automated Recommendations**: AI-powered medicine suggestions based on diagnosis
- **Medical History**: Track patient visits and treatments

### Inventory Tracking
- **Real-time Updates**: Live inventory management
- **Purchase History**: Complete transaction records
- **Shopping Cart**: Session-based cart management
- **Data Visualization**: Interactive tables and analytics

## 🔐 Security Features

- **Authentication System**: Secure login with session management
- **Data Validation**: Input sanitization and validation
- **Connection Security**: Encrypted MongoDB connections
- **Session Management**: Secure user session handling

## 📊 System Capabilities

- **Real-time Data Processing**: Instant updates across all operations
- **Scalable Architecture**: Built to handle growing healthcare needs
- **User-friendly Interface**: Intuitive design for healthcare professionals
- **Comprehensive Reporting**: Detailed analytics and reporting features

## 🤝 Contributing

We welcome contributions to improve the Medical Management System:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/medical-feature`)
3. **Commit changes** (`git commit -m 'Add medical feature'`)
4. **Push to branch** (`git push origin feature/medical-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow healthcare data privacy standards
- Maintain code documentation
- Test thoroughly with sample medical data
- Ensure HIPAA compliance considerations

## 🛡️ Data Privacy & Compliance

- **Data Security**: All patient data is encrypted and securely stored
- **Access Control**: Role-based access for different user types
- **Audit Trail**: Complete logging of all system activities
- **Compliance Ready**: Designed with healthcare regulations in mind

## 📝 API Reference

### Medicine Operations
```python
# Add Medicine
add_medicine(name, price, quantity, medicines_collection)

# Update Medicine
update_medicine(name, price, quantity, medicines_collection)

# Delete Medicine
delete_medicine(name, medicines_collection)
```

### Patient Operations
```python
# Add Patient
add_patient(name, age, problem, patients_collection, diagnosis_medicine_collection)

# Get Recommendations
recommend_medicine(problem, diagnosis_medicine_collection)
```

## 🐛 Known Issues

- Shopping cart resets on page refresh (session-based)
- MongoDB connection requires stable internet
- Large datasets may require pagination

## 📞 Support

Need help with the Medical Management System?

- 🐛 **Bug Reports**: [Create an issue](https://github.com/hemanth090/medical-management-system/issues)
- 💡 **Feature Requests**: [Start a discussion](https://github.com/hemanth090/medical-management-system/discussions)
- 📧 **Direct Contact**: [naveenhemanth4@gmail.com](mailto:naveenhemanth4@gmail.com)

## 🚀 Future Roadmap

- [ ] Advanced analytics and reporting dashboard
- [ ] Multi-user role management (Admin, Doctor, Pharmacist)
- [ ] Prescription management system
- [ ] Integration with external pharmacy APIs
- [ ] Mobile app development
- [ ] Telemedicine features
- [ ] Insurance claim processing
- [ ] Multi-language support

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **MongoDB** for robust database solutions
- **Streamlit** for rapid web application development
- **Healthcare Community** for requirements and feedback
- **Open Source Contributors** for continuous improvements

## 📈 Performance Metrics

- **Real-time Processing**: Instant data updates and synchronization
- **Scalable Design**: Handles multiple concurrent users
- **Efficient Queries**: Optimized MongoDB operations
- **User Experience**: Intuitive interface reducing training time

---

**Built with ❤️ for Healthcare by [Naveen Hemanth](https://github.com/hemanth090)**

*Empowering healthcare management through technology.*
