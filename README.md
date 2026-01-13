# 🧠 AI Sentiment Analysis & Text Summarizer Web App

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-green)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.25-orange)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A full-stack web application that allows users to perform **sentiment analysis** and **text summarization** on any text input. Built with **FastAPI** for the backend and **Streamlit** (or React) for the frontend, powered by **Hugging Face Transformers** models.

---

## Table of Contents

- [Features](#features)  
- [Demo](#demo)  
- [Installation](#installation)  
- [Running the Application](#running-the-application)  
- [API Endpoints](#api-endpoints)  
- [Usage Example](#usage-example)  
- [Technologies Used](#technologies-used)  
- [License](#license)  

---

## Features

- **Sentiment Analysis:** Classifies text as positive, negative, or neutral using a BERT-based model.  
- **Text Summarization:** Generates concise summaries using T5 or BART models.  
- **Secure Authentication:** JWT-based login system.  
- **File Upload Support:** Optionally analyze text from uploaded documents.  
- **Easy Deployment:** Runs locally or on a Linux server / Heroku.  
- **Performance Monitoring:** Tracks response time and model accuracy.  

---

## Demo

Example interface: login, enter text, and view sentiment & summary.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/ai-sentiment-summarizer.git
cd ai-sentiment-summarizer
