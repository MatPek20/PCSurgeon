# PC Surgeon

PC Surgeon is a modern desktop utility suite built with Python and CustomTkinter that combines system monitoring, file security, storage analysis, and network diagnostics into a single application.
Designed with a responsive multi-threaded architecture, PC Surgeon performs intensive operations in the background while maintaining a smooth and interactive user experience.

## **Features**

1.	System Monitoring Dashboard
Monitor your computer's performance in real time.
Included Metrics
•	Live CPU Usage Monitoring
•	Live RAM Usage Monitoring
•	Dynamic Circular Usage Gauges
•	System Status Indicators
•	Top 5 Resource-Consuming Processes
•	Auto Refresh Updates

2.	Privacy Vault
Secure sensitive files using modern encryption techniques.
Features
•	AES-256 File Encryption
•	AES-256 File Decryption
•	Password-Based Key Generation (PBKDF2)
•	Secure File Protection
•	Automatic Password Field Clearing

3.	Duplicate File Finder
Identify and manage duplicate files efficiently.
Features
•	SHA-256 File Hashing
•	Duplicate File Detection
•	Folder Scanning
•	Original File Identification
•	Storage Optimization Assistance

4.	Network Diagnostics
Quickly check internet connectivity and network responsiveness.
Features
•	HTTP/HTTPS Connectivity Testing
•	Network Latency Measurement
•	Response Time Analysis
•	Connection Health Assessment
Health classifications:
Latency	Status
< 100 ms	Excellent
100–300 ms	Stable
> 300 ms	High Latency


## **Screenshots**
<img width="954" height="608" alt="dashboard" src="https://github.com/user-attachments/assets/4f6e7d21-b5e3-4f99-b71a-899e9ade6f22" />
<img width="981" height="475" alt="Secure Vault" src="https://github.com/user-attachments/assets/df152ba8-466b-4e87-90cb-9bea8709904e" />
<img width="943" height="704" alt="redudnant file" src="https://github.com/user-attachments/assets/e4c174a9-51fe-41f6-bc3a-5874924c4cf0" />
<img width="978" height="489" alt="ping latency" src="https://github.com/user-attachments/assets/f2d40158-0667-46ab-88a0-855e2d796dc3" />




## **Architecture**

The application follows a modular layered design:
main.py
Application entry point and dependency initialization.
ui.py
Handles graphical interface components, user interactions, and background task management.
engine.py
Core processing layer responsible for:
•	Encryption & Decryption
•	Duplicate File Detection
•	Network Diagnostics
•	System Operations
metrics.py
Responsible for:
•	Hardware Telemetry Collection
•	Resource Monitoring
•	Dashboard Visualization Components



## Technologies Used

•	Python 3.x

•	CustomTkinter

•	Psutil

•	Cryptography

•	Threading

•	Hashlib

•	Requests


## Installation

Clone the repository:

git clone https://github.com/MatPek20/PCSurgeon.git

Move into the project directory:

cd PC-Surgeon

Install dependencies:

pip install -r requirements.txt

Or install manually:

pip install customtkinter psutil cryptography requests

Run the application:

python main.py

Security Notes

PC Surgeon uses:

•	AES-256 encryption through the Cryptography library

•	PBKDF2 password-based key derivation

•	SHA-256 hashing for duplicate file analysis

•	Background worker threads for long-running operations

No user data is transmitted to external servers.



## Future Improvements

•	Disk Health Monitoring

•	GPU Monitoring

•	Dark/Light Theme Toggle

•	Scheduled System Scans

•	Exportable Diagnostic Reports

•	Advanced Network Analysis Tools

(Will update soon)



## **Author**

Developed by MatPek20

## Support
If you found this project useful, consider giving it a star on GitHub.

