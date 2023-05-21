// JSON data containing objects
var jsonData = [];


  // Function to create a square element
  function createSquare(name) {
    var square = document.createElement('div');
    square.className = 'square';
    square.textContent = name;
    return square;
  }

  // Get the square container element
  var squareContainer = document.getElementById('square-container');

  // Iterate over each object in the JSON data
  for (var i = 0; i < jsonData.length; i++) {
    var object = jsonData[i];
    var square = createSquare(object.name);
    squareContainer.appendChild(square);
  }