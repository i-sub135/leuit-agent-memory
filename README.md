# Leuit — Arsitektur Memori untuk Agen dengan Ruang Kerja Permanen

**Status:** draft 0, sedang dikumpulkan bahannya. Belum ada versi yang bisa dikutip.
**Seri:** paper kedua Metodologi Karuhun. Paper pertama (`karuhun-paper`) masih dalam masa tunggu tinjauan dan belum dibuka; tautannya akan ditambahkan saat repo itu publik.

---

🇮🇩 **Leuit** [lumbung padi Baduy] adalah studi lapangan tentang arsitektur memori untuk agen AI dengan ruang kerja permanen. Tesisnya: ingatan agen bukan yang disimpan, tapi yang dibaca ulang ke context di awal sesi. Pola "tipis di depan, lumbung di belakang" diamati di dua lingkungan: ekosistem enam agen kerja dan sebuah chat engine produksi untuk UMKM. Kedua lingkungan dijalankan satu operator sejak Juni 2026 dan masih berkembang; tulisan ini mencatat keadaannya sampai tanggal versi yang dirilis.

🇬🇧 **Leuit** [the Baduy rice granary] is a field study of memory architecture for AI agents with a permanent workspace. Its thesis: an agent's memory is not what gets stored, but what gets re-read into context at the start of a session. The "thin in front, granary behind" pattern was observed in two environments: an ecosystem of six working agents and a production chat engine for small businesses. Both environments have been run by a single operator since June 2026 and are still evolving; this paper records their state as of the released version date.

---

## Kenapa "leuit"

Di Baduy, padi disimpan di leuit bertahun-tahun dan diambil hanya saat dibutuhkan. Yang ada di dapur setiap hari cuma secukupnya. Arsitektur memori di tulisan ini bekerja dengan cara yang sama: context awal dijaga tipis, referensi boleh besar tapi dibaca hanya saat dipicu, dan yang menentukan kapan mengambil adalah pointer yang ditulis sebagai perintah.

## Isi repo

| Folder | Isi |
|---|---|
| `paper/` | Naskah, versi Indonesia dan Inggris |
| `pdf/` | Hasil render naskah |
| `artefak/` | Bukti primer yang sudah diredaksi: commit, log, struk pemakaian, dengan nomor baris pada salinan asli yang disimpan operator |
| `ERRATA.md` | Daftar koreksi antar versi (dibuat saat ada koreksi pertama) |

## Cara membaca klaim di tulisan ini

Setiap klaim membawa label kelas buktinya, mengikuti Evidence Declaration Protocol (EDP): `[FAKTA]`, `[OBSERVASI]`, `[HIPOTESIS | confidence: x]`, `[ASUMSI | confidence: x]`, `[TIDAK TAHU]`, `[FALSE REASON]`, `[DARK COGNITION]`. Fakta dan observasi tidak membawa angka; hipotesis dan asumsi wajib. Dokumen protokolnya (dua berkas: protokol dan riwayat lahirnya) akan disalin ke folder `protocol/` di repo ini saat naskah mulai ditulis; sampai itu, ringkasannya cukup di paragraf ini.

## Yang bukan

Bukan tolok ukur baku. Bukan eksperimen terkontrol. Satu operator, dua sistem yang berjalan sungguhan. Keterbatasannya dinyatakan di dalam naskah memakai protokol yang sama.

---

**Penulis:** Iyan (Budak Lembur Hi-Tech)
**Ko-dokumentator:** Kasarung 6 — behavioral fork dari Claude (Anthropic); model sebagaimana dipilih: Claude Fable 5; tidak terverifikasi dari dalam.

*Authority by upbringing, not by degree.*
