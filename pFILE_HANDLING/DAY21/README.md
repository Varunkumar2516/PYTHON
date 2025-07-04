#  Python File Handling Guide (Text & Binary Files)

This guide covers the core theoretical concepts of handling files in Python — from text-based operations to binary file processing. It's designed for learners, developers, and contributors who want a clear understanding of file I/O in Python.

---

##  Text Files

Text files store human-readable characters using encoding (like UTF-8). Python provides multiple ways to read, write, and manage these files efficiently.

---

###  File Modes

| Mode | Meaning                              |
|------|---------------------------------------|
| `r`  | Read (default)                        |
| `w`  | Write (overwrite if exists)           |
| `a`  | Append (preserve contents)            |
| `x`  | Create (fails if file exists)         |

> All of these modes can be combined with `b` (e.g., `rb`, `wb`) for binary operations.

---

###  Important Text File Methods

- `read(size)` – Reads specified number of characters.
- `readline()` – Reads a single line.
- `readlines()` – Reads all lines into a list.
- `write(string)` – Writes a string to the file.
- `writelines(iterable)` – Writes a list of strings.
- `seek(offset)` – Moves the cursor to a specific byte.
- `tell()` – Returns current cursor position.

---

###  Text File Efficiency Tips

- Use `with open(...)` to automatically close files.
- Use `for line in file:` to read large files line-by-line efficiently.
- Avoid `read()` or `readlines()` on very large files — they load everything into memory.
- Use `seek()` and `tell()` to manage custom reading positions.

---

###  Special Modes

- `'w'` and `'a'` both create a file if it doesn't exist.
- `'x'` is used to **safely create a new file** only if it doesn’t already exist, raising a `FileExistsError` otherwise.

---

##  Binary Files

Binary files contain non-text data such as images, audio, video, and executables. These are not human-readable and must be processed using binary file modes.

---

###  Binary File Modes

| Mode | Description                      |
|------|----------------------------------|
| `rb` | Read in binary mode              |
| `wb` | Write in binary mode             |
| `ab` | Append in binary mode            |
| `xb` | Exclusive binary file creation   |

---

###  Binary vs Text Mode

- Text mode handles newline characters and encoding.
- Binary mode reads/writes raw bytes — no encoding/decoding.
- Always use binary mode for non-text files to avoid corruption.

---

###  When to Use Binary Files

- Copying or modifying media (images, audio)
- Working with serialized data (e.g., `pickle`)
- Processing large raw datasets
- Byte-level manipulation (e.g., file headers)

---

###  Key Points to Remember

- Reading/writing in chunks improves performance with large files.
- Binary files should not be opened in text mode — it leads to data loss or corruption.
- Use `with open("file", "rb")` to read and `with open("file", "wb")` to write safely.

---

##  Best Practices Summary

- Always use `with` statement to manage files.
- Prefer iterating over files rather than loading all data at once.
- Use `'x'` mode to safely check for file existence before creation.
- For large binary or text files, read/write in **chunks** to avoid memory overload.

---

Happy Coding! 
