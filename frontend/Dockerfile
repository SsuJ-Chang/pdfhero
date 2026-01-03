FROM node:20-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

# Vite default port
EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
