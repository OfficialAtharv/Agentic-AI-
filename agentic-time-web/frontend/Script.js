async function askAgent() {
  const query = document.getElementById("query").value;
  const responseBox = document.getElementById("response");

  if (!query) {
    responseBox.innerText = "Please enter a city or question.";
    return;
  }

  responseBox.innerText = "Thinking... 🤔";

  try {
    const res = await fetch("http://127.0.0.1:8000/time", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ location: query }),
    });

    const data = await res.json();
    console.log(data); // 👈 ADD THIS
    responseBox.innerText = JSON.stringify(data, null, 2);
    
  } catch (error) {
    responseBox.innerText = "Error connecting to server.";
  }
}
