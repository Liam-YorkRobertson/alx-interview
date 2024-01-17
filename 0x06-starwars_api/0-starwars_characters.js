#!/usr/bin/node

const request = require('request');

const fetchCharacterName = (characterUrl) => new Promise((resolve, reject) => {
  request(characterUrl, (err, response, body) => {
    if (err) reject(err);
    else resolve(JSON.parse(body).name);
  });
});

const filmId = process.argv[2];

request(`https://swapi-api.hbtn.io/api/films/${filmId}`, (err, response, body) => {
  if (err) process.exit(1);
  const characters = JSON.parse(body).characters;
  characters.reduce((prevPromise, characterUrl) => {
    return prevPromise.then(() => fetchCharacterName(characterUrl).then(console.log));
  }, Promise.resolve());
});
