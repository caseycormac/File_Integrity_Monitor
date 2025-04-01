# File_Integrity_Monitor
File Integrity Monitor
Vulnerability Management
Cormac Casey

What is my Project? 

My File Integrity Monitor (FIM) project is a crucial tool designed to enhance data security and integrity by detecting changes made to files within a specified directory (Baseline). In today's digital landscape, where data breaches and unauthorized modifications are prevalent concerns, having a reliable mechanism to monitor file changes is essential. This project leverages cryptographic hashing techniques to create a “baseline” of file integrity, providing the user with the ability to identify modifications to files in real time.

How does my Project Work?

The operation of the File Integrity Monitor is divided into two primary phases: baseline collection and ongoing monitoring.

In the baseline collection phase, the program scans a designated directory (./Files) and calculates the SHA-512 hash for each file present. This hash serves as a unique fingerprint for the file's contents. Once calculated, these hashes are stored in a file named “baseline.txt”, with each entry consisting of the file path followed by its corresponding hash. This initial step ensures that a secure reference point is established, which will be used for future comparisons.

The second phase, monitoring, begins when the user opts to check the integrity of the files against the stored baseline. During this process, the program reads the “baseline.txt” file and retrieves the previously stored hashes. It then recalculates the current hash for each file in the directory. The heart of the monitoring function lies in the comparison between the current hash and the baseline hash. If discrepancies are found it indicates that a file has been modified, the program then flags this change, notifying the user. Furthermore, if any files have been deleted since the last baseline was collected, the monitor will report these deletions as well. This dual approach not only helps in identifying unauthorized changes but also aids in maintaining an audit trail for compliance and security purposes.


What are the Purposes and Uses of my project?

The File Integrity Monitor serves several critical purposes in the realms of cybersecurity and data management. 
Firstly, it acts as a protective measure against unauthorized access or tampering. In an age where data integrity is paramount, this tool helps the user safeguard sensitive files by ensuring that any changes made to files are logged and reported.
Secondly, the project serves compliance needs for organizations required to adhere to regulatory standards such as GDPR, which mandate strict monitoring and reporting of any file changes. By maintaining a detailed record of modifications, the FIM project assists organizations in demonstrating compliance during audits and assessments.
Thirdly, the File Integrity Monitor is invaluable for change detection in dynamic environments, where files may frequently be modified. Whether in a corporate setting, a government institution, or personal projects, having the ability to track changes provides peace of mind and helps to identify potential security breaches swiftly.

Langauges, Hardware, Software and Librarys used:

•	Python
•	import hashlib
•	import os
•	from time import sleep, strftime
•	from getpass import getuser
•	Personal Laptop
•	Kali Linux WSL
•	Microsoft Word (Documentation)

Problem Statement:

Organizations today face an increasing threat of unauthorized modifications to critical files, which can compromise the integrity and confidentiality of their systems. File tampering, whether due to malicious intent or accidental changes, poses significant risks in the form of data breaches, operational disruptions, or regulatory non-compliance.
Despite the availability of advanced security tools, many small- to medium-sized businesses and personal users lack access to cost-effective, straightforward solutions to monitor file integrity. This creates a gap where sensitive files remain vulnerable to undetected changes, especially in environments without real-time monitoring systems.
The project addresses this issue by developing a File Integrity Monitor (FIM) using Python. This tool will calculate and compare hash values of monitored files to detect changes. It aims to provide an accessible, lightweight, and customizable solution that can alert users to file modifications, deletions, or unauthorized additions, ensuring the integrity of sensitive data.
The proposed FIM system will demonstrate the practicality of leveraging Python libraries to achieve an effective and simple security tool suitable for educational purposes, individual users, or small-scale environments.

Result:

The File Integrity Monitor (FIM) developed as part of my project successfully demonstrates the importance of monitoring file changes to ensure data integrity and system security. By using Python’s built-in libraries and hash-based comparison techniques, the tool provides an efficient solution for detecting unauthorized file modifications, deletions, or additions.

This project highlights how straightforward programming techniques can be employed to address a critical cybersecurity concern, making file monitoring accessible to smaller organizations, personal users, and students. Additionally, the FIM serves as a foundation for future enhancements, such as real-time monitoring, integration with notification systems, and support for larger, more complex environments.

Overall, my project underscores the value of lightweight, customizable tools in enhancing security practices and reinforces the importance of integrity checks in protecting sensitive data from malicious actors or accidental alterations.
