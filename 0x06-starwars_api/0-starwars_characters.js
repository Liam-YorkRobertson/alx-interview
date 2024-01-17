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
  if (err) return;

  Promise.all(JSON.parse(body).characters.map(fetchCharacterName))
    .then((characterNames) => characterNames.forEach(console.log))
    .catch(() => {});
});
