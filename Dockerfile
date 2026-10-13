FROM node:24-bookworm-slim

ENV NODE_ENV=production \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:${PATH}"

WORKDIR /app

RUN apt-get -o Acquire::Retries=3 update \
    && apt-get install -y --no-install-recommends \
        g++ \
        make \
        python3 \
        python3-venv \
    && rm -rf /var/lib/apt/lists/*

COPY package.json package-lock.json ./
RUN npm ci --omit=dev

COPY requirements.txt ./
RUN python3 -m venv /opt/venv \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 10000

CMD ["npm", "start"]
