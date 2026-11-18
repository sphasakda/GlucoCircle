# GlucoCircle

**Diabetes support, made more connected.**

GlucoCircle is a family-oriented diabetes support platform designed to help people better understand their glucose patterns, explore nutrition, and feel more supported in managing diabetes.

The project is currently a working prototype, with a focus on FreeStyle Libre users and the potential to support additional continuous glucose monitors (CGMs) in the future.

## The Problem

Managing diabetes involves more than checking glucose levels. Understanding glucose patterns, making nutrition decisions, and keeping loved ones informed can be challenging.

GlucoCircle aims to bring these pieces together in one accessible platform.

## Our Solution

GlucoCircle combines glucose insights, nutrition information, and AI-powered assistance to make diabetes management easier to understand.

### Features

- **Glucose Dashboard** — View glucose readings and basic statistics in one place.
- **Nutrition Explorer** — Search foods, adjust portion sizes, and view estimated nutritional information.
- **Mira, AI Assistant** — Ask questions and receive easy-to-understand explanations about glucose patterns and nutrition.
- **My Circle** — A planned family-support feature designed to help users stay connected with the people who support them.

## Technology

| Technology | Purpose |
|---|---|
| React | User interface |
| Python and Flask | Backend and API |
| Claude API | AI-powered assistant |
| Open Food Facts | Food and nutrition information |

## Running GlucoCircle Locally

### Requirements

Before getting started, make sure you have:
- Python installed
- Node.js and npm installed
- An Anthropic API key

### Setup Instructions

**1. Clone the repository**

Open your terminal and run:

```bash
git clone https://github.com/sphasakda/GlucoCircle
cd GlucoCircle
```

**2. Create a Python virtual environment**

From the main GlucoCircle folder, run:

```bash
python -m venv venv
```

**3. Activate the virtual environment**

For Windows Git Bash:

```bash
source venv/Scripts/activate
```

**4. Install the backend dependencies**

Make sure you are in the main GlucoCircle folder, then run:

```bash
pip install -r requirements.txt
```

**5. Add your API key**

Create a file named `.env` in the main GlucoCircle folder and add:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Anthropic API key. Do not share or commit this file.

**6. Start the backend**

In the main GlucoCircle folder, run:

```bash
python -m backend.app
```

Keep this terminal open while using the application.

**7. Open a second terminal and start the frontend**

Navigate to the frontend folder:

```bash
cd frontend
```

Install the frontend dependencies:

```bash
npm install
```

Then start the development server:

```bash
npm run dev
```

**8. Open GlucoCircle in your browser**

Once the frontend server starts, open:

`http://localhost:5173`

You should now be able to use GlucoCircle locally!

## What's Next?

GlucoCircle is an evolving project. Future improvements include:

- FreeStyle Libre data integration
- Support for additional CGM devices
- Expanded family and caregiver features
- More personalized nutrition insights
- Improvements to Mira's glucose analysis and assistance

## Important Note

This is an early-stage prototype. Glucose readings currently use simulated demo data and are not connected to an actual FreeStyle Libre device.

GlucoCircle is intended for educational and informational support. It is not a substitute for professional medical advice, diagnosis, or treatment.

---

**Built with the goal of making diabetes support more understandable, accessible, and connected.**
