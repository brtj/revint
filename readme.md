# container build
docker build -t dotest:latest .
docker run -d -p 8080:8080 dotest
or 
cloudbuild.yaml

# flask development
export FLASK_APP="service"
export FLASK_ENV="development"
flask run

# db
sqlite3 database.db
.tables

# POST inputs
curl -X PUT -H "Content-Type: application/json" -d '{"dateOfBirth":"1990-01-08"}' localhost:5000/hello/Bartosz
