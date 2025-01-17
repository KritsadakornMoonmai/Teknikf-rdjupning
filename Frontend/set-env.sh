#!/bin/sh

# Replace placeholder in nginx.conf.template with the environment variable
if [ -z "$VITE_API_URL" ]; then
    echo "Error: VITE_API_URL environment variable is not set."
    exit 1
fi

envsubst '${VITE_API_URL}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

exec "$@"
