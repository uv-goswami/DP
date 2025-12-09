1. Write a program to perform encryption and decryption using Caesar cipher
 (substitutional cipher).
 2. Write a program to perform encryption and decryption using Rail Fence Cipher
 (transpositional cipher)
 3. Write a Python program that defines a function and takes a password string as input and
 returns its SHA-256 hashed representation as a hexadecimal string.
 4. Write a Python program that reads a file containing a list of usernames and passwords,
 one pair per line (separated by a comma). It checks each password to see if it has been
 leaked in a data breach. You can use the "Have I Been Pwned" API
 (https://haveibeenpwned.com/API/v3) to check if a password has been leaked.
 5. Write a Python program that generates a password using a random combination of
 words from a dictionary file.
 6. Write a Python program that simulates a brute-force attack on a password by trying out
 all possible character combinations.
 7. Demonstrate the usage/sending of a digitally signed document.
 8. Students needs to conduct a data privacy audit of an organization to identify potential
 vulnerabilities and risks in their data privacy practices.
 9. Students needs to explore the requirements of the Data Protection Regulations and
 develop a plan for ensuring compliance with the regulation.
 10. Students needs to explore ethical considerations in data privacy, such as the balance
 between privacy and security, the impact of data collection and analysis on
 marginalized communities, and the role of data ethics in technology development
---


# Data-Privacy

---
# Unit : 1
## **1. Notion of Data Privacy**
- **Definition:**  
  Protection of personal/sensitive information from unauthorized access, use, disclosure, alteration, or destruction.
- **Core Idea:**  
  Individuals should have **control** over how their data is collected, processed, stored, and shared.
- **Key Principles** (from Stallings [2] & GDPR concepts):  
  - **Lawfulness, fairness, transparency** – processing must be legal and clear to the data subject.  
  - **Purpose limitation** – use data only for the stated purpose.  
  - **Data minimization** – collect only what is necessary.  
  - **Accuracy** – keep data correct and up to date.  
  - **Storage limitation** – retain only as long as needed.  
  - **Integrity & confidentiality** – protect against breaches.  
  - **Accountability** – organizations must prove compliance.

---

## **2. Historical Context of Data Privacy**
- **Pre‑Digital Era:**  
  Privacy was about physical spaces, correspondence, and personal records.
- **1970s:**  
  First data protection laws (e.g., Hesse Data Protection Act, Germany, 1970).  
  OECD Guidelines (1980) – foundational for global privacy principles.
- **1990s:**  
  Internet growth → large‑scale personal data collection.  
  EU Data Protection Directive 95/46/EC.
- **2010s:**  
  Social media, big data, AI → stricter laws (GDPR 2018, CCPA 2020).  
  Rise of **Privacy by Design** (Cavoukian, 2010) – embed privacy into systems from the start.
- **India:**  
  - *Justice K.S. Puttaswamy v. Union of India* (2017) – Right to Privacy recognized as a fundamental right.  
  - Personal Data Protection Bill drafts → **Digital Personal Data Protection Act 2023**.

---

## **3. Types of Sensitive Data** (from Venkataramanan [3] & Jarmul [4])
- **Personally Identifiable Information (PII):** Name, address, phone, email, ID numbers.
- **Financial Data:** Bank accounts, credit/debit card details, transaction history.
- **Health Data:** Medical records, prescriptions, genetic data.
- **Biometric Data:** Fingerprints, facial recognition, iris scans, voice patterns.
- **Location Data:** GPS coordinates, travel history.
- **Online Identifiers:** IP address, cookies, device IDs.
- **Special Category Data** (GDPR): Race, religion, political opinions, sexual orientation.

---

## **4. Privacy Laws and Regulations**
### **Global Examples**
| Law / Regulation | Region | Key Features |
|------------------|--------|--------------|
| **GDPR** (2018) | EU | Strong consent rules, right to access, right to erasure, heavy fines. |
| **CCPA** (2020) | California, USA | Right to know, delete, opt‑out of data sale. |
| **HIPAA** | USA | Protects health data privacy/security. |
| **LGPD** | Brazil | GDPR‑like, covers personal data processing. |

### **India – Digital Personal Data Protection Act 2023** ([5])
- **Scope:** Applies to digital personal data in India and abroad if related to Indian individuals.
- **Key Terms:**  
  - *Data Principal* – individual whose data is processed.  
  - *Data Fiduciary* – entity deciding purpose/means of processing.  
  - *Consent Manager* – platform for managing user consent.
- **Rights of Data Principals:**  
  - Right to access information about processing.  
  - Right to correction and erasure.  
  - Right to grievance redressal.
- **Obligations of Data Fiduciaries:**  
  - Obtain valid consent.  
  - Implement security safeguards.  
  - Report breaches to the Data Protection Board.
- **Penalties:**  
  - Up to ₹250 crore for serious breaches.
---
# Unit: 2 - **DATA PRIVACY ATTACKS, CRYPTOGRAPHY & DATA PROTECTION**  
---

## **1. Types of Attacks / Data Breaches on Data Privacy**

### **A. Based on Intent & Actor**
- **Malicious External Attacks** – hacking, phishing, ransomware.
- **Insider Threats** – misuse of access, accidental leaks.
- **State‑sponsored Attacks** – cyber‑espionage, political interference.

### **B. Based on Method**
- **Data Interception** – sniffing, man‑in‑the‑middle (MITM).  
- **Data Exfiltration** – unauthorized copying/moving of data.  
- **SQL Injection** – exploiting database queries.  
- **Credential Stuffing** – using stolen credentials.  
- **Social Engineering** – manipulating people to reveal info.

---

## **2. Latest Real‑World Examples (2023–2024)**

| **Attack Type** | **Recent Example** | **Where to Use Countermeasures** | **Where Not to Use / Limitations** |
|-----------------|--------------------|-----------------------------------|-------------------------------------|
| **Ransomware** | MOVEit Transfer breach (2023) | Offline backups, patching, segmentation | Paying ransom (no guarantee) |
| **Phishing + MFA Bypass** | Microsoft 365 phishing campaign (2024) | Phishing‑resistant MFA (FIDO2), training | SMS‑only MFA (SIM swap risk) |
| **Cloud Misconfiguration** | Toyota data leak (2023) | Cloud security posture tools | Public cloud buckets for sensitive data |
| **Insider Threat** | Twitter source code leak (2023) | Role‑based access, monitoring | Over‑privileged accounts without logging |

---

## **3. Impact of Data Breaches / Attacks**
- **Individuals:** Identity theft, fraud, harassment.  
- **Organizations:** Financial loss, fines, loss of trust, downtime.  
- **Society:** Erosion of digital trust, national security risks.

---

## **4. Introduction to Cryptography**
- **Definition:** Securing information by transforming it into unreadable form, reversible only with a key.
- **Goals (CIA + A):** Confidentiality, Integrity, Authentication, Non‑repudiation.
- **Real‑World Context:** Banking apps, e‑commerce, secure messaging (Signal, WhatsApp).
- **Limitation:** Encryption doesn’t protect data on compromised endpoints.

---

## **5. Symmetric Encryption**
- **Concept:** Same key for encryption & decryption.
- **Advantages:** Fast, efficient for large data.
- **Disadvantages:** Key distribution problem.
- **Examples:** AES, ChaCha20.
- **Where to Use:**  
  - WhatsApp message payloads (AES‑256)  
  - Zoom AES‑GCM meeting encryption  
  - Disk encryption (BitLocker, FileVault)
- **Where Not to Use:**  
  - Between strangers without secure key exchange  
  - Public APIs with exposed keys

---

## **6. Asymmetric Encryption**
- **Concept:** Public key (encrypt) + private key (decrypt).
- **Advantages:** Solves key distribution, enables digital signatures.
- **Disadvantages:** Slower than symmetric.
- **Examples:** RSA, ECC.
- **Where to Use:**  
  - TLS 1.3 HTTPS handshakes  
  - Signal Protocol key exchange  
  - ProtonMail secure email
- **Where Not to Use:**  
  - Bulk data encryption (too slow)  
  - Low‑power IoT without crypto acceleration

---

## **7. Hashing**
- **Definition:** One‑way transformation to fixed‑length digest.
- **Properties:** Deterministic, irreversible, collision‑resistant.
- **Examples:** SHA‑256, SHA‑3, Argon2.
- **Where to Use:**  
  - Password storage (with salt)  
  - File integrity checks  
  - Blockchain transaction verification
- **Where Not to Use:**  
  - As encryption (cannot be reversed)  
  - Password storage without salt

---

## **8. Digital Signatures**
- **Purpose:** Verify authenticity & integrity.
- **Process:** Hash → encrypt hash with private key → verify with public key.
- **Examples:** RSA signatures, ECDSA, EdDSA.
- **Where to Use:**  
  - Code signing (Windows, Apple updates)  
  - Legal e‑signatures (DocuSign)  
  - Blockchain smart contracts
- **Where Not to Use:**  
  - Without verifying certificate authenticity  
  - On mutable data without re‑signing

---

## **9. Data Protection Measures**
- **Technical Controls:** Encryption (at rest/in transit), access control, DLP tools, firewalls, IDS/IPS.
- **Organizational Controls:** Privacy policies, employee training, incident response plans.
- **Legal Compliance:** GDPR, DPDP Act 2023, HIPAA, CCPA.

---

## **10. Emerging Trends**
- **Post‑Quantum Cryptography (PQC):** CRYSTALS‑Kyber, Dilithium (NIST 2024 drafts).  
- **Zero‑Knowledge Proofs (ZKPs):** zk‑SNARKs in privacy‑preserving blockchains.  
- **Confidential Computing:** Intel SGX, AMD SEV – encrypt data in use.  
- **Homomorphic Encryption:** Process encrypted data without decrypting (Microsoft SEAL, IBM HELib).
---
# **UNIT 3 – Data Collection, Use and Reuse**  
---

## **1. Harms Associated with Data Collection, Use and Reuse**

### **A. Individual Harms**
- **Loss of Privacy:** Personal details exposed without consent.  
- **Identity Theft:** Stolen data used for fraud.  
- **Profiling & Discrimination:** Targeted ads, biased hiring, insurance premium hikes.

### **B. Organizational Harms**
- **Reputation Damage:** Loss of customer trust after misuse.  
- **Legal Penalties:** Non‑compliance with GDPR, DPDP Act, HIPAA.  
- **Data Breach Fallout:** Financial loss, operational disruption.

### **C. Societal Harms**
- **Surveillance State:** Mass monitoring eroding freedoms.  
- **Misinformation Amplification:** Data misuse in political campaigns.  
- **Digital Divide:** Unequal access to privacy protections.

**Latest Example (2024):**  
- **Cambridge Analytica‑style micro‑targeting** re‑emerging in smaller political campaigns using scraped social media data.  
- **AI facial recognition misuse** in public spaces without consent.

---

## **2. Introduction to Data Anonymization**
- **Definition:**  
  Process of removing or altering personal identifiers so individuals cannot be directly or indirectly identified.
- **Goal:**  
  Enable data analysis/use while protecting privacy.
- **Key Difference from Encryption:**  
  - Encryption is reversible with a key.  
  - Anonymization is (ideally) irreversible.

---

## **3. Data Anonymization Techniques**

| **Technique** | **Description** | **Where to Use** | **Where Not to Use / Limitations** | **Example** |
|---------------|-----------------|------------------|-------------------------------------|-------------|
| **Masking** | Replace real values with fictional but realistic data | Testing environments, demos | Production analytics needing accurate values | Masking credit card numbers in call center logs |
| **Pseudonymization** | Replace identifiers with pseudonyms | Research datasets needing re‑linking | Public release datasets (still re‑identifiable) | Assigning patient IDs instead of names |
| **Generalization** | Reduce precision of data | Publishing aggregated stats | When high precision is critical | Age → Age range |
| **Suppression** | Remove certain data fields entirely | Removing rare disease names in public health data | When field is essential for analysis | Removing exact GPS coordinates |
| **Data Perturbation** | Add noise to data values | Statistical analysis | When exact values are critical | Adding ±2% noise to salaries |
| **K‑Anonymity** | Ensure each record is indistinguishable from ≥k‑1 others | Public dataset releases | Vulnerable to attribute linkage attacks | Census data grouping |
| **Differential Privacy** | Add mathematically calibrated noise to protect individuals | Large‑scale statistical queries | Small datasets (noise may distort results) | Apple iOS telemetry, US Census 2020 |

---

## **4. Challenges in Anonymizing Data**
- **Re‑identification Risk:** Cross‑referencing with other datasets can reveal identities.  
- **Data Utility vs. Privacy Trade‑off:** More anonymization → less accuracy.  
- **Dynamic Data:** Streaming or frequently updated datasets are harder to anonymize.  
- **High‑Dimensional Data:** Many attributes increase re‑identification risk.  
- **Evolving Threats:** New AI models can deanonymize data more effectively.

**Latest Example (2023–2024):**  
- Researchers deanonymized “anonymous” mobility datasets using public social media check‑ins.  
- Generative AI models inferring personal details from partially anonymized text.

---

## **5. Real‑World Use Cases**

### **Where to Use Anonymization**
- **Healthcare Research:** Share patient data without violating HIPAA/DPDP Act.  
- **Public Statistics:** Census, transport usage, COVID‑19 case data.  
- **Product Analytics:** Aggregate user behavior without tracking individuals.

### **Where Not to Use Anonymization**
- **Fraud Detection:** Needs identifiable transaction data.  
- **Personalized Services:** Recommendation engines require user‑linked data.  
- **Legal Evidence:** Courts require original, unaltered data.

---

## **6. Best Practices**
- Combine multiple anonymization techniques for stronger protection.  
- Regularly assess re‑identification risk.  
- Apply **Privacy by Design** — plan anonymization at the start of data collection.  
- Maintain a data inventory to track sensitive fields.  
- Follow legal frameworks (GDPR Art. 25, DPDP Act 2023).

---

# **UNIT 4 – Ethical Considerations in Data Privacy**

---

## **1. Privacy and Surveillance**

### **A. Privacy as an Ethical Right**
- **Definition:** The moral right of individuals to control their personal information and be free from unwarranted intrusion.
- **Ethical Basis:**  
  - **Autonomy:** Respecting individuals’ ability to make informed choices.  
  - **Dignity:** Treating people as ends, not means (Kantian ethics).  
  - **Fairness:** Avoiding exploitation of personal data.

### **B. Surveillance**
- **Definition:** Continuous or systematic monitoring of individuals’ activities, communications, or data.
- **Types:**  
  - **Government Surveillance:** National security monitoring, CCTV, internet traffic interception.  
  - **Corporate Surveillance:** Tracking user behavior for targeted advertising.  
  - **Workplace Surveillance:** Monitoring employee emails, keystrokes, or location.
- **Ethical Concerns:**  
  - Chilling effect on free speech.  
  - Potential abuse of power.  
  - Disproportionate targeting of certain groups.

**Latest Example (2024):**  
- **EU AI Act debates** over regulating facial recognition in public spaces.  
- **India’s CCTNS expansion** raising concerns about mass surveillance without strong oversight.

---

## **2. Ethics of Data Collection and Use**

### **A. Ethical Principles**
- **Informed Consent:** Data subjects must understand what is collected and why.  
- **Purpose Limitation:** Use data only for the stated purpose.  
- **Data Minimization:** Collect only what is necessary.  
- **Transparency:** Clear communication about data practices.  
- **Accountability:** Organizations must take responsibility for misuse.

### **B. Ethical Dilemmas**
- **Public Good vs. Individual Privacy:**  
  - Example: Using location data for pandemic contact tracing.  
- **Secondary Use:**  
  - Data collected for one purpose later used for another without consent.

**Latest Example (2023–2024):**  
- **Google’s AI health research** criticized for using patient data without explicit consent.  
- **Ride‑hailing apps** using trip data for unrelated marketing.

---

## **3. Bias and Discrimination in Data Analysis**

### **A. Sources of Bias**
- **Data Bias:** Historical inequalities embedded in datasets.  
- **Algorithmic Bias:** Model design choices amplifying unfairness.  
- **Sampling Bias:** Non‑representative data leading to skewed results.

### **B. Ethical Risks**
- **Discrimination:**  
  - In hiring (AI rejecting candidates from certain backgrounds).  
  - In lending (credit scoring disadvantaging minorities).  
- **Reinforcement of Stereotypes:** Predictive policing targeting specific communities.

### **C. Mitigation Strategies**
- **Bias Audits:** Regularly test algorithms for fairness.  
- **Diverse Data:** Ensure datasets represent all relevant groups.  
- **Explainability:** Make AI decisions interpretable.

**Latest Example (2024):**  
- **Amazon’s AI recruitment tool** retired after bias against women.  
- **US mortgage AI systems** investigated for racial disparities in loan approvals.

---

## **4. Best Practices for Ethical Data Handling**
- Embed **Privacy by Design** and **Ethics by Design** in all projects.  
- Conduct **Ethical Impact Assessments** alongside Privacy Impact Assessments.  
- Establish independent **Ethics Review Boards** for high‑risk data projects.  
- Train staff on **ethical decision‑making** in data handling.  
- Engage with stakeholders, including affected communities.

---

## **5. Where to Apply / Avoid Certain Practices**

| **Practice** | **Where to Apply** | **Where Not to Apply** |
|--------------|--------------------|------------------------|
| **Surveillance** | High‑security zones, fraud detection with oversight | Mass public monitoring without consent or safeguards |
| **Data Collection** | Research with informed consent, regulated industries | Collecting unrelated data “just in case” |
| **Automated Decision‑Making** | Low‑risk personalization (e.g., content recommendations) | High‑stakes decisions without human review (e.g., criminal sentencing) |
