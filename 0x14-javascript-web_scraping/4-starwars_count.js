#!/usr/bin/node
/**
 * Write a script that   prints the number of movies where
 */

const request = require('request');

// Check if API URL is provided as an argument
if (process.argv.length < 3) {
  console.error('Usage: node wedge_antilles_movies.js <api_url>');
  process.exit(1);
}

// Extract API URL from command line arguments
const apiUrl = process.argv[2];

// Character ID for Wedge Antilles
const WEDGE_ANTILLES_ID = 18;

// Send GET request to the Star Wars API to fetch films
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const filmsData = JSON.parse(body);
      let moviesWithWedgeAntilles = 0;

      // Iterate over each film to check if Wedge Antilles is present
      filmsData.results.forEach(film => {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${WEDGE_ANTILLES_ID}/`)) {
          moviesWithWedgeAntilles++;
        }
      });

      console.log(`${moviesWithWedgeAntilles}`);
    }
  }
});
