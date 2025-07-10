# Simple Upload App

A clean and simple React application for uploading pictures and recording audio.

## 🚀 Quick Start

### Install Dependencies
```bash
cd Frontend
npm install
```

### Start the Development Server
```bash
npm run dev
```

The app will run on `http://localhost:5173`

## 📁 Project Structure

```
ustad/
├── Frontend/         # React application
│   ├── src/          # React source code
│   ├── package.json  # Frontend dependencies
│   ├── server.js     # Express server (moved from backend)
│   ├── backend-package.json  # Backend dependencies
│   ├── backend-README.md     # Backend documentation
│   └── README.md     # Frontend documentation
└── README.md         # This file
```

## 🎨 Features

### 📸 Image Upload
- Upload images from your device
- Real-time preview
- Supports all common image formats
- Responsive image display

### 🎤 Audio Recording
- Record audio using your microphone
- Built-in audio player for playback
- Automatic microphone permission handling
- Records in WAV format

### 🎯 User Experience
- Clean, modern interface
- Mobile-responsive design
- Smooth animations
- Intuitive controls

## 🛠️ How to Use

### Upload a Picture
1. Click the "Choose Image" button
2. Select an image file from your device
3. View the preview below

### Record Audio
1. Click "🎤 Start Recording"
2. Allow microphone access when prompted
3. Speak into your microphone
4. Click "⏹️ Stop Recording" when done
5. Use the audio player to listen to your recording

## 🔧 Development

### Frontend Development
```bash
cd Frontend
npm run dev
```

### Building for Production
```bash
cd Frontend
npm run build
npm run preview
```

## 📦 Technologies Used

### Frontend
- **React 18** - UI library
- **Vite** - Build tool and dev server
- **CSS3** - Modern styling with gradients
- **Web Audio API** - Audio recording
- **File API** - Image upload and preview

### Backend (Optional)
- **Node.js** - JavaScript runtime
- **Express.js** - Web framework (moved to Frontend folder)

## 🌐 Browser Compatibility

- Chrome 66+
- Firefox 60+
- Safari 14+
- Edge 79+

## 📝 Notes

- Audio recording requires HTTPS in production (or localhost for development)
- Microphone access must be granted by the user
- Images and audio are stored temporarily in the browser
- No server upload functionality (client-side only)

## 🐛 Troubleshooting

### Microphone Access Issues
- Make sure to allow microphone access when prompted
- Check browser settings for microphone permissions
- Try refreshing the page if permission is denied

### Image Upload Issues
- Ensure the file is an image format (JPEG, PNG, GIF, etc.)
- Check file size (large files may take time to load)

### Audio Recording Issues
- Ensure your microphone is working
- Check browser compatibility
- Try using Chrome or Firefox for best compatibility

---

**Happy Uploading! 🎉** 