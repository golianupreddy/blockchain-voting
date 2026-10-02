window.App = {
  eventStart: function() {
    // ---- IKIKADA PASTE CHEY ----
    const urlParams = new URLSearchParams(window.location.search);
    const authParam = urlParams.get("Authorization");
    if (authParam) {
      const tokenValue = authParam.replace("Bearer ", "");
      if (window.location.pathname.includes("admin")) {
        localStorage.setItem("jwtTokenAdmin", tokenValue);
      } else {
        localStorage.setItem("jwtTokenVoter", tokenValue);
      }
    }
    // ----------------------------

    var provider = new Web3.providers.HttpProvider("http://127.0.0.1:9545");
    ...