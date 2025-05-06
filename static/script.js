function factorial() {
  fetch('/factorial/' + $('#factorial').val())
  .then( (response) => { 
    return response.text();
  }).then( (data) => {
    $('#result').html(data);
  });
}

function fibonacci() {
  fetch('/fibonacci/' + $('#fibonacci').val())
  .then( (response) => { 
    return response.text();
  }).then( (data) => {
    $('#result').html(data);
  });
}

function average() {
  // ? y=123s & x=23
  // root/average?num1=3&num2=4
  fetch('/average?num1=' + $('#avg1').val() + '&num2=' + $('#avg2').val())
  .then( (response) => { 
    return response.text();
  }).then( (data) => {
    $('#result').html(data);
  });
}

function genJSON() {
  return {
    "factorial": $("#factorial").val(),
    "fibonacci": $("#fibonacci").val(),
    "avg1": $("#avg1").val(),
    "avg2": $("#avg2").val()
  }
}

function sendJSON() {
  fetch('/json', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(genJSON())
  }).then( (response) => { 
    return response.text();
  }).then( (data) => {
    $('#result').html(data);
  });
}
