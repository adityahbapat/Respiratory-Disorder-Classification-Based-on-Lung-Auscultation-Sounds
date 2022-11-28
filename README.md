### Respiratory Disorder Classification Based on Lung Auscultation sounds

Respiratory sounds are important indicators of respiratory health and respiratory disorders. The sound emitted when a person 
breathes is directly related to air movement, changes within lung tissue and the position of secretions within the lung. 
A wheezing sound, for example, is a common sign that a patient has an obstructive airway disease like asthma or chronic 
obstructive pulmonary disease (COPD). These sounds can be recorded using digital stethoscopes and other recording techniques.
This digital data opens up the possibility of using machine learning to automatically diagnose respiratory disorders like asthma, 
pneumonia and bronchiolitis, to name a few.

### Dataset Link
Respiratory Sound Database: https://www.kaggle.com/vbookshelf/respiratory-sound-database

### Requirements:
To get started with the project make sure you have python installed.

### Folder Setup:
Here is a detailed folder setup to help you get started

respiratory_disorder_classification (Main Project Folder)
- Respiratory_Sound_Database (sub-folder)
- - audio_and_txt_files , etc
- venv (virtual env sub folder)
- backend (flask app)
- processed_audio_files
- .gitignore
- demographic_info.txt
- README.md
- respiratory_disorder_classification.ipynb
- training
- - train.csv
- validation
- - val.csv 


creating a virtual env:
1. `python -m venv C:\Users\"Aditya Bapat"\Desktop\project\respiratory_disorder_classification\venv` (project folder path\venv)
2. give permission for windows user: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted`
3. To activate: `.\venv\Scripts\activate.ps1` 
4. Install the req packages: eg `pip install tensorflow` (without venv do: pip install tensorflow --user)

GPU support for tensorflow: https://www.youtube.com/watch?v=hHWkvEcDBO0

### Flask App
Flask app can be found in the backend folder
To run the app:
`python app.py`