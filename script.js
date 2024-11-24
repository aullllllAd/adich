
function downloadFile() {

    const imageUrl = "img/scanme.jpg"; // Path ke file gambar

    // Buat elemen <a> secara dinamis
    const link = document.createElement('a');
    link.href = imageUrl; // URL file
    link.download = "scanme.jpg"; // Nama file saat diunduh
    document.body.appendChild(link); // Tambahkan ke DOM sementara
    link.click(); // Trigger unduhan
    document.body.removeChild(link); // Hapus elemen setelah unduhan
  }



// Mulai dengan halaman pertama yang aktif
document.getElementById('page1').classList.add('active');

let currentSlide = 0;

function moveSlide() {
    const slides = document.querySelectorAll('.carousel-item');
    const totalSlides = slides.length;

    // Menghapus kelas active dari gambar yang sedang tampil
    slides[currentSlide].classList.remove('active');

    // Mengubah indeks slide saat ini
    currentSlide = (currentSlide + 1) % totalSlides; // Berpindah ke slide berikutnya (looping)

    // Menambahkan kelas active pada gambar yang baru
    slides[currentSlide].classList.add('active');
}

// Mengatur interval agar gambar bergeser setiap 3 detik
setInterval(moveSlide, 4000); // 3000 ms = 3 detik
function playMusic() {
  const audio = document.getElementById('backgroundMusic');
  if (audio.paused) {
      audio.play(); // Memulai musik
  } else {
      audio.pause(); // Menghentikan musik jika sudah bermain
      audio.currentTime = 0; // Mengembalikan ke awal
  }
}
