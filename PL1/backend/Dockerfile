#base image
FROM node

# Create app directory
WORKDIR /app

# Install app dependencies [From and To]
COPY . /app/

# Run app dependencies
RUN npm install

# Port Expose
EXPOSE 80

CMD ["node", "app.js"]