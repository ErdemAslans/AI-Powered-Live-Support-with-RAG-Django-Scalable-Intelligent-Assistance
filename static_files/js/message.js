"use strict";

document.addEventListener("DOMContentLoaded", function () {
  const messageBox = document.getElementById("message-box");
  const closeButton = document.getElementById("close-btn");

  if (messageBox) {
    messageBox.style.display = "block"; // Mesaj kutusunu göster
  }

  if (closeButton) {
    closeButton.addEventListener("click", function () {
      if (messageBox) {
        messageBox.style.display = "none"; // Mesaj kutusunu gizle
      }
    });
  }
});
