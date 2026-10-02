const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const voter_id = document.getElementById('voter-id').value;
  
  if (voter_id.toLowerCase() === 'admin') {
    window.location.replace('https://decentralized-voting-system-one.vercel.app/admin.html');
  } else {
    window.location.replace('https://decentralized-voting-system-one.vercel.app/index.html');
  }
});
