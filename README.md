# Fast Note

API catatan sederhana untuk belajar struktur data Python melalui FastAPI.
Data disimpan di memori: semua catatan hilang saat server dimulai ulang.
Jalankan satu proses server agar semua request memakai penyimpanan yang sama.

## Menjalankan aplikasi

```powershell
uv sync
uv run fast-note
```

Buka http://127.0.0.1:8000/docs untuk mencoba endpoint melalui **Try it out**.
Untuk development dengan reload otomatis:

```powershell
uv run fastapi dev src/fast_note/app.py
```

## Struktur data yang dipelajari

| Struktur | Penggunaan di Fast Note | Operasi yang dilatih |
| --- | --- | --- |
| `dict` | Menyimpan catatan dengan ID sebagai key dan objek `Note` sebagai value | `notes[id] = note`, `.get(id)`, `del notes[id]` |
| `list` | Daftar catatan dan tag yang berurutan, bisa diubah | `list()`, list comprehension, `in`, `.append()`, `.remove()` |
| `tuple` | Snapshot dengan urutan `(id, title, tags)` | Membuat tuple, akses indeks, unpacking, sifat immutable |

Implementasi dan komentar belajar ada di `src/fast_note/app.py`.
`Note` adalah model Pydantic untuk validasi data; `notes` adalah dictionary Python
yang menyimpan objek-objek tersebut.

## Endpoint

| Method | Path | Latihan |
| --- | --- | --- |
| POST | `/notes` | Menambahkan catatan ke dict |
| GET | `/notes/{note_id}` | Mengambil catatan berdasarkan key |
| DELETE | `/notes/{note_id}` | Menghapus catatan dari dict |
| GET | `/notes` | Mengambil list catatan; filter opsional `?tag=python` |
| POST | `/notes/{note_id}/tags` | Menambahkan elemen ke list tag |
| DELETE | `/notes/{note_id}/tags/{tag}` | Menghapus elemen dari list tag |
| GET | `/notes/{note_id}/snapshot` | Membuat tuple dari catatan saat ini |

## Latihan lewat Swagger

1. Panggil `POST /notes` dengan body berikut:

   ```json
   {
     "title": "Belajar Python",
     "content": "Hari ini belajar struktur data lewat aplikasi catatan.",
     "tags": ["python", "belajar"]
   }
   ```

2. Gunakan `id` dari respons untuk `GET /notes/{note_id}`. Buat catatan kedua
   dan amati bahwa dict menyimpan keduanya dengan key berbeda.
3. Panggil `GET /notes`, kemudian coba filter `tag=python`. Hasilnya berupa list
   JSON; hasil filter kosong adalah `[]`.
4. Panggil `POST /notes/{note_id}/tags` dengan `{"tag": "fastapi"}`.
   Amati bahwa tag baru muncul di akhir list. Coba kirim lagi: API mengembalikan
   `409` karena tag sudah ada.
5. Panggil `DELETE /notes/{note_id}/tags/belajar`. Amati perubahan list tag.
6. Panggil `GET /notes/{note_id}/snapshot`. Jika ID catatan adalah `1`, hasilnya:

   ```json
   [1, "Belajar Python", ["python", "fastapi"]]
   ```

   Di server, nilai tersebut adalah tuple `(1, "Belajar Python", ("python", "fastapi"))`.
   JSON tidak memiliki tipe tuple, sehingga tuple dan list sama-sama dikirim
   sebagai array. Snapshot baru dibuat setiap request; endpoint ini tidak
   menyimpan riwayat catatan.

7. Hapus catatan lewat `DELETE /notes/{note_id}`, lalu ambil lagi. API akan
   mengembalikan `404` karena key tersebut sudah dihapus.

## Latihan langsung di Python

Jalankan `uv run python`, lalu coba:

```python
tags = ["python", "belajar"]
note = {"id": 1, "title": "Belajar Python", "tags": tags}
snapshot = (note["id"], note["title"], tuple(tags))

tags.append("fastapi")
print(note["tags"])  # ['python', 'belajar', 'fastapi']
print(snapshot[2])   # ('python', 'belajar') — salinan tuple tetap sama

note_id, title, saved_tags = snapshot  # tuple unpacking
print(note_id, title, saved_tags)

# Coba baris ini secara terpisah: akan menghasilkan TypeError.
# snapshot[1] = "Judul baru"
```

Tantangan lanjutan: tambahkan endpoint untuk mengganti judul catatan, mengambil
tag berdasarkan indeks, atau mengurutkan list catatan berdasarkan judul.

## Menjalankan pengujian

```powershell
uv run python -m unittest discover -s tests -v
```
