# English Learning App - Development Tasks

## Core MVP Features

### Text Input & Processing
- [x] Set up Flask project structure with proper blueprints
- [ ] Implement image upload endpoint with file validation (jpg, png, pdf)
- [ ] Use local Gemma model for OCR text extraction from images
- [ ] Create text input form as alternative to image upload
- [ ] Add text preprocessing (cleaning, sentence segmentation)

### Text Display & Audio Playback
- [ ] Build frontend page to display extracted text with word-level spans
- [ ] Set up local English text-to-speech (pyttsx3 or similar)
- [ ] Implement word highlighting system that syncs with audio playback
- [ ] Add audio controls (play, pause, speed adjustment)
- [ ] Handle text chunking for longer passages

### Speech Recording & Analysis
- [ ] Implement local audio recording (pyaudio or sounddevice)
- [ ] Set up local speech-to-text processing (Whisper local deployment)
- [ ] Build pronunciation comparison logic using Gemma model
- [ ] Create visual feedback system (correct/incorrect word highlighting)
- [ ] Design word-level analysis with extensible architecture for phoneme-level
- [ ] Add audio playback of user's recording for review

### Backend Infrastructure
- [ ] Set up Ollama integration for local Gemma model - in-progress (EZ)
- [ ] Configure model prompts for OCR and pronunciation scoring tasks
- [ ] Create database schema for user sessions and text storage
- [ ] Implement file storage system for uploaded images/audio
- [ ] Add error handling and logging throughout

### Frontend Polish
- [ ] Create responsive UI with clean text reading interface
- [ ] Add progress tracking for reading sessions
- [ ] Implement basic user feedback collection
- [ ] Add loading states and error messages

## Stretch Goal: Farsi Integration

### Model Setup & Training
- [ ] Fine-tune Gemma 3n on Farsi language dataset
- [ ] Test bilingual capabilities (English-Farsi translation)
- [ ] Optimize model for conversational Q&A about English text
- [ ] Set up model switching logic in Ollama

### Bilingual Interface
- [ ] Add language toggle (English/Farsi) to UI
- [ ] Implement Farsi text rendering (right-to-left support)
- [ ] Create Farsi input methods for questions
- [ ] Add Farsi audio output using ElevenLabs TTS

### Q&A Functionality
- [ ] Build question input system with Farsi support
- [ ] Implement context-aware responses using fine-tuned model
- [ ] Add question templates ("What does X mean?", "How do you use X?")
- [ ] Create conversation history for each text session

### Enhanced Features
- [ ] Word/phrase explanation system in Farsi
- [ ] Cultural context explanations for English idioms
- [ ] Grammar rule explanations in Farsi
- [ ] Difficulty assessment of English text for Farsi speakers