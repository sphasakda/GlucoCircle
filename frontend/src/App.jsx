// frontend/src/App.jsx
import { useState, useEffect } from 'react'
import './App.css'

// Main App component, which serves as the entry point for the GlucoCircle application.
function App() {

  // Store glucose data from Flask backend
  const [glucoseData, setGlucoseData] = useState(null)

  // Track loading status and any errors that occur during data fetching
  const [loading, setLoading] = useState(true)

  // Store potential error messages for display to the user
  const [error, setError] = useState(null)

  // State variable to track the currently active tab in the application, allowing for dynamic content rendering based on user navigation.
  const [activeTab, setActiveTab] = useState('Home')

  // Fetch glucose data from the Flask backend API when the page loads
  useEffect(() => {
  fetch('http://127.0.0.1:5000/api/glucose')
    .then(response => {
      if (!response.ok) {
        throw new Error('Could not retrieve glucose data')
      }
      return response.json()
    })
    .then(data => {
      setGlucoseData(data)
      setLoading(false)
    })
    .catch(error => {
      setError(error.message)
      setLoading(false)
    })
}, [])

// Define the navigation items for the bottom navigation bar
  const navigation = [
    { name: 'Home', icon: '⌂' },
    { name: 'Trends', icon: '↗' },
    { name: 'Nutrition', icon: '𓌉◯𓇋' },
    { name: 'Mira', icon: '₍^. .^₎Ⳋ' },
    { name: 'My Circle', icon: '𖠋♡𖠋' },
  ]

  // Render the main application UI, including the header, main content area, and bottom navigation bar.
  return (
    <div className="app">
      <header className="topbar">
        <a className="logo" href="#" onClick={() => setActiveTab('Home')}>
          <span className="logo-icon">G</span>
          GlucoCircle
        </a>
        <div className="profile">
          <span className="profile-avatar">☺</span>
          <span>My Account</span>
        </div>
      </header>

  {/*Main content area that changes based on the active tab, including a welcome section, glucose card, insights, and tools for the user.*/} 
      <main className="main">
        <section className="welcome">
          <p className="eyebrow">YOUR PERSONAL HEALTH COMPANION</p>
          <h1>{activeTab === 'Home' ? 'A little check-in ☀️' : activeTab}</h1>
          <p className="subtitle">
            {activeTab === 'Home'
              ? "Your health journey, one day at a time."
              : `Welcome to your ${activeTab.toLowerCase()} space.`}
          </p>
        </section>

{/*Conditional rendering of the main content based on the tab that is active*/}
        {activeTab === 'Home' && (
          <>
            <section className="glucose-card">
              <div className="card-heading">
                <span className="small-label">YOUR GLUCOSE</span>
                <span className="status-pill">Sample data</span>
              </div>

{/* Displaying the latest glucose reading in a prominent format, with the value and unit clearly indicated. */}
              <div className="glucose-reading">
              <span className="reading-number">
                {loading
                  ? '...'
                  : error
                    ? '--'
                    : glucoseData?.readings?.at(-1)?.value ?? '--'}
              </span>

                <span className="reading-unit">mg/dL</span>
              </div>

              <p className="glucose-note">
                {loading
                  ? 'Loading your readings...'
                  : error
                    ? error
                    : 'Your latest simulated glucose reading.'}
              </p>

              <div className="glucose-footer">
                <span>𓌉◯𓇋</span>
                Simulated CGM reading · Not live data
              </div>
            </section>

{/* Section providing insights from Mira, the AI assistant, to help users understand their glucose data and trends. */}
            <section className="insight-section">
              <div className="section-title">
                <span className="mira-icon">₍^. .^₎Ⳋ</span>
                <div>
                  <h2>A note from Mira</h2>
                  <p>A little insight to help you understand your data.</p>
                </div>
              </div>

              <div className="insight-card">
                <p>
                  Your recent sample readings show a gradual rise followed
                  by a decline. You can explore the trend whenever you're ready.
                </p>
                <button onClick={() => setActiveTab('Trends')}>
                  Explore your trends →
                </button>
              </div>
            </section>

{/* Displaying the different tools available in the app, each represented by a card with an icon, title, description, and an arrow indicating navigation. */}
            <section className="tools-section">
              <div className="section-title">
                <div>
                  <h2>Your everyday tools</h2>
                  <p>Everything you need, all in one place.</p>
                </div>
              </div>

{/* Grid layout for the different tool cards, each representing a feature of the app. */}
              <div className="tools-grid">
                <button className="tool-card nutrition" onClick={() => setActiveTab('Nutrition')}>
                  <span className="tool-icon">𓌉◯𓇋</span>
                  <h3>Nutrition</h3>
                  <p>Explore foods and understand their nutrition.</p>
                  <span className="tool-arrow">→</span>
                </button>

{/* New tool card for "My trends" to allow users to view their glucose patterns and trends over time. */}
                <button className="tool-card trends" onClick={() => setActiveTab('Trends')}>
                  <span className="tool-icon">↗</span>
                  <h3>My trends</h3>
                  <p>Get a closer look at your glucose patterns.</p>
                  <span className="tool-arrow">→</span>
                </button>

{/* New tool card for "Talk to Mira" to allow users to interact with the AI assistant for health insights and guidance. */}
                <button className="tool-card mira" onClick={() => setActiveTab('Mira')}>
                  <span className="tool-icon">₍^. .^₎Ⳋ</span>
                  <h3>Talk to Mira</h3>
                  <p>Ask questions and explore your health data.</p>
                  <span className="tool-arrow">→</span>
                </button>

{/* New tool card for "My Circle" to allow users to stay connected with their family and friends they choose to add to their circle. */}
                <button className="tool-card family" onClick={() => setActiveTab('My Circle')}>
                  <span className="tool-icon">𖠋♡𖠋</span>
                  <h3>My Circle</h3>
                  <p>Stay connected with the people who support you.</p>
                  <span className="tool-arrow">→</span>
                </button>
              </div>
            </section>
          </>
        )}

{/* Placeholder section for tabs other than 'Home', displaying the active tab's icon and name, along with a back button to return to the home view. */}
        {activeTab !== 'Home' && (
          <section className="placeholder">
            <span className="placeholder-icon">
              {navigation.find(item => item.name === activeTab)?.icon}
            </span>
            <h2>{activeTab}</h2>
            <p>This is where your {activeTab.toLowerCase()} experience will live.</p>
            <button onClick={() => setActiveTab('Home')}>
              ← Back to home
            </button>
          </section>
        )}
      </main>

{/* Bottom navigation bar that allows users to switch between different sections of the app. */}
      <nav className="bottom-nav">
        {navigation.map(item => (
          <button
            key={item.name}
            className={activeTab === item.name ? 'nav-item active' : 'nav-item'}
            onClick={() => setActiveTab(item.name)}
          >
            <span className="nav-icon">{item.icon}</span>
            <span>{item.name}</span>
          </button>
        ))}
      </nav>
    </div>
  )
}

export default App
