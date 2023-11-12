# Hiring Task 1
## Password Generator App
### Tech
- Python - Language
- FastAPI - Webframework

## How to run Locally

cd into root directory and install requirements. Create virutal env if necessary.
```sh
pip install -r requirements.txt
```
Starting the App

Runs the app with uvicorn server
```sh
python app/main.py
```
## How to run as Docker Container
Install Docker Engine by following the official installation [Guide](https://www.mongodb.com/docs/manual/installation/).
cd into the root directory
Using docker compose to pull and build image and building container
```sh
docker-compose up --build
```
or start in detached mode without interactive shell
```sh
docker-compose up -d
```

If everthing went correct we will see following message at the end
```sh
$ Application startup complete.
```
## How to use the APIs:
FastAPI provides web interface to use the APIs, also can be used with other API testing tools and curl or dedicated frontend

User http://0.0.0.0:3000/docs/ to open interactive docs provide by FastAPI to try all apis.

##### Generate Password
http://0.0.0.0:3000/
###### Method: GET
Generates a password string of length 20 chars consisting of alphanumeric and special characters
Response Body
```sh
{
  "password": "ESr*QZ|zk.j{V;0rX]Q9"
}
```
Use query param 'max_length' to specify the length of the password, negative length will result error
http://0.0.0.0:3000/?max_length=6
###### Method: GET
```sh
{
  "password": "9y3?:v"
}
```

###### Additional Info:
"generate_alphanum_password" utility function can be further improved as per requirements 
to generate more versatile passwords.





