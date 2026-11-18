# GlucoseCircle

To try GlucoCircle locally:

1. Download the project

git clone <(https://github.com/sphasakda/GlucoCircle)>
cd GlucoCircle

2. Set up the backend

python -m venv venv

Activate the environment on Windows Git Bash:

source venv/Scripts/activate

Install the required packages:

pip install -r requirements.txt

3. Add your API key

Create a .env file in the main project folder and add:

ANTHROPIC_API_KEY=your_api_key_here

4. Start the backend

python -m backend.app

5. Start the app

Open another terminal:

cd frontend
npm install
npm run dev

Open the local address provided by Vite in your browser.
