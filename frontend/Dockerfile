FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Expose port for development
EXPOSE 3000

# Start Vite server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]
