# GitHub AI

## Demo
https://github.com/Arjun-G-04/github-ai/assets/34741958/c299e132-5bbb-4257-930d-e1dbce700a2c

## Presentation
[Presentation](https://www.canva.com/design/DAFymXb9jvk/-GpQsNQG1r7HMl9YwZlMyw/view?utm_content=DAFymXb9jvk&utm_campaign=designshare&utm_medium=link&utm_source=editor)

## Setup

### Pre-requisites
1. Python 3.10 or above
2. pip package manager
3. OpenAI API Key
4. Public GitHub repo link

### Step 1: Clone this repo
Clone this repo using
```
git clone https://github.com/Arjun-G-04/github-ai
```

And move to the folder using
```
cd github-ai
```

### Step 2: Clone the repo that you want to be AI accessible
Follow step 1 with the different URL

### Step 3: Create .env file
Create `.env` file with the following contents
```
OPENAI_API_TOKEN={OPENAI_API_KEY}
HOST=0.0.0.0
PORT=8080
EMBEDDER_LOCATOR=text-embedding-ada-002
EMBEDDING_DIMENSION=1536
MODEL_LOCATOR=gpt-3.5-turbo
MAX_TOKENS=400
TEMPERATURE=0.0
REPO_NAME={REPO_NAME}
REPO_OWNER={REPO_OWNER}
GITHUB_API_KEY={GITHUB_API_KEY}
```

### Step 4: Install all dependencies
Install dependencies using
```
pip install --upgrade -r requirements.txt
```

### Step 5: Run all the necessary servers and pipelines
Have 4 terminals, and in each terminal run each of the following commands
```
python backend.py
```
```
python pipeline.py
```
```
python main.py
```
```
streamlit run ui.py
```

### Step 6: Use the UI interface to start using the tool!
Ask away the questions related to repo or anything else that you want!

## Made with ❤️ by __balloon animals__ during TransfiNITTe 2023 at NITT 
