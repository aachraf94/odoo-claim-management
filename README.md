# Claims Management Module for AlMiyah Djazair

An Odoo module designed to streamline customer claims and complaints management for AlMiyah Djazair, a water utility company.

## 📌 Overview
This module provides an efficient system for tracking, processing, and resolving both technical and commercial claims across AlMiyah Djazair’s agencies.

## 🚀 Key Features

### 📝 Claims Management
- Record claims from multiple sources (citizens, businesses, monitoring units).
- Track claim status throughout its lifecycle.
- Attach supporting documents.
- Generate automated claim references.
- Manage priority and urgency levels.

### 👤 Claimant Management
- Maintain detailed claimant profiles.
- Support both individual and business claimants.
- Track claim history per claimant.

### 🏢 Agency Operations
- Enable agency-specific claim handling.
- Manage employee roles and responsibilities.
- Assign teams for claim resolution.

### 📞 Communication Tracking
- Record all customer interactions.
- Track phone calls and status updates.
- Maintain a complete communication history.

### 📂 Project Integration
- Create projects for complex claims.
- Assign teams and monitor progress.
- Link tasks to claim resolution.

---
## ⚙️ Installation

1. Clone this repository into your Odoo addons directory:
   ```bash
   git clone https://github.com/your-repo/claim_management.git /path/to/odoo/addons
   ```
2. Update Odoo’s module list and install the module:
   - Navigate to **Apps** in Odoo.
   - Remove the "Apps" filter.
   - Search for "Claim Management".
   - Click **Install**.

---
## 📦 Dependencies
This module requires the following Odoo modules:
- `base`
- `mail`
- `web`
- `hr`
- `project`

---
## 🔧 Configuration

### 1️⃣ Agency Setup
- Create agencies and assign managers.
- Configure agency details and contact information.

### 2️⃣ Employee Roles
- Assign employees to agencies.
- Define roles (customer service, technician, etc.).

### 3️⃣ Claim Types
- **Technical Claims:** Water quality, leaks, infrastructure issues.
- **Commercial Claims:** Billing errors, consumption disputes.

---
## 📌 Usage Guide

### 🆕 Creating a New Claim
1. Go to **Claims Management > Claims > All Claims**.
2. Click **Create**.
3. Fill in required details:
   - Claimant information.
   - Claim subject and description.
   - Assign agency.
   - Set priority and claim type.
4. Click **Submit**.

### 🔄 Processing Claims
#### Commercial Claims:
- Assign a commercial team.
- Document resolutions in PV.
- Finalize dispute resolution.

#### Technical Claims:
- Assign a technical team.
- Record intervention details.
- Document resolution steps.

### 📢 Customer Communication
- Record interactions.
- Track communication history.
- Update claim status.
- Collect customer feedback.

---
## 🔐 Security & Access Control
The module enforces **role-based access control** with the following permission levels:
- **Agency Managers**: Full access.
- **Customer Service Agents**: Manage customer interactions.
- **Technical Teams**: Handle technical claims.
- **Commercial Teams**: Resolve commercial disputes.

---
## 👥 Authors & Contributors
Developed by **2CS SIT2 TEAM 02 - ESI 2025**.

### Team Members:
- **Abdelkebir Achraf** - [GitHub](https://github.com/aachraf94)
- **Boussebata Issam** - [GitHub](https://github.com/ISSAM2411)
- **Zaidi Yasmine** - [GitHub](https://github.com/yasmiinie)
- **Makhloufi Aymen** - [GitHub](https://github.com/AymenMakhloufi)

---
## 📜 License
This module is licensed under **LGPL-3**.

---
## 📧 Support & Contact
For inquiries and support:
- 🌐 [AlMiyah Djazair Website](https://almiyah-djazair.dz)
- 📩 [Support Email](mailto:support@almiyah-djazair.dz)

---
## 🤝 Contributing
Contributions are welcome! Please follow our contribution guidelines before submitting a pull request.

---

