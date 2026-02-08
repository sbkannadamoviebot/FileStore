FROM node:18

WORKDIR /app

# ಮೊದಲು ಇವೆರಡನ್ನು ಮಾತ್ರ ಕಾಪಿ ಮಾಡು
COPY package*.json ./

# ಈಗ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡು
RUN npm install

# ಆಮೇಲೆ ಬಾಕಿ ಉಳಿದ ಎಲ್ಲಾ ಫೈಲ್‌ಗಳನ್ನು ಕಾಪಿ ಮಾಡು
COPY . .

CMD ["node", "index.js"]
