chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "getURL") {
    sendResponse({ url: window.location.href });
  } else if (request.action === "checkPhishing") {
    // You can implement additional logic here if needed
    sendResponse({ message: "Checking for phishing..." });
  }
});
