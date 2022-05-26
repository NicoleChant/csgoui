import os

def test_number_of_images():
    assert len(os.listdir('images')) == 3

def test_logo_exists():
    assert "csgo_logo.png" in os.listdir('images')

def test_theme_exists():
    assert "csgo-media.jpg" in os.listdir('images')

def test_snap_exists():
    assert "csgo_snap.jpg" in os.listdir('images')

def test_sound_file_exists():
    assert "csgoaudio.wav" in os.listdir()
