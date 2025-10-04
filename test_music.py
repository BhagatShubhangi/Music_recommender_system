import pytest
from music import recommend_songs

def test_exact_match():
    results = recommend_songs("Good 4 U Olivia Rodrigo")
    assert isinstance(results, list)
    assert "error" not in results[0]
    assert any("Good 4 U" in song["name"] for song in results)

def test_partial_match():
    results = recommend_songs("Olivia Rodrigo")
    assert isinstance(results, list)
    assert "error" not in results[0]

def test_case_insensitive_match():
    results = recommend_songs("good 4 u olivia rodrigo")
    assert isinstance(results, list)
    assert "error" not in results[0]

def test_no_match():
    results = recommend_songs("Nonexistent Song Name")
    assert isinstance(results, list)
    assert "error" in results[0]

def test_multiple_matches():
    # Assuming "Stay" appears in multiple song names/artists
    results = recommend_songs("Stay")
    assert isinstance(results, list)
    assert "error" not in results[0]
