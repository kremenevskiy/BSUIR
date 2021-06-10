## e-shop - web internet online shop to find and order apple devices

## Docker hub image: https://hub.docker.com/repository/docker/kremenevskiy/eshop-img



## How to run:
### - Production Mode
#### 1. Download file: docker-compose-prod.yml
#### 2. Run it terminal:
```angular2html
wget https://raw.githubusercontent.com/kremenevskiy/BSUIR/master/Term_4-python/e-shop/docker-compose-prod.yml
docker-compose -f docker-compose-prod.yml up --build
```
#### 3. Visit host in a browser: localhost:8000

### - Dev Mode
#### 1. Clone current git directory
#### 2. Run docker compose
```angular2html
git clone git@github.com:kremenevskiy/BSUIR.git
cd BSUIR/Term_4-python/e-shop
docker-compose up --build
```
#### 3. Visit host in a browser: localhost:8000






