#!/usr/bin/node
/**
 *Write a script that prints all characters of a Star Wars movie:
 *The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name by line
* You must use the Star wars API
* You must use the module request
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) console.log('error:', error);
  else {
    if (response.statusCode === 200) {
      const charactersUrls = JSON.parse(body).characters;
      charactersUrls.forEach(characterUrl => {
        request(characterUrl, function (error, response, body) {
          if (error) console.log('error:', error);
          else {
            if (response.statusCode === 200) console.log(JSON.parse(body).name);
          }
        });
      });
    }
  }
});
