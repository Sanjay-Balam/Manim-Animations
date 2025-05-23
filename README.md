# Manimations: Generate Math 2D-Animation Videos with single prompt

This project allows you to generate advanced [Manim](https://www.manim.community/) animation scripts using natural language prompts, powered by the Gemini LLM API.

## Features

- **Prompt-to-Manim:** Enter a math animation prompt, get a ready-to-run Manim script.
- **Backend API:** Flask server that connects to Gemini LLM and returns Python code.
- **Secure:** API keys and endpoints are managed via `.env` (never committed to git).
- **Easy Rendering:** Save and render generated scripts with Manim.

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/Sanjay-Balam/Manim-Animations.git
cd Cursor-2D-Animation-project/manimations
```

### 2. Set up the environment

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Add your `.env` file

Create a `.env` file in the `manimations` directory:

## Future Implementation

- **One-Prompt, Full Video Generation:**  
  The goal is to allow users to generate complete, high-quality 2D animated math videos from a single natural language prompt. The system will interpret the prompt, generate all necessary Manim scripts, and stitch together a full educational video automatically.

- **Clean and Intuitive UI:**  
  A user-friendly web interface will be developed, enabling anyone to enter a math concept or lesson as a prompt and instantly receive a polished animated video—no coding required.

- **Automatic Rendering and Download:**  
  Users will be able to preview, render, and download their videos directly from the UI.

- **Extensible and Modular:**  
  The platform will support additional animation types, voiceover integration, and more, making it a powerful tool for educators, students, and content creators.


## References

- [Manim Community](https://www.manim.community/)
- [Google Gemini API](https://aistudio.google.com/app/apikey)

## Output of the above code

![Cosine Wave Animation](media/videos/generated_manim/480p15/CosineWave.gif)
