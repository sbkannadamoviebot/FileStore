# 1. ಪೈಥಾನ್ ಇಮೇಜ್ ಬಳಸು
FROM python:3.10-slim

# 2. ಕೆಲಸ ಮಾಡುವ ಫೋಲ್ಡರ್ ಸೆಟ್ ಮಾಡು
WORKDIR /app

# 3. ಸಿಸ್ಟಮ್ ಅಪ್‌ಡೇಟ್ ಮಾಡು
RUN apt-get update && apt-get install -y git

# 4. ಎಲ್ಲಾ ಫೈಲ್‌ಗಳನ್ನು ಕಾಪಿ ಮಾಡು
COPY . .

# 5. ಪೈಥಾನ್ ಲೈಬ್ರರಿಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡು
RUN pip install --no-cache-dir -r requirements.txt

# 6. ನಿನ್ನ ಬಾಟ್ ರನ್ ಮಾಡಲು ಕಮಾಂಡ್ (main.py ಅಥವಾ bot.py ಯಾವುದು ಮುಖ್ಯವೋ ಅದನ್ನು ಹಾಕು)
CMD ["python3", "main.py"]
