EmptySea Framework by ndurrani

EmptySea is a tactical network security framework designed for rapid service discovery, protocol auditing, and infrastructure stress testing. It provides a centralized command center for security researchers to execute complex network tools through a streamlined, automated interface.

🚀 Key Features
Service Fingerprinting: Automated HTTP header collection and advanced Nmap scanning profiles.

SSH Firmware Audit: Secure, automated interaction with vendor-specific devices (Linux, Huawei, Hikvision).

Layer-2 Testing: Automated DHCP exhaustion and network isolation testing via the Yersinia engine.

Traffic Evaluation: Advanced packet manipulation and firewall testing using the Hping3 engine.

Persistent Logging: Automatic session logging with timestamps for all executed modules, ensuring audit trail integrity.

📋 Prerequisites
EmptySea requires a Linux-based operating system (Kali Linux is recommended). You must have the following system tools and Python libraries installed:

1. System Dependencies
Install the required network utilities:

Bash
sudo apt update
sudo apt install nmap hping3 yersinia -y
2. Python Dependencies
Install the necessary Python libraries:

Bash
pip3 install paramiko requests
🛠 Installation
Clone the repository to your local machine:

Bash
git clone https://github.com/ndurrani-ipo/EmptySea-Framework.git
cd EmptySea-Framework
Ensure the script has execute permissions:

Bash
chmod +x ES.py
💻 How to Run
Because this framework interacts with low-level network protocols (raw sockets, packet injection), you must run the script with root privileges:

Bash
sudo python3 ES.py
Usage Workflow:
Target Initialization: Upon startup, you will be prompted to enter the Target IP and optional SSH credentials.

Dashboard: Select the operational vector (1-6) you wish to execute.

Log Storage: All outputs are automatically saved to the /logs directory created within the script's folder.

⚠️ Safety & Legal Disclaimer
This software is for authorized security testing and educational purposes only. Testing infrastructure you do not own or have explicit written permission to audit is illegal and unethical. The author of EmptySea assumes no liability for any damage, unauthorized access, or legal consequences arising from the misuse of this tool. Use responsibly and keep all testing within the scope of your authorized engagements.

💡 Best Practices for the Community
Network Hygiene: Always perform a dry run on a controlled virtual lab environment before targeting live infrastructure.

Reporting: Ensure that you document your findings ethically and inform the system owners of any identified vulnerabilities immediately.

Updates: If you add new modules or find bugs, feel free to submit a Pull Request to help improve the framework for the community.

📝 License
Distributed under the MIT License. See the LICENSE file for more information.

