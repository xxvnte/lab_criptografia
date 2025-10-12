(async () => {
  const p = "usertest";
  if (!window.CryptoJS) {
    await new Promise((r) => {
      const s = document.createElement("script");
      s.src =
        "https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js";
      s.onload = r;
      document.head.appendChild(s);
    });
  }
  const h = CryptoJS.MD5(p).toString();
  console.log(h);
  return h;
})();
