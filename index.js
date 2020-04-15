const fetchPromise = fetch("http://switch-hub.local/account");
// Target main element
const main = document.getElementById("main");
fetchPromise.then(response => {
  return response.json();
}).then(people => {
  const names = people.id;
  // Append names to main element
  main.innerHTML = names;
});