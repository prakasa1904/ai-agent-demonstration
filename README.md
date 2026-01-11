## Deskripsi

Repository untuk belajar membuat AI Agent sederhana menggunakan OpenAI API. Dengan AI Agent ini, kita bisa mengotomatisasi tugas-tugas tertentu dengan memanfaatkan kemampuan pemrosesan bahasa alami dari model OpenAI. Sehingga, kita dapat membuat sistem yang dapat berinteraksi, mengambil keputusan, dan menyelesaikan tugas-tugas spesifik secara otomatis. Dengan diintegrasikan dengan tools tertentu, AI Agent ini dapat memperluas fungsionalitasnya untuk memenuhi kebutuhan pengguna.

### Tujuan
Tujuan dari repository ini adalah untuk memberikan contoh praktis tentang bagaimana membangun AI Agent yang dapat melakukan tugas-tugas tertentu, seperti memantau penggunaan CPU server, dengan menggunakan OpenAI API. Dengan mengikuti contoh ini, diharapkan pembaca dapat memahami konsep dasar pembuatan AI Agent dan mengaplikasikannya dalam proyek mereka sendiri.

### Penggunaan

1. Clone repository ini ke lokal mesin Anda.
   ```bash
   git clone https://github.com/prakasa1904/ai-agent-demonstration.git
   ```
2. Masuk ke direktori proyek.
   ```bash
   cd ai-agent-demonstration
   ```
3. Buat virtual environment.
   ```bash
   make init
   ```
4. Copy file `.env.example` menjadi `.env` dan isi variabel lingkungan yang diperlukan, seperti `OPENAI_API_KEY`.
   ```bash
   cp .env.example .env
   ```
5. Jalankan AI Agent.
   ```bash
   make run
   ```

### Referensi
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Python Client Library](https://github.com/openai/openai-python)
- [Function Call](https://platform.openai.com/docs/guides/function-calling)