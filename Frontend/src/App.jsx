import { useState, useRef } from 'react'
import './App.css'

function App() {
  const [selectedImage, setSelectedImage] = useState(null)
  const [isRecording, setIsRecording] = useState(false)
  const [audioBlob, setAudioBlob] = useState(null)
  const [audioUrl, setAudioUrl] = useState(null)
  const mediaRecorderRef = useRef(null)
  const audioChunksRef = useRef([])

  // Handle image upload
  const handleImageUpload = (event) => {
    const file = event.target.files[0]
    if (file) {
      setSelectedImage(URL.createObjectURL(file))
    }
  }

  // Start recording audio
  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      mediaRecorderRef.current = new MediaRecorder(stream)
      audioChunksRef.current = []

      mediaRecorderRef.current.ondataavailable = (event) => {
        audioChunksRef.current.push(event.data)
      }

      mediaRecorderRef.current.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/wav' })
        const audioUrl = URL.createObjectURL(audioBlob)
        setAudioBlob(audioBlob)
        setAudioUrl(audioUrl)
      }

      mediaRecorderRef.current.start()
      setIsRecording(true)
    } catch (error) {
      console.error('Error accessing microphone:', error)
      alert('Error accessing microphone. Please allow microphone access.')
    }
  }

  // Stop recording audio
  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop()
      mediaRecorderRef.current.stream.getTracks().forEach(track => track.stop())
      setIsRecording(false)
    }
  }

  return (
    <div className="app">
      <header className="app-header">
        <h1>Simple Upload App</h1>
        <p>Upload a picture and record audio</p>
      </header>

      <main className="app-main">
        {/* Image Upload Section */}
        <div className="section">
          <h2>Upload Picture</h2>
          <div className="upload-area">
            <input
              type="file"
              accept="image/*"
              onChange={handleImageUpload}
              id="image-upload"
              className="file-input"
            />
            <label htmlFor="image-upload" className="upload-button">
              Choose Image
            </label>
          </div>
          {selectedImage && (
            <div className="image-preview">
              <img src={selectedImage} alt="Preview" />
            </div>
          )}
        </div>

        {/* Audio Recording Section */}
        <div className="section">
          <h2>Record Audio</h2>
          <div className="audio-controls">
            {!isRecording ? (
              <button onClick={startRecording} className="record-button">
                🎤 Start Recording
              </button>
            ) : (
              <button onClick={stopRecording} className="stop-button">
                ⏹️ Stop Recording
              </button>
            )}
          </div>
          {audioUrl && (
            <div className="audio-preview">
              <h3>Recorded Audio:</h3>
              <audio controls src={audioUrl} />
            </div>
          )}
        </div>
      </main>
    </div>
  )
}

export default App
