# Application Server

This project involves the deployment of our AirBnB clone application. In this project, I configured Nginx on provided web servers to serve a WSGI Flask app running through Gunicorn. Additionally, I set up an Upstart script to ensure the application remains running across server reboots.

## Tasks

### 0. Set Up Development with Python

In this task, I configured the file `web_flask/0-hello_route.py` from my [AirBnB_clone_v2](https://github.com/glovic/AirBnB_clone_v2) repository to serve content on the route `/airbnb-onepage/`, running on port `5000`.

### 1. Set Up Production with Gunicorn

This task involved setting up a production environment by installing and configuring Gunicorn to serve the same file from task 0.

### 2. Serve a Page with Nginx

**File:** [2-app_server-nginx_config](./2-app_server-nginx_config)

This task involved creating an Nginx configuration file to proxy requests on the route `/airbnb-onepage/` to the Gunicorn app running on port `5000`.

### 3. Add a Route with Query Parameters

**File:** [3-app_server-nginx_config](./3-app_server-nginx_config)

In this task, I created an Nginx configuration file to proxy requests on the route `/airbnb-dynamic/number_odd_or_even/<int:num>` to the Gunicorn app running on port `5000`.

### 4. Let's Do This for Your API

In this task, I configured the API from my [AirBnB_clone_v3](https://github.com/glovic/AirBnB_clone_v3) to run on Gunicorn.

**File:** [4-app_server-nginx_config](./4-app_server-nginx_config)

I created an Nginx configuration file to proxy requests to the AirBnB API, which is served by the corresponding Gunicorn app.

### 5. Serve Your AirBnB Clone

In this task, I configured the complete AirBnB app from [AirBnB_clone_v4](https://github.com/GRACE8129/AirBnB_clone_v4) to run on Gunicorn and be served through Nginx.

**File:** [5-app_server-nginx_config](./5-app_server-nginx_config)

I configured Nginx to serve the static assets from `web_dynamic/static/` on the Gunicorn AirBnB app.

### 6. Deploy It

**File:** [gunicorn.conf](./gunicorn.conf)

This task involved creating a configuration file for an Upstart script to start a Gunicorn process bound to port `5003` that serves the content from task 5. The Gunicorn process spawns three worker processes and logs errors to `/tmp/airbnb-error.log` and access logs to `/tmp/airbnb-access.log`.

### 7. No Service Interruption

**File:** [4-reload_gunicorn_no_downtime](./4-reload_gunicorn_no_downtime)

This task involved creating a Bash script to gracefully reload Gunicorn without causing service interruptions.
