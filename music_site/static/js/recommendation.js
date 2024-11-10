    // Function to play the selected song
    function playSong(src) {
      const audioPlayer = document.getElementById('audio-player');
      const audioSource = document.getElementById('audio-source');
      const nowPlaying = document.getElementById('now-playing');

      audioSource.src = src;
      audioPlayer.load();
      audioPlayer.play();

      nowPlaying.textContent = "Playing: " + src.split('/').pop(); // Display song name
    }
