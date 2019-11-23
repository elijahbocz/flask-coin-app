var data = null;

var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function () {
  if (this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("GET", "https://api.coingecko.com/api/v3/coins/list");
xhr.setRequestHeader("cache-control", "no-cache");
xhr.setRequestHeader("Postman-Token", "b51fa0cc-9416-4a3d-a283-a83ec97cd24d");

xhr.send(data);

console.log(data);

function matchName(input) {
  const reg = new RegExp(input.split('').join('\\w*').replace(/\W/, ""), 'i');
  return names.filter(function(name) {
    if (name.match(reg)) {
      return name;
    }
  });
}

function changeInput(val) {
  var autoCompleteResult = matchName(val);
  document.getElementById("result").innerHTML = autoCompleteResult;
}