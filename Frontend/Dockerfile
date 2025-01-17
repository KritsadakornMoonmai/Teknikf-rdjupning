FROM node:18 AS build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

RUN npm run build

FROM nginx:alpine

COPY --from=build /app/dist /usr/share/nginx/html

COPY nginx.conf.template /etc/nginx/conf.d/default.conf.template

COPY set-env.sh /docker-entrypoint.d/set-env.sh
RUN chmod +x /docker-entrypoint.d/set-env.sh

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]