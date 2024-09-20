#!/usr/bin/node
// Starwars API

const request = require('request');

// Function to fetch movie details
function fetchMovie (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, { json: true }, (err, res, body) => {
    if (err) {
      return console.error('Error:', err);
    }

    const characters = body.characters;
    fetchCharacters(characters);
  });
}

// Function to fetch character names in order
function fetchCharacters (characterUrls) {
  const characterPromises = characterUrls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, { json: true }, (err, res, body) => {
        if (err) {
          return reject(err);
        }
        resolve(body.name);
      });
    });
  });

  // Wait for all character names to be fetched and then print them in order
  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(err => console.error('Error:', err));
}

// Get the movie ID from command-line arguments
const args = process.argv.slice(2);
const movieId = args[0];

if (movieId) {
  fetchMovie(movieId);
} else {
  console.log('Please provide a Movie ID as a command-line argument.');
}
