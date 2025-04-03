document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const fileInput = document.getElementById("receiptUpload");
  const resultDiv = document.getElementById("result");
  
  if (!fileInput.files || fileInput.files.length === 0) {
      resultDiv.className = "error";
      resultDiv.innerText = "Please select a file first.";
      return;
  }

  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append("file", file);

  try {
      resultDiv.className = "loading";
      resultDiv.innerText = "Analyzing receipt...";

      const response = await fetch("http://localhost:5000/upload", {
          method: "POST",
          body: formData
      });

      if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      resultDiv.className = "success";
      resultDiv.innerHTML = `
          <strong>Analysis Result:</strong><br>
          ${data.message}<br><br>
          <strong>Tax Tip:</strong><br>
          ${data.tax_tip}
      `;
  } catch (error) {
      console.error("Error:", error);
      resultDiv.className = "error";
      resultDiv.innerText = `Error: ${error.message}`;
  }
});