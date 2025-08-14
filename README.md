
🗺️ Campus Navigator

A web-based campus navigation system built using Django that helps users find optimal paths between locations on campus using an unweighted graph algorithm.

⸻

🚀 Features
	•	📍 Interactive Map: Displays campus layout with buildings and paths
	•	🔍 Find Path: Calculates shortest path between two selected locations
	•	🏫 Building Information: Displays details for each location
	•	🔒 User Authentication: Secure login and registration system
	•	🌐 Responsive UI: Works seamlessly on desktop and mobile devices

⸻

🛠 Tech Stack

Frontend	Backend	Database	Tools	Methodology
HTML, CSS, JavaScript	Django	SQLite	Git, GitHub	Agile


⸻

📸 Screenshots

|| Login Page ||	Registration Page ||	Home Page and Map View ||
|| <img width="2940" height="1596" alt="login page" src="https://github.com/user-attachments/assets/d875f326-1e96-4870-bffc-0c915936209f" /> ||
<img width="2940" height="1596" alt="registration page" src="https://github.com/user-attachments/assets/0a051db4-1963-45c0-a973-30f40f2cae02" /> ||
<img width="2940" height="1596" alt="homepage" src="https://github.com/user-attachments/assets/ac6c3085-8529-4cad-8281-e1c05bd0c3b9" /> ||





⸻

🔧 Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/Izaz-123/Campus_Navigator.git
cd Campus_Navigator

2️⃣ Create a Virtual Environment

python -m venv .venv

3️⃣ Activate the Virtual Environment
	•	Windows:

.venv\Scripts\activate

	•	Mac/Linux:

source .venv/bin/activate

4️⃣ Install Dependencies

pip install -r requirements.txt

5️⃣ Run Migrations

python manage.py migrate

6️⃣ Start the Development Server

python manage.py runserver

7️⃣ Access the App

Open your browser and go to:

http://127.0.0.1:8000


⸻

📍 How It Works
	•	The map is represented as an unweighted graph in Django backend.
	•	When a user selects two locations, the system uses Breadth-First Search (BFS) to find the shortest path.
	•	The path is then displayed visually on the campus map.

⸻

👤 Author

Mohammad Izaz
📧 Email: izazofficial123@gmail.com
🌐 GitHub: Izaz-123
