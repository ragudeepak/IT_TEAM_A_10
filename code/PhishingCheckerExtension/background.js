chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.sendMessage(tab.id, { action: "getURL" }, function(response) {
    // Handle the response from content script (send the URL to your Flask backend)
    console.log(response.url);

    // Use XMLHttpRequest or fetch to send the URL to your backend
    fetch("http://127.0.0.1:5000/check_phishing", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url: response.url }),
    })
      .then(response => response.json())
      .then(data => {
        alert(data.is_safe
          ? `It is ${data.confidence}% safe to go`
          : "The URL may be unsafe");
      })
      .catch(error => console.error("Error:", error));
  });
});
