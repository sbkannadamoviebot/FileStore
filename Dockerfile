FROM node:18
WORKDIR /app

# ಮೊದಲು ಎಲ್ಲವನ್ನೂ ಕಾಪಿ ಮಾಡು
COPY . .

# ಲಿಸ್ಟ್ ಮಾಡಿ ನೋಡು (ಬಿಲ್ಡ್ ಲೋಗ್‌ನಲ್ಲಿ ಫೈಲ್ಸ್ ಕಾಣಿಸುತ್ತವೆ)
RUN ls -la

# ಈಗ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡು
RUN npm install

CMD ["node", "index.js"]

