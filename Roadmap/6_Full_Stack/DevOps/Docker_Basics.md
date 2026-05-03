# **Full Stack: Docker Basics**

"It works on my machine!" 
Docker solves this problem by packaging your app and its environment into a **Container**.

---

## **1. What is a Container?**
A container is a lightweight, standalone package that includes everything needed to run an application: code, runtime, system tools, and libraries.

---

## **2. Images vs. Containers**
- **Image:** A read-only template (the "Blueprint").
- **Container:** A running instance of an image (the "House").

---

## **3. The Dockerfile**
A script that contains instructions on how to build a Docker Image.

```dockerfile
# Use Node.js as the base
FROM node:18

# Set the working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the code
COPY . .

# Start the app
CMD ["npm", "start"]
```

---

## **4. Docker Compose**
Used to run multi-container apps (e.g., your App + a Database) with a single command: `docker-compose up`.

---

## **🎯 Exercise for You:**
1. Install Docker Desktop.
2. Create a simple "Hello World" Node.js app.
3. Write a Dockerfile to containerize it.
4. Build the image and run it on port 3000.
