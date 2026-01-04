import { useEffect, useState } from 'react'
import { FileUploader } from './components/FileUploader'
import { useTheme } from './context/ThemeContext'
import './App.css'

function App() {
  const [isMobile, setIsMobile] = useState(false)
  const { theme, toggleTheme } = useTheme()

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 1024)
    }

    checkMobile()
    window.addEventListener('resize', checkMobile)
    return () => window.removeEventListener('resize', checkMobile)
  }, [])

  if (isMobile) {
    return (
      <div className="mobile-blocker">
        <div className="glass-card p-6 text-center">
          <h1 className="text-xl font-bold mb-3">Desktop Only</h1>
          <p className="text-slate-400 text-sm">Please use a screen width of 1024px or wider for the best experience.</p>
        </div>
      </div>
    )
  }

  return (
    <div className="app-shell">
      <header className="app-header">
        <div className="header-content">
          <div className="logo">
            <img src="/favicon.png" alt="PDF Hero Logo" className="w-6 h-6 object-contain" />
            <span className="brand-text">PDF Hero</span>
          </div>

          <button
            onClick={toggleTheme}
            className="theme-toggle"
            aria-label="Toggle Theme"
          >
            {theme === 'light' ? (
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
              </svg>
            ) : (
              <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364-6.364l-.707.707M6.343 17.657l-.707.707m12.728 0l-.707-.707M6.343 6.343l-.707-.707M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            )}
          </button>
        </div>
      </header>

      <main className="app-main">
        <section className="main-panel animate-fade-in">
          <div className="hero-text">
            <h1 className="hero-title">File to PDF, <br />Instantly.</h1>
            <p className="hero-subtitle">Convert your Word documents and images to high-quality PDF files for free. No accounts, no limits.</p>
          </div>

          <div className="uploader-wrapper">
            <FileUploader />
          </div>
        </section>
      </main>

      <footer className="app-footer">
        <div className="footer-meta">&copy; {new Date().getFullYear()} RJ PDF Hero. All rights reserved. Privacy Policy | Terms of Service</div>
      </footer>
    </div>
  )
}

export default App
