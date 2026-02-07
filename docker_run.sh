# /bin/bash

docker run -it --rm \
    -e POSTGRES_USER='sensitive' \
    -e POSTGRES_PASSWORD='sensitive' \
    -e POSTGRES_DB='taxis' \
    -v taxis_data:/var/lib/postgresql \
    -p 5432:5432 \
    postgres:18
