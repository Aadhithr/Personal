// Get the button elements and output option select element
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const generateBtn = document.getElementById("generateBtn");
const copyBtn = document.getElementById("copyBtn");
const outputOption = document.getElementById("outputOption");
const transcriptDiv = document.getElementById("transcript");
const outputDiv = document.getElementById("summary");

let recognition;
let transcript = "";

// Check browser support for speech recognition
if (window.SpeechRecognition || window.webkitSpeechRecognition) {
  recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.continuous = true;
  recognition.interimResults = true;
} else {
  transcriptDiv.innerHTML = "Sorry, your browser doesn't support Speech Recognition.";
}

// Event listener for the "Start Recording" button
startBtn.addEventListener("click", () => {
  startBtn.disabled = true;
  stopBtn.disabled = false;
  generateBtn.disabled = true;
  transcriptDiv.innerHTML = "Recording...";

  transcript = ""; // Reset the transcript

  recognition.start();
});

// Event listener for the "Stop Recording" button
stopBtn.addEventListener("click", () => {
  recognition.stop();
  startBtn.disabled = false;
  stopBtn.disabled = true;
  generateBtn.disabled = false;
});

// Event listener for the "Generate" button
generateBtn.addEventListener("click", () => {
  const transcriptText = transcriptDiv.innerText;
  const selectedOption = outputOption.value;

  generateOutput(transcriptText, selectedOption);
});

// Event listener for the "Copy" button
copyBtn.addEventListener("click", () => {
  copyText();
});

// Event handler for speech recognition results
recognition.onresult = (event) => {
  const currentResultIndex = event.results.length - 1;
  const currentTranscript = event.results[currentResultIndex][0].transcript;

  if (event.results[currentResultIndex].isFinal) {
    transcript += currentTranscript + " ";
  }

  transcriptDiv.innerHTML = transcript;
  generateBtn.disabled = false;
};

// Event handler for speech recognition end
recognition.onend = () => {
  transcriptDiv.innerHTML += "";
};

// Event handler for speech recognition errors
recognition.onerror = (event) => {
  transcriptDiv.innerHTML = "Error occurred in recognition: " + event.error;
};

// Function to copy the transcript to the clipboard
function copyText() {
  const textToCopy = transcriptDiv.innerText;

  navigator.clipboard.writeText(textToCopy)
    .then(() => {
      console.log('Text copied to clipboard');
    })
    .catch((error) => {
      console.error('Error copying text to clipboard:', error);
    });
}

// Function to generate the output based on selected option
function generateOutput(text, option) {
  let prompt;
  if (option === "summary") {
    prompt = encodeURIComponent("Summarize key points: " + text);
  } else if (option === "guidedQuestions") {
    prompt = encodeURIComponent("Create guided questions based on the text: " + text);
  } else if (option === "quiz") {
    prompt = encodeURIComponent("Create a quiz based on the text: " + text);
  } else if (option === "todolist") {
    prompt = encodeURIComponent("Create a todo list based on: " + text);
  } else {
    console.error("Invalid output option");
    return;
  }

  const ws = new WebSocket(`wss://backend.buildpicoapps.com/ask_ai_streaming?app_id=tough-natural&prompt=${prompt}`);
  let summary = ""; // Accumulate the summary text

  // Event listener for WebSocket messages
  ws.addEventListener("message", (event) => {
    summary += event.data;
  });

  // Event listener for WebSocket close
  ws.addEventListener("close", (event) => {
    console.log("Connection closed", event.code, event.reason);
    if (event.code !== 1000) {
      alert("Oops, we ran into an error. Refresh the page and try again.");
    } else {
      // Display the generated output
      outputDiv.innerText = summary;
      console.log("Generated Output:", summary); // Display output in console
    }
  });

  // Event listener for WebSocket errors
  ws.addEventListener("error", (error) => {
    console.log('WebSocket error', error);
    alert("Oops, we ran into an error. Refresh the page and try again.");
  });
}
