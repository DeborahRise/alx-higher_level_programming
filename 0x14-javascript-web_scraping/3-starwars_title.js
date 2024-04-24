#!/usr/bin/node
/**
 * Write a script that  prints the title of a Star Wars movie
 * where the episode number matches a given integer.
 * The first argument is the movie ID
 * You must use the Star wars API
 * with the endpoint https://swapi-api.alx-tools.com/api/films/:id
 * You must use the module request
 */

const request = require('request');

// Check if movie ID is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node star_wars_movie.js <movie_id>');
  process.exit(1);
}

// Extract movie ID from command line arguments
const movieId = process.argv[2];

// Construct the API URL with the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(`${movieData.title}`);
    }
  }
});
