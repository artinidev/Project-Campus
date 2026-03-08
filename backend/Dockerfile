# Use LTS version of Node.js
FROM node:18-alpine

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json if available
# This allows Docker to cache the npm install step if only source files change
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy backend source code into the container
COPY . .

# Expose port 5000 as configured in the Node server
EXPOSE 5000

# Command to run the backend server
CMD ["npm", "start"]
