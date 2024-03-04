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
<img width="1428" alt="Capture d’écran 2024-03-04 à 05 41 22" src="https://github.com/CallMeNachos/automated-pipeline-airbnb/assets/60932767/cb2e5b3f-e6b8-4196-a486-70dedbdb57cf">
5. Double-click on the user you have created (here ```devuser```) then create an access key.
<img width="1426" alt="Capture d’écran 2024-03-04 à 05 41 50" src="https://github.com/CallMeNachos/automated-pipeline-airbnb/assets/60932767/2ae3ff56-b62c-4a3b-8329-6a9c2450847f">

6. Download your credentials and store it in the working directory as ```user_credentials.json```
7. You are ready to go !
