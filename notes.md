## Step 1
```
git clone --no-checkout https://github.com/HaileyTQuach/Smart-Nutritional-App.git NourishBot
cd NourishBot
git checkout 1-start
```

## Step 2
```
python3.11 -m venv venv
source venv/bin/activate # activate venv
pip install -r requirements.txt
```
This command installs crewai, which orchestrates AI agents for task management, and gradio, which builds the user-friendly web interface. Additionally, ibm_watsonx_ai is crucial for ingredient detection and nutritional analysis, while langchain and fastapi handle natural language generation and asynchronous operations, respectively. Other key packages include pydantic for data validation, pillow for image processing, and requests for API communication. Together, these packages enable the app's core functionalities, from AI-driven workflows to user interaction.

## Step 3
create multimodal_queries.py file