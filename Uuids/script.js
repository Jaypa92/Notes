/* uuid (universally unique identifier) is a 128 bit identifier that is used to uniquely identify objects, entities, or data across
distributed systems. They are commonly used in databases and have 5 different versions. v4 is the most commonly used version. 
They are good for avoiding data ID collisions, security purposes, and can even be used as the primary key in databases instead
of auto incrementing integers. */

/* In Javascript, the uuid library has to be installed ex: npm install uuid. It then has to be imported before it canbe used. */

const {v4 : uuidv4} = require('uuid');

console.log(uuidv4());