# GitHub AI

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
```

### Step 4: Install all dependencies
Install dependencies using
```
pip install --upgrade -r requirements.txt
```

### Step 5: Run Pathway server
Run the server using
```
python main.py
```

### Step 6: Run the UI interface
Run the UI using
```
streamlit run ui.py
```