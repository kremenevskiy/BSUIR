## e-shop - web internet online shop to find and order apple devices

## Docker hub image: https://hub.docker.com/repository/docker/kremenevskiy/eshop-img



## How to run:
### - Production Mode
#### 1. Download file: docker-compose-prod.yml, .env.dev
#### 2. Run it terminal:
```angular2html
wget https://raw.githubusercontent.com/kremenevskiy/BSUIR/master/Term_4-python/e-shop/docker-compose-prod.yml
wget https://raw.githubusercontent.com/kremenevskiy/BSUIR/master/Term_4-python/e-shop/.env.dev
docker-compose -f docker-compose-prod.yml up
```
#### 3. Visit host in a browser: 0.0.0.0:8000

### - Dev Mode
#### 1. Clone current git directory
#### 2. Run docker compose
```angular2html
git clone git@github.com:kremenevskiy/BSUIR.git
cd BSUIR/Term_4-python/e-shop
docker-compose up --build
```
#### 3. Visit host in a browser: 0.0.0.0:8000

## Functionality:

- view different products
- chose product want to buy
- look at product details (specifications)
- put product to the cart
- put other products to the cart
- make order of chosen products
- see made orders in logged user profile
- see details about made orders
- login
- registration
- make order for unlogged
- add your products from admin account
- change all created products from admin
- CRUD operations







