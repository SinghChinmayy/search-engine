# Searchy - NLP Search Engine Pipeline

A modular NLP pipeline designed for document ingestion, processing, and representation.

## 🏗️ Pipeline Architecture

The pipeline follows a sequential flow from raw data to processed tokens:

**Sources** → **Ingestion** (Loaders) → **Preprocessing** (Normalization & Tokenization) → **Representation** (Coming Soon) → **Output**

---

## 📥 Document Ingestion

The ingestion layer handles fetching and reading documents from various sources.

### 1) Supported Data Sources
- [x] `.txt` files
- [ ] wikipedia dump to build search engine on top of it
### 2) Loaders (`pipeline/loaders/`)
- **TxtLoader**: Efficiently reads text files using UTF-8 encoding. It provides a standard `load()` interface for the rest of the pipeline.

---

## ⚙️ Preprocessing (`pipeline/processor/`)

This stage cleans and structures the raw text into a format suitable for downstream tasks.

### 1) Text Normalization
- **Unicode Normalization**: Uses `NFKC` format for maximum compatibility across different character sets.
- **Line Ending Normalization**: Standardizes Windows (`\r\n`) and old macOS (`\r`) line endings to Linux/Standard POSIX format (`\n`).
- **Case Folding**: Converts all text to lowercase to ensure case-insensitive processing.
- **Stripping**: Removes leading and trailing whitespace.
- *Upcoming: Punctuation handling and advanced cleaning.*
- stemming and lematization is yet ot implement
- common words removal is also yet to implement

### 2) Tokenization
- we had option to use basic .split() and regex to use for tokenization 
- Uses a robust regex-based tokenizer (`\b\w+(?:[-']\w+)*\b`) that respects:
    - Standard alphanumeric words.
    - Hyphenated words (e.g., `semi-structured`).
    - Contractions/Apostrophes (e.g., `don't`).

- build a posting list for tokens

future advanced:
    build a advanced inverted index posting list 
---



# inverse indexing

- basi implenmentation is being done 

docs is tokenized and unique id is assigned to docs
    the id maps to the origginal docs and 
