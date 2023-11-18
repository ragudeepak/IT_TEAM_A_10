document.getElementById("checkButton").addEventListener("click", function() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: "checkPhishing" }, function(response) {
      alert(response.message);
    });
  });
});
