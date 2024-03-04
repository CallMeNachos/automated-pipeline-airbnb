# automated-pipeline-airbnb

## Installation

#### Load python packages :
```pip install -r requirements.txt```

#### Run MinIO:
1. Install Docker in your local machine
https://docs.docker.com/get-docker/

2. Run command ```docker compose up```
3. Open MinIO through http://127.0.0.1:9001/ or http://127.0.0.1:9000/
4. Create a user under Administartor/Identity/Users    
![Capture d’écran 2024-03-04 à 05.29.48.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2F1h%2Fxtxjb6tj51s8_v5wnbf9jvyh0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_OK2Y5F%2FCapture%20d%E2%80%99%C3%A9cran%202024-03-04%20%C3%A0%2005.29.48.png)
5. Double-click on the user you have created (here ```devuser```) then create an access key.
![Capture d’écran 2024-03-04 à 05.29.00.png](..%2F..%2F..%2F..%2Fvar%2Ffolders%2F1h%2Fxtxjb6tj51s8_v5wnbf9jvyh0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_DSklXS%2FCapture%20d%E2%80%99%C3%A9cran%202024-03-04%20%C3%A0%2005.29.00.png)
6. Download your credentials and store it in the working directory as ```user_credentials.json```
7. You are ready to go !