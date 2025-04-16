FROM node:lts AS build
 
 WORKDIR /app
 
 COPY package.json /app/package.json
 COPY package-lock.json /app/package-lock.json
 
 RUN npm install
 
 COPY . .
 
 RUN npm run build
 
 FROM nginx:latest
 
 COPY --from=build /app/dist /usr/share/nginx/html