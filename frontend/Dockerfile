# Use a Node.js image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
RUN npm install

# Copy the frontend code
COPY . .

# Expose port for frontend (React default is 3000)
EXPOSE 3000

# Start frontend
CMD ["npm", "start"]
