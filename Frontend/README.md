# Simple Upload App

A clean and simple React application for uploading pictures and recording audio.

## Features

- 📸 **Image Upload**: Upload and preview images
- 🎤 **Audio Recording**: Record audio using your microphone
- 🎨 **Clean UI**: Modern, responsive design
- 📱 **Mobile Friendly**: Works on all devices

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn
- Modern browser with microphone access

### Installation

```bash
npm install
```

### Running the Development Server

```bash
npm run dev
```

The app will start on `http://localhost:5173`

## Usage

### Upload Picture
1. Click "Choose Image" button
2. Select an image file from your device
3. The image will be displayed as a preview

### Record Audio
1. Click "🎤 Start Recording" button
2. Allow microphone access when prompted
3. Speak into your microphone
4. Click "⏹️ Stop Recording" when done
5. Play back your recorded audio

## Features Explained

### Image Upload
- Supports all common image formats (JPEG, PNG, GIF, etc.)
- Real-time preview
- Responsive image display

### Audio Recording
- Uses Web Audio API
- Records in WAV format
- Built-in audio player for playback
- Automatic microphone permission handling

### User Experience
- Simple, intuitive interface
- Visual feedback for all actions
- Responsive design for mobile and desktop
- Smooth animations and transitions

## Build for Production

```bash
npm run build
```

## Preview Production Build

```bash
npm run preview
```

## Technologies Used

- **React 18** - UI library
- **Vite** - Build tool and dev server
- **CSS3** - Modern styling with gradients
- **Web Audio API** - Audio recording functionality
- **File API** - Image upload and preview

## Browser Compatibility

- Chrome 66+
- Firefox 60+
- Safari 14+
- Edge 79+

## Project Structure

```
src/
├── App.jsx          # Main application component
├── App.css          # Application styles
├── main.jsx         # Application entry point
└── index.css        # Global styles
```

## Notes

- Audio recording requires HTTPS in production (or localhost for development)
- Microphone access must be granted by the user
- Images are stored temporarily in the browser (not uploaded to server)
- Audio recordings are stored temporarily in the browser (not uploaded to server)
