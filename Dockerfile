# Use the lightweight Nginx Alpine image
FROM nginx:alpine

# Remove default Nginx website
RUN rm -rf /usr/share/nginx/html/*

# Copy custom Nginx configuration to listen on port 3000
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy all static website files to the Nginx html directory
COPY . /usr/share/nginx/html

# Ensure Nginx serves assets from the correct nested directories (html, css, js, assets)
# The previous step natively copies everything in the root, including assets/

# Expose port 3000 (which matches nginx.conf)
EXPOSE 3000

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]
