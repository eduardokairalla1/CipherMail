# 🔐 CipherMail

A secure messaging CLI application built with Python and MongoDB featuring end-to-end encryption.

**Developed by Eduardo Kairalla**

---

## ✨ Features

### 🔒 Security
- **End-to-End Encryption** - Fernet symmetric encryption for all messages
- **Password Hashing** - SHA256 for secure password storage
- **Zero-Knowledge** - Only users with encryption key can read messages
- **Environment Variables** - Sensitive configuration stored in .env

### 🍃 MongoDB Integration
- **NoSQL Database** - MongoDB for flexible data storage
- **PyMongo Driver** - Seamless interaction with MongoDB
- **Collections** - Separate collections for users and messages

---

## 📦 Requirements

- **Python 3.12.3+**
- **Poetry** (dependency management)
- **MongoDB** (database)

---

## 🐋 Running with Docker

### Pull the Project Docker Image

```bash
docker pull edu3983/ciphermail:0.1.0
```

### Running the Container
> Make sure your MongoDB instance or MongoDB Atlas cluster is running and accessible.

```bash
docker run -it --rm -e MONGODB_URI="<your_mongodb_uri>" edu3983/ciphermail:0.1.0
```

### Docker Parameters

- `-it` - Interactive mode (required for CLI input)
- `--rm` - Automatically remove container when it exits
- `-e MONGODB_URI` - Pass MongoDB connection string as environment variable

---

## 🚀 Development Installation

### 1. Pre-requisites: Python and Poetry

**Check Python version:**
```bash
python --version  # Should be 3.12.3 or higher
```

**Install Poetry:**
> See [Poetry Installation Guide](https://python-poetry.org/docs/#installation) for details.

### 2. Clone/Navigate to Project

```bash
git clone https://github.com/eduardokairalla1/ciphermail.git
```

```bash
cd ciphermail/
```

### 4. Install Dependencies

```bash
poetry install
```

### 5. Configure Environment

```bash
# Copy example environment file
cp .env.example .env
```
> Edit `.env` to use your environment variables:

---

## 🎮 Usage

### Starting the Application

**Option 1: Using the run script (Recommended)**
```bash
./scripts/run
```

**Option 2: Using Poetry**
```bash
poetry run python -m ciphermail.main
```

---

## 📖 How It Works

### Login/Register in system
#### Register a New User

1. Start the application
2. Choose option `2` (Register)
3. Enter a username
4. Enter a password
5. Account created successfully!

#### Login

1. Choose option `1` (Login)
2. Enter your username
3. Enter your password
4. Access granted!

### After Login in system

#### Send Encrypted Message

1. Choose option `1` (Send message)
2. Enter recipient's @username (e.g., `@alice` or just `alice`)
3. Type your message
4. Enter an encryption key (hidden input) - **Remember this key!**
5. Message encrypted and sent to MongoDB

#### Read Messages

1. Choose option `2` (Read messages)
2. See list of unread messages with sender and timestamp
3. Select message number (or `0` to cancel)
4. Enter the decryption key
5. If key is correct, message is displayed and marked as read

### 🔐 Important Security Note

**The encryption key is NOT stored!** You must share it with your recipient through a secure channel (phone call, Signal, WhatsApp, etc.). Without the correct key, messages cannot be decrypted.

---

## 📂 Project Structure

```
ciphermail/
├── ciphermail/
│   ├── main.py                      # Entry point
│   ├── app.py                       # Application entry
│   ├── interface/
│   │   ├── cli.py                   # Main CLI logic
│   │   └── ui.py                    # UI components (ASCII art, colors)
│   ├── config/
│   │   └── database.py              # MongoDB connection manager
│   ├── models/
│   │   ├── user.py                  # User model
│   │   └── message.py               # Message model
│   └── services/
│       ├── auth.py                  # Authentication service
│       ├── messaging.py             # Messaging service
│       └── encryption.py            # Encryption/decryption
├── scripts/
│   ├── run                          # Convenience run script
│   └── build                        # Docker build script
├── .env                             # Environment variables
├── .env.example                     # Environment template
├── .gitignore                       # Git ignore rules
├── pyproject.toml                   # Poetry configuration
└── README.md                        # This file
```

### Code Organization

- **`interface/`** - User interface and interaction
- **`config/`** - Application configurations
- **`models/`** - Data custom models (User, Message)
- **`services/`** - Business logic (auth, messaging, encryption)

---

## 🔒 Security Features

### Password Security
- **SHA256 Hashing** - Passwords are hashed before storage
- **No Plain Text** - Passwords never stored in plain text
- **Hidden Input** - Password input invisible using `getpass`

### Message Encryption
- **Fernet Encryption** - Symmetric encryption (AES 128-bit)
- **Unique Keys** - Each message can use different encryption key
- **No Key Storage** - Encryption keys never stored in database
- **End-to-End** - Messages encrypted before saving to MongoDB

### Database Security
- **Environment Variables** - Connection strings in .env (not in code)
- **Encrypted Storage** - All messages stored encrypted
- **User Isolation** - Users can only read their own messages

---

## 🛠️ Technologies Used

| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Programming language | 3.12.3+ |
| **MongoDB** | NoSQL database | Atlas or self-hosted (Docker) |

---

## 💡 Tips

1. **Share encryption keys securely** - Use Signal, WhatsApp, or phone call
2. **Use strong passwords** - Mix letters, numbers, and symbols
3. **Different keys for different messages** - Increase security
4. **Remember your keys** - No key recovery available
5. **Keep MongoDB running** - Application needs database connection

---

## 🤝 Contributing

This is an educational project. Feel free to:
- Report bugs
- Suggest improvements
- Fork and experiment or add features/improvements
- Learn from the code
- Share with others

---

**Stay Secure! 🔐**
